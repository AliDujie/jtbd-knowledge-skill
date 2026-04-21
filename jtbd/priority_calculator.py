"""JTBD 优先级矩阵与机会分数模块

对应 SKILL.md 执行能力三+四：计算机会分数、输出优先级矩阵。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from .config import FORCE_TYPES, FORCE_LABELS

OPPORTUNITY_DIMENSIONS = ("struggle", "alternative", "market", "budget")

DIMENSION_LABELS: Dict[str, str] = {
    "struggle": "挣扎强度",
    "alternative": "替代方案不满意度",
    "market": "市场规模",
    "budget": "预算可获取性",
}

DIMENSION_WEIGHTS: Dict[str, float] = {
    "struggle": 0.30,
    "alternative": 0.25,
    "market": 0.25,
    "budget": 0.20,
}

SCORE_INTERPRETATION = [
    (4.0, 5.0, "高机会", "立即投入，这是一个强JTBD"),
    (3.0, 3.9, "中等机会", "值得进一步验证"),
    (2.0, 2.9, "低机会", "需要更多证据或换方向"),
    (1.0, 1.9, "不建议", "挣扎不够强或市场太小"),
]

SCORING_RUBRICS: Dict[str, Dict[int, str]] = {
    "struggle": {
        5: "客户主动投入大量时间精力寻找解决方案，表现出强烈情绪",
        4: "客户有明确的补偿行为（组合多个工具、自制解决方案）",
        3: "客户承认问题存在，偶尔寻找解决方案",
        2: "客户知道问题但接受现状",
        1: "客户未意识到问题或认为不重要",
    },
    "alternative": {
        5: "没有可用的替代方案，或现有方案极差",
        4: "现有方案存在明显权衡，客户被迫妥协",
        3: "现有方案基本可用但有不满",
        2: "现有方案较好，只有小问题",
        1: "现有方案很好，客户满意",
    },
    "market": {
        5: "大众市场，影响数百万人",
        4: "大型细分市场",
        3: "中型细分市场",
        2: "小众市场",
        1: "极小众",
    },
    "budget": {
        5: "客户已在替代方案上花费大量金钱（可从多个预算中抢钱）",
        4: "客户有明确预算用于解决此问题",
        3: "客户愿意付费但金额不确定",
        2: "客户习惯免费方案",
        1: "客户不愿意为此付费",
    },
}


@dataclass
class JobScore:
    """单个 Job 的机会评分"""
    job_description: str
    jtbd_statement: str = ""
    scores: Dict[str, int] = field(default_factory=dict)
    score_reasons: Dict[str, str] = field(default_factory=dict)
    force_scores: Dict[str, int] = field(default_factory=dict)

    @property
    def opportunity_score(self) -> float:
        if not self.scores:
            return 0.0
        total = 0.0
        for dim, weight in DIMENSION_WEIGHTS.items():
            total += self.scores.get(dim, 0) * weight
        return round(total, 2)

    @property
    def net_force(self) -> float:
        push = self.force_scores.get("push", 0)
        pull = self.force_scores.get("pull", 0)
        anxiety = self.force_scores.get("anxiety", 0)
        inertia = self.force_scores.get("inertia", 0)
        return (push + pull) - (anxiety + inertia)

    @property
    def level(self) -> str:
        s = self.opportunity_score
        for low, high, label, _ in SCORE_INTERPRETATION:
            if low <= s <= high:
                return label
        return "未评估"

    @property
    def action(self) -> str:
        s = self.opportunity_score
        for low, high, _, act in SCORE_INTERPRETATION:
            if low <= s <= high:
                return act
        return "需要评估"


@dataclass
class PriorityMatrix:
    """优先级矩阵"""
    jobs: List[JobScore] = field(default_factory=list)

    def ranked(self) -> List[JobScore]:
        return sorted(self.jobs, key=lambda j: j.opportunity_score, reverse=True)

    def top_n(self, n: int = 3) -> List[JobScore]:
        return self.ranked()[:n]


class PriorityAnalyzer:
    """优先级分析器

    用法示例::

        analyzer = PriorityAnalyzer()
        job = analyzer.add_job("在出差时快速找到合适住处")
        analyzer.score_job(job, "struggle", 4, "用户平均花30分钟比价")
        analyzer.score_job(job, "alternative", 3, "携程可用但体验一般")
        analyzer.score_job(job, "market", 4, "商旅市场规模大")
        analyzer.score_job(job, "budget", 4, "企业有差旅预算")
        analyzer.score_forces(job, push=4, pull=3, anxiety=2, inertia=2)
        print(analyzer.render_markdown())
    """

    def __init__(self) -> None:
        self.matrix = PriorityMatrix()

    def add_job(self, description: str, jtbd_statement: str = "") -> JobScore:
        job = JobScore(job_description=description, jtbd_statement=jtbd_statement)
        self.matrix.jobs.append(job)
        return job

    def score_job(self, job: JobScore, dimension: str, score: int, reason: str = "") -> None:
        if dimension not in OPPORTUNITY_DIMENSIONS:
            raise ValueError(f"未知维度: {dimension}，可选: {OPPORTUNITY_DIMENSIONS}")
        if not 1 <= score <= 5:
            raise ValueError(f"分数 {score} 超出范围 1-5")
        job.scores[dimension] = score
        if reason:
            job.score_reasons[dimension] = reason

    def score_forces(self, job: JobScore, push: int = 0, pull: int = 0,
                     anxiety: int = 0, inertia: int = 0) -> None:
        for name, val in [("push", push), ("pull", pull), ("anxiety", anxiety), ("inertia", inertia)]:
            if val and not 1 <= val <= 5:
                raise ValueError(f"{name} 分数 {val} 超出范围 1-5")
            if val:
                job.force_scores[name] = val

    def get_rubric(self, dimension: str) -> Dict[int, str]:
        return SCORING_RUBRICS.get(dimension, {})

    def render_markdown(self) -> str:
        ranked = self.matrix.ranked()
        lines = ["# JTBD 优先级矩阵\n"]

        lines.append("| 排名 | Job描述 | 机会分数 | 净推动力 | 建议行动 |")
        lines.append("|------|---------|---------|---------|---------|")
        for i, job in enumerate(ranked, 1):
            net = f"+{job.net_force}" if job.net_force >= 0 else str(job.net_force)
            lines.append(f"| {i} | {job.job_description} | {job.opportunity_score} | {net} | {job.action} |")
        lines.append("")

        for i, job in enumerate(ranked, 1):
            lines.append(f"## 第{i}名: {job.job_description}\n")
            if job.jtbd_statement:
                lines.append(f"**JTBD 描述:** {job.jtbd_statement}\n")
            lines.append(f"**机会分数:** {job.opportunity_score} ({job.level})\n")

            if job.scores:
                lines.append("**维度评分:**")
                for dim in OPPORTUNITY_DIMENSIONS:
                    if dim in job.scores:
                        label = DIMENSION_LABELS[dim]
                        weight = DIMENSION_WEIGHTS[dim]
                        score = job.scores[dim]
                        reason = job.score_reasons.get(dim, "")
                        line = f"- {label}: {score}/5 (权重{weight:.0%})"
                        if reason:
                            line += f" — {reason}"
                        lines.append(line)
                lines.append("")

            if job.force_scores:
                lines.append("**四力分析:**")
                for ft in FORCE_TYPES:
                    if ft in job.force_scores:
                        lines.append(f"- {FORCE_LABELS[ft]}: {job.force_scores[ft]}/5")
                lines.append(f"- 净推动力: {job.net_force}")
                lines.append("")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        return {
            "jobs": [
                {
                    "description": j.job_description,
                    "jtbd_statement": j.jtbd_statement,
                    "opportunity_score": j.opportunity_score,
                    "level": j.level,
                    "action": j.action,
                    "scores": j.scores,
                    "score_reasons": j.score_reasons,
                    "force_scores": j.force_scores,
                    "net_force": j.net_force,
                }
                for j in self.matrix.ranked()
            ]
        }
