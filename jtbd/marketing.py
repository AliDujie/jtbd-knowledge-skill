"""JTBD 营销文案生成模块

对应 SKILL.md 执行能力六：生成 JTBD 营销文案。
基于四力模型生成不同角度的文案方案。
"""

from dataclasses import dataclass, field
from typing import Dict, List


COPY_PURPOSES = ("ad", "landing_page", "social_media", "email")

PURPOSE_LABELS: Dict[str, str] = {
    "ad": "广告",
    "landing_page": "落地页",
    "social_media": "社交媒体",
    "email": "邮件",
}

COPY_ANGLES = ("push_driven", "pull_driven", "anxiety_elimination")

ANGLE_LABELS: Dict[str, str] = {
    "push_driven": "推力驱动（痛点共鸣）",
    "pull_driven": "拉力驱动（愿景吸引）",
    "anxiety_elimination": "焦虑消除（降低门槛）",
}

HEADLINE_FORMULAS: Dict[str, str] = {
    "struggle_resonance": "还在为{struggle}烦恼？",
    "progress_vision": "{desired_outcome}，从{product}开始",
    "contrast": "从{old_state}到{new_state}",
    "question": "如果{desired_outcome}只需要{simple_action}呢？",
}


@dataclass
class CopyBrief:
    """文案创作简报"""
    product: str
    target_job: str
    struggle: str
    desired_outcome: str
    key_anxieties: List[str] = field(default_factory=list)
    key_inertias: List[str] = field(default_factory=list)
    tone: str = "专业但亲切"
    purpose: str = "landing_page"


@dataclass
class CopyDraft:
    """单个文案方案"""
    angle: str
    headline: str
    subheadline: str = ""
    body: str = ""
    anxiety_response: str = ""
    inertia_response: str = ""
    cta: str = ""


@dataclass
class CopyPlan:
    """完整文案方案"""
    brief: CopyBrief
    drafts: List[CopyDraft] = field(default_factory=list)
    principles: List[str] = field(default_factory=list)


COPY_PRINCIPLES = [
    "用客户自己的语言描述挣扎（不要用行业术语）",
    "帮客户可视化使用产品后的进步（'新我'画面）",
    "直接攻击焦虑（降低采用门槛）",
    "直接攻击惯性（给出切换的理由和路径）",
    "不要描述功能列表，描述生活如何变好",
]


