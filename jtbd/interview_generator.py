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

    def include_dimensions(self, dimensions: List[str]) -> "InterviewBuilder":
        for d in dimensions:
            if d not in INTERVIEW_DIMENSIONS and d != "inertia":
                raise ValueError(
                    f"未知维度: {d}，可选: {', '.join(INTERVIEW_DIMENSIONS)}, inertia"
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
