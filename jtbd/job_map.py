"""JTBD Universal Job Map 模块

基于 Ulwick ODI 方法论的 Universal Job Map 工具。
将任何 Job 分解为8个标准阶段，并关联 Desired Outcome Statements。

Universal Job Map 8阶段:
1. Define (定义) — 确定目标和规划方法
2. Locate (定位) — 收集完成Job所需的输入和信息
3. Prepare (准备) — 在执行前设置环境和组织输入
4. Confirm (确认) — 在执行前验证准备就绪
5. Execute (执行) — 执行Job的核心动作
6. Monitor (监控) — 跟踪执行是否按预期进行
7. Modify (修正) — 根据监控结果做调整
8. Conclude (结束) — 完成Job并整理善后
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


JOB_MAP_STAGES = (
    "define",
    "locate",
    "prepare",
    "confirm",
    "execute",
    "monitor",
    "modify",
    "conclude",
)

STAGE_LABELS: Dict[str, str] = {
    "define": "定义 (Define)",
    "locate": "定位 (Locate)",
    "prepare": "准备 (Prepare)",
    "confirm": "确认 (Confirm)",
    "execute": "执行 (Execute)",
    "monitor": "监控 (Monitor)",
    "modify": "修正 (Modify)",
    "conclude": "结束 (Conclude)",
}

STAGE_DESCRIPTIONS: Dict[str, str] = {
    "define": "确定Job的目标、规划方法、决定要做什么",
    "locate": "收集完成Job所需的物品、信息和资源",
    "prepare": "设置环境、组织输入、为执行做好准备",
    "confirm": "在正式执行前验证一切准备就绪",
    "execute": "执行Job的核心任务动作",
    "monitor": "跟踪和评估执行是否按预期进行",
    "modify": "根据监控结果做出调整和改进",
    "conclude": "完成Job、整理善后、存档或清理",
}

STAGE_GUIDING_QUESTIONS: Dict[str, List[str]] = {
    "define": [
        "客户在这个阶段要确定什么目标？",
        "客户如何决定采用什么方法？",
        "客户需要考虑哪些约束条件？",
    ],
    "locate": [
        "客户需要收集什么信息或物品？",
        "信息来源有哪些？哪些难以获取？",
        "客户如何判断信息是否足够？",
    ],
    "prepare": [
        "客户在执行前需要做哪些准备工作？",
        "准备过程中最耗时或最容易出错的步骤是什么？",
        "有哪些准备工作可以提前完成或自动化？",
    ],
    "confirm": [
        "客户如何确认准备工作已完成？",
        "有哪些验证步骤容易被忽略？",
        "确认不充分会导致什么后果？",
    ],
    "execute": [
        "核心执行步骤是什么？",
        "执行过程中最容易出问题的环节？",
        "客户在执行时最希望减少什么？（时间、错误、精力）",
    ],
    "monitor": [
        "客户如何知道执行是否正常？",
        "需要监控哪些关键指标？",
        "监控信息是否及时、准确？",
    ],
    "modify": [
        "当发现偏差时，客户如何调整？",
        "调整过程的成本有多高？",
        "有哪些常见的调整场景？",
    ],
    "conclude": [
        "Job完成后客户需要做什么善后工作？",
        "如何评估Job的完成质量？",
        "有哪些收尾工作容易被遗忘？",
    ],
}


@dataclass
class StageNeed:
    """某个阶段的具体需求"""
    stage: str
    description: str
    importance: int = 5
    satisfaction: int = 5
    evidence: str = ""

    @property
    def opportunity(self) -> float:
        return self.importance + max(self.importance - self.satisfaction, 0)


@dataclass
class JobMapStage:
    """Job Map 中的一个阶段"""
    stage: str
    context: str = ""
    needs: List[StageNeed] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    current_solutions: List[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return STAGE_LABELS.get(self.stage, self.stage)

    @property
    def avg_opportunity(self) -> float:
        if not self.needs:
            return 0.0
        return round(sum(n.opportunity for n in self.needs) / len(self.needs), 2)


@dataclass
class JobMap:
    """完整的 Universal Job Map"""
    job_statement: str
    executor: str = ""
    stages: Dict[str, JobMapStage] = field(default_factory=dict)

    def get_stage(self, stage: str) -> Optional[JobMapStage]:
        return self.stages.get(stage)

    def get_top_opportunities(self, n: int = 5) -> List[StageNeed]:
        all_needs: List[StageNeed] = []
        for s in self.stages.values():
            all_needs.extend(s.needs)
        return sorted(all_needs, key=lambda x: x.opportunity, reverse=True)[:n]

    def get_underserved_stages(self, threshold: float = 12.0) -> List[JobMapStage]:
        return [
            s for s in self.stages.values()
            if s.avg_opportunity >= threshold
        ]


class JobMapBuilder:
    """Universal Job Map 构建器

    用法示例::

        builder = JobMapBuilder("管理商务出差的住宿安排")
        builder.set_executor("商旅经理")
        builder.add_stage_context("define", "确定出差日期、目的地、预算标准")
        builder.add_need("define", "快速确定符合公司差旅标准的预算范围",
                         importance=8, satisfaction=4)
        builder.add_need("locate", "找到目的地附近所有符合标准的酒店",
                         importance=9, satisfaction=3)
        builder.add_pain_point("locate", "需要在多个平台反复比较")
        job_map = builder.build()
        print(JobMapBuilder.render_markdown(job_map))
    """

    def __init__(self, job_statement: str):
        self._job = job_statement
        self._executor = ""
        self._stages: Dict[str, JobMapStage] = {}
        for stage in JOB_MAP_STAGES:
            self._stages[stage] = JobMapStage(stage=stage)

    def set_executor(self, executor: str) -> "JobMapBuilder":
        self._executor = executor
        return self

    def add_stage_context(self, stage: str, context: str) -> "JobMapBuilder":
        self._validate_stage(stage)
        self._stages[stage].context = context
        return self

    def add_need(self, stage: str, description: str,
                 importance: int = 5, satisfaction: int = 5,
                 evidence: str = "") -> "JobMapBuilder":
        self._validate_stage(stage)
        self._validate_score(importance, "importance")
        self._validate_score(satisfaction, "satisfaction")
        need = StageNeed(
            stage=stage, description=description,
            importance=importance, satisfaction=satisfaction,
            evidence=evidence,
        )
        self._stages[stage].needs.append(need)
        return self

    def add_pain_point(self, stage: str, pain: str) -> "JobMapBuilder":
        self._validate_stage(stage)
        self._stages[stage].pain_points.append(pain)
        return self

    def add_current_solution(self, stage: str, solution: str) -> "JobMapBuilder":
        self._validate_stage(stage)
        self._stages[stage].current_solutions.append(solution)
        return self

    def build(self) -> JobMap:
        return JobMap(
            job_statement=self._job,
            executor=self._executor,
            stages=dict(self._stages),
        )

    @staticmethod
    def _validate_stage(stage: str) -> None:
        if stage not in JOB_MAP_STAGES:
            raise ValueError(f"未知阶段: {stage}，可选: {JOB_MAP_STAGES}")

    @staticmethod
    def _validate_score(score: int, name: str) -> None:
        if not 1 <= score <= 10:
            raise ValueError(f"{name} 分数 {score} 超出范围 1-10")

    @staticmethod
    def render_markdown(job_map: JobMap) -> str:
        lines = [f"# Universal Job Map\n"]
        lines.append(f"**Job:** {job_map.job_statement}")
        if job_map.executor:
            lines.append(f"**执行者:** {job_map.executor}")
        lines.append("")

        top_opps = job_map.get_top_opportunities(5)
        if top_opps:
            lines.append("## 最高机会需求 (Top Opportunities)\n")
            lines.append("| 阶段 | 需求 | 重要性 | 满意度 | 机会分 |")
            lines.append("|------|------|--------|--------|--------|")
            for need in top_opps:
                stage_label = STAGE_LABELS.get(need.stage, need.stage)
                lines.append(
                    f"| {stage_label} | {need.description} "
                    f"| {need.importance} | {need.satisfaction} | {need.opportunity:.1f} |"
                )
            lines.append("")

        for stage_key in JOB_MAP_STAGES:
            stage = job_map.stages.get(stage_key)
            if not stage:
                continue
            label = STAGE_LABELS[stage_key]
            desc = STAGE_DESCRIPTIONS[stage_key]
            lines.append(f"## 阶段{JOB_MAP_STAGES.index(stage_key)+1}: {label}\n")
            lines.append(f"*{desc}*\n")

            if stage.context:
                lines.append(f"**场景描述:** {stage.context}\n")

            if stage.needs:
                lines.append("**需求与机会:**\n")
                sorted_needs = sorted(stage.needs, key=lambda n: n.opportunity, reverse=True)
                for need in sorted_needs:
                    opp = need.opportunity
                    indicator = "🔴" if opp >= 12 else ("🟡" if opp >= 10 else "🟢")
                    lines.append(
                        f"- {indicator} {need.description} "
                        f"(重要性:{need.importance} 满意度:{need.satisfaction} "
                        f"机会分:{opp:.1f})"
                    )
                    if need.evidence:
                        lines.append(f"  - 证据: {need.evidence}")
                lines.append("")

            if stage.pain_points:
                lines.append("**痛点:**\n")
                for p in stage.pain_points:
                    lines.append(f"- {p}")
                lines.append("")

            if stage.current_solutions:
                lines.append("**当前解决方案:**\n")
                for s in stage.current_solutions:
                    lines.append(f"- {s}")
                lines.append("")

            if not stage.needs and not stage.pain_points and not stage.context:
                questions = STAGE_GUIDING_QUESTIONS.get(stage_key, [])
                if questions:
                    lines.append("**待探索问题:**\n")
                    for q in questions:
                        lines.append(f"- [ ] {q}")
                    lines.append("")

        underserved = job_map.get_underserved_stages()
        if underserved:
            lines.append("## 机会总结\n")
            lines.append(f"发现 {len(underserved)} 个高机会阶段（平均机会分≥12）：\n")
            for s in sorted(underserved, key=lambda x: x.avg_opportunity, reverse=True):
                lines.append(f"- **{s.label}** (平均机会分: {s.avg_opportunity})")
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def render_json(job_map: JobMap) -> Dict:
        return {
            "job_statement": job_map.job_statement,
            "executor": job_map.executor,
            "stages": {
                key: {
                    "label": stage.label,
                    "context": stage.context,
                    "avg_opportunity": stage.avg_opportunity,
                    "needs": [
                        {
                            "description": n.description,
                            "importance": n.importance,
                            "satisfaction": n.satisfaction,
                            "opportunity": n.opportunity,
                            "evidence": n.evidence,
                        }
                        for n in stage.needs
                    ],
                    "pain_points": stage.pain_points,
                    "current_solutions": stage.current_solutions,
                }
                for key, stage in job_map.stages.items()
            },
            "top_opportunities": [
                {
                    "stage": n.stage,
                    "description": n.description,
                    "opportunity": n.opportunity,
                }
                for n in job_map.get_top_opportunities(10)
            ],
        }