class MarketingCopywriter:
    """营销文案生成器

    用法示例::

        writer = MarketingCopywriter()
        writer.set_brief(
            product="旅行预订平台",
            target_job="出差时快速找到合适住处",
            struggle="每次出差都要花30分钟比价找酒店",
            desired_outcome="专注工作而不是为住宿烦恼",
            purpose="landing_page",
        )
        writer.add_anxiety("不确定平台上的酒店评价是否真实")
        writer.add_inertia("已经习惯用携程了")
        plan = writer.generate()
        print(writer.render_markdown(plan))
    """

    def __init__(self) -> None:
        self._brief: CopyBrief = None
        self._anxieties: List[str] = []
        self._inertias: List[str] = []

    def set_brief(self, product: str, target_job: str, struggle: str,
                  desired_outcome: str, purpose: str = "landing_page",
                  tone: str = "专业但亲切") -> "MarketingCopywriter":
        if purpose not in COPY_PURPOSES:
            raise ValueError(f"未知用途: {purpose}，可选: {COPY_PURPOSES}")
        self._brief = CopyBrief(
            product=product, target_job=target_job,
            struggle=struggle, desired_outcome=desired_outcome,
            purpose=purpose, tone=tone,
        )
        return self

    def add_anxiety(self, anxiety: str) -> "MarketingCopywriter":
        self._anxieties.append(anxiety)
        return self

    def add_inertia(self, inertia: str) -> "MarketingCopywriter":
        self._inertias.append(inertia)
        return self

    def generate(self) -> CopyPlan:
        if not self._brief:
            raise ValueError("请先调用 set_brief 设置文案简报")

        b = self._brief
        b.key_anxieties = self._anxieties
        b.key_inertias = self._inertias
        drafts: List[CopyDraft] = []

        drafts.append(CopyDraft(
            angle="push_driven",
            headline=f"还在为{b.struggle}烦恼？",
            subheadline=f"你不是一个人。每天有数万人面临同样的困扰。",
            body=(
                f"我们理解{b.struggle}带来的挫败感。"
                f"这不仅浪费时间，更让你无法专注于真正重要的事。\n\n"
                f"{b.product}帮你解决这个问题，让你{b.desired_outcome}。"
            ),
            anxiety_response=self._format_anxiety_response(b),
            inertia_response=self._format_inertia_response(b),
            cta=f"立即体验{b.product}",
        ))

        drafts.append(CopyDraft(
            angle="pull_driven",
            headline=f"{b.desired_outcome}，从{b.product}开始",
            subheadline=f"想象一下，如果{b.struggle.replace('每次', '再也不用')}",
            body=(
                f"使用{b.product}的人已经实现了这样的改变：\n"
                f"从为{b.struggle}到{b.desired_outcome}。\n\n"
                f"你也可以。"
            ),
            anxiety_response=self._format_anxiety_response(b),
            inertia_response=self._format_inertia_response(b),
            cta=f"开始你的改变",
        ))

        drafts.append(CopyDraft(
            angle="anxiety_elimination",
            headline=f"担心切换到{b.product}？我们理解你的顾虑",
            subheadline="每一个顾虑，我们都认真对待",
            body=self._format_full_anxiety_body(b),
            anxiety_response="",
            inertia_response=self._format_inertia_response(b),
            cta=f"无风险试用{b.product}",
        ))

        return CopyPlan(brief=b, drafts=drafts, principles=COPY_PRINCIPLES)

    def _format_anxiety_response(self, brief: CopyBrief) -> str:
        if not brief.key_anxieties:
            return ""
        lines = ["你可能在想："]
        for a in brief.key_anxieties:
            lines.append(f"- \"{a}\" — 我们的回应：[针对性解决方案]")
        return "\n".join(lines)

    def _format_inertia_response(self, brief: CopyBrief) -> str:
        if not brief.key_inertias:
            return ""
        lines = ["切换很简单："]
        for idx, iner in enumerate(brief.key_inertias, 1):
            lines.append(f"- 关于\"{iner}\"：[具体的过渡方案]")
        return "\n".join(lines)

    def _format_full_anxiety_body(self, brief: CopyBrief) -> str:
        if not brief.key_anxieties:
            return f"我们知道尝试新产品需要勇气。{brief.product}提供无风险试用，让你安心体验。"
        lines = [f"我们知道尝试新产品需要勇气。以下是用户最常见的顾虑：\n"]
        for a in brief.key_anxieties:
            lines.append(f"**\"{a}\"**")
            lines.append(f"→ [针对性解决方案和证据]\n")
        lines.append(f"{brief.product}提供无风险试用，让你安心体验。")
        return "\n".join(lines)

    @staticmethod
    def render_markdown(plan: CopyPlan) -> str:
        b = plan.brief
        lines = [f"# 营销文案方案 — {b.product}\n"]
        lines.append(f"**目标 Job:** {b.target_job}")
        lines.append(f"**核心挣扎:** {b.struggle}")
        lines.append(f"**期望进步:** {b.desired_outcome}")
        lines.append(f"**文案用途:** {PURPOSE_LABELS.get(b.purpose, b.purpose)}")
        lines.append(f"**语调:** {b.tone}\n")

        for i, draft in enumerate(plan.drafts, 1):
            angle_label = ANGLE_LABELS.get(draft.angle, draft.angle)
            lines.append(f"---\n\n## 方案{i}: {angle_label}\n")
            lines.append(f"### 标题\n\n**{draft.headline}**\n")
            if draft.subheadline:
                lines.append(f"*{draft.subheadline}*\n")
            lines.append(f"### 正文\n\n{draft.body}\n")
            if draft.anxiety_response:
                lines.append(f"### 消除焦虑\n\n{draft.anxiety_response}\n")
            if draft.inertia_response:
                lines.append(f"### 克服惯性\n\n{draft.inertia_response}\n")
            lines.append(f"### 行动号召\n\n**{draft.cta}**\n")

        lines.append("---\n\n## 文案原则提醒\n")
        for p in plan.principles:
            lines.append(f"- {p}")

        return "\n".join(lines)

    @staticmethod
    def render_json(plan: CopyPlan) -> Dict:
        b = plan.brief
        return {
            "product": b.product,
            "target_job": b.target_job,
            "struggle": b.struggle,
            "desired_outcome": b.desired_outcome,
            "purpose": b.purpose,
            "drafts": [
                {"angle": d.angle, "headline": d.headline,
                 "subheadline": d.subheadline, "body": d.body, "cta": d.cta}
                for d in plan.drafts
            ],
        }
