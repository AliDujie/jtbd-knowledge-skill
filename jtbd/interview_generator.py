"""JTBD 访谈框架生成器

根据分析维度和场景自动生成定制化的访谈问题列表，
支持按维度筛选、自定义追加和输出格式化。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import AnalysisConfig, INTERVIEW_DIMENSIONS
from .templates import INTERVIEW_QUESTIONS


@dataclass
class InterviewQuestion:
    """单个访谈问题"""

    dimension: str
    question: str
    is_custom: bool = False
    priority: int = 1
    follow_up: str = ""


@dataclass
class InterviewGuide:
    """完整的访谈指南"""

    title: str
    context: str
    questions: List[InterviewQuestion] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)

    def get_by_dimension(self, dimension: str) -> List[InterviewQuestion]:
        return [q for q in self.questions if q.dimension == dimension]

    def get_high_priority(self, min_priority: int = 2) -> List[InterviewQuestion]:
        return [q for q in self.questions if q.priority >= min_priority]


DIMENSION_LABELS: Dict[str, str] = {
    "competition": "竞争理解",
    "push": "推力探索",
    "pull": "拉力探索",
    "anxiety": "焦虑识别",
    "inertia": "惯性识别",
    "validation": "需求验证",
    "job_map": "Job Map阶段探索",
    "job_drivers": "ABC驱动因素探索",
    "success_criteria": "成功标准探索",
    "obstacles": "障碍识别",
}

ALL_INTERVIEW_DIMENSIONS = (
    "competition", "push", "pull", "anxiety", "inertia",
    "validation", "job_map", "job_drivers", "success_criteria", "obstacles",
)

EXTENDED_QUESTIONS: Dict[str, List[str]] = {
    "job_map": [
        "在开始这个任务之前，你需要做哪些准备工作？",
        "你是如何确定要做什么/怎么做的？（Define阶段）",
        "你从哪里获取完成任务需要的信息？（Locate阶段）",
        "执行过程中最容易出问题的环节是什么？（Execute阶段）",
        "你怎么知道事情是否按预期进行？（Monitor阶段）",
    ],
    "job_drivers": [
        "你的社交圈或公司文化如何影响你在这方面的选择？（Attitudes）",
        "你的职业角色或家庭情况如何影响这个需求？（Background）",
        "什么具体事件或情境促使你需要完成这个任务？（Circumstances）",
        "这三种因素（社会期望、个人背景、具体情境）哪个影响最大？",
        "有没有什么外部变化让这个需求变得更紧迫？",
    ],
    "success_criteria": [
        "你怎么定义'做好了'？什么标准？",
        "如果有一个理想的解决方案，它的效果应该是什么样的？",
        "你目前的方案在多大程度上满足了这些标准？",
        "哪些标准是'必须满足'的，哪些是'锦上添花'的？",
        "你愿意为完美满足这些标准付出多少额外成本？",
    ],
    "obstacles": [
        "在尝试新方案时，什么因素让你犹豫不决？",
        "你在使用当前方案时遇到过哪些困难？",
        "如果要推荐新方案给同事，你觉得他们可能会有什么顾虑？",
        "在采用新方案的过程中，谁还参与了决策？",
        "学习使用新方案的过程中，最大的障碍是什么？",
    ],
}

INTERVIEW_TYPES = ("switch", "odi", "churn")

INTERVIEW_TYPE_LABELS: Dict[str, str] = {
    "switch": "Switch访谈 — 聚焦客户转换行为的四力分析",
    "odi": "ODI访谈 — 聚焦Job Map各阶段的需求挖掘",
    "churn": "流失访谈 — 聚焦客户离开原因和未满足需求",
}

DEFAULT_TIPS = [
    "问做过什么而非想要什么（揭示偏好 > 陈述偏好）",
    "寻找'能量'——情感强度、身体语言变化",
    "从宽到窄识别挣扎最强烈的群体",
    "团队一起参与访谈建立共识",
    "将数据与综合分析分开展示",
    "保持好奇心，不要引导受访者的回答",
    "关注具体事件和行为，而非抽象观点",
    "当受访者说'我觉得...'时，追问'能举个例子吗？'",
]


class InterviewBuilder:
    """访谈框架构建器

    用法示例::

        builder = InterviewBuilder("旅行预订平台用户访谈")
        builder.set_context("针对过去3个月内使用过竞品的用户")
        builder.include_dimensions(["competition", "push", "pull", "anxiety"])
        builder.add_custom_question("push", "你最近一次出差遇到的最大住宿问题是什么？", priority=3)
        guide = builder.build()
        print(builder.render_markdown(guide))
    """

    def __init__(self, title: str, config: Optional[AnalysisConfig] = None):
        self.title = title
        self.config = config or AnalysisConfig()
        self._context = ""
        self._dimensions: List[str] = list(self.config.interview_dimensions)
        self._custom_questions: List[InterviewQuestion] = []
        self._extra_tips: List[str] = []

    def set_context(self, context: str) -> "InterviewBuilder":
        self._context = context
        return self

    def set_interview_type(self, interview_type: str) -> "InterviewBuilder":
        if interview_type not in INTERVIEW_TYPES:
            raise ValueError(
                f"未知访谈类型: {interview_type}，可选: {INTERVIEW_TYPES}"
            )
        self._interview_type = interview_type
        if interview_type == "switch":
            self._dimensions = ["competition", "push", "pull", "anxiety", "inertia"]
        elif interview_type == "odi":
            self._dimensions = ["job_map", "success_criteria", "job_drivers"]
        elif interview_type == "churn":
            self._dimensions = ["competition", "push", "obstacles", "validation"]
        return self

    def include_dimensions(self, dimensions: List[str]) -> "InterviewBuilder":
        for d in dimensions:
            if d not in ALL_INTERVIEW_DIMENSIONS:
                raise ValueError(
                    f"未知维度: {d}，可选: {', '.join(ALL_INTERVIEW_DIMENSIONS)}"
                )
        self._dimensions = dimensions
        return self

    def add_custom_question(
        self,
        dimension: str,
        question: str,
        priority: int = 1,
        follow_up: str = "",
    ) -> "InterviewBuilder":
        self._custom_questions.append(
            InterviewQuestion(
                dimension=dimension,
                question=question,
                is_custom=True,
                priority=priority,
                follow_up=follow_up,
            )
        )
        return self

    def add_tip(self, tip: str) -> "InterviewBuilder":
        self._extra_tips.append(tip)
        return self

    def build(self) -> InterviewGuide:
        questions: List[InterviewQuestion] = []

        for dim in self._dimensions:
            template_qs = INTERVIEW_QUESTIONS.get(dim, [])
            if not template_qs:
                template_qs = EXTENDED_QUESTIONS.get(dim, [])
            max_q = self.config.max_questions_per_dimension
            for q_text in template_qs[:max_q]:
                questions.append(
                    InterviewQuestion(dimension=dim, question=q_text, priority=1)
                )

        for cq in self._custom_questions:
            questions.append(cq)

        tips = list(DEFAULT_TIPS) + self._extra_tips

        return InterviewGuide(
            title=self.title,
            context=self._context,
            questions=questions,
            tips=tips,
        )

    @staticmethod
    def render_markdown(guide: InterviewGuide) -> str:
        lines = [f"# {guide.title}\n"]

        if guide.context:
            lines.append(f"**访谈背景:** {guide.context}\n")

        dims_in_order = []
        seen = set()
        for q in guide.questions:
            if q.dimension not in seen:
                dims_in_order.append(q.dimension)
                seen.add(q.dimension)

        for dim in dims_in_order:
            label = DIMENSION_LABELS.get(dim, dim)
            lines.append(f"## {label}\n")
            dim_qs = [q for q in guide.questions if q.dimension == dim]
            for i, q in enumerate(dim_qs, 1):
                marker = " ⭐" if q.priority >= 3 else ""
                custom_tag = " [自定义]" if q.is_custom else ""
                lines.append(f"{i}. {q.question}{marker}{custom_tag}")
                if q.follow_up:
                    lines.append(f"   - 追问: {q.follow_up}")
            lines.append("")

        if guide.tips:
            lines.append("## 访谈技巧\n")
            for tip in guide.tips:
                lines.append(f"- {tip}")
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def render_json(guide: InterviewGuide) -> Dict:
        return {
            "title": guide.title,
            "context": guide.context,
            "questions": [
                {
                    "dimension": q.dimension,
                    "question": q.question,
                    "is_custom": q.is_custom,
                    "priority": q.priority,
                    "follow_up": q.follow_up,
                }
                for q in guide.questions
            ],
            "tips": guide.tips,
        }
