"""JTBD 进步力量分析模块

提供四种力量（推力、拉力、焦虑、惯性）的结构化分析工具。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import FORCE_TYPES, FORCE_LABELS, FORCE_CATEGORIES
from .templates import FORCES_ANALYSIS_TEMPLATE


@dataclass
class ForceItem:
    """单条力量分析项"""
    force_type: str
    sub_type: str
    description: str
    intensity: int = 3
    evidence: str = ""
    source: str = ""


@dataclass
class ForcesProfile:
    """完整的四力分析画像"""
    items: List[ForceItem] = field(default_factory=list)

    def add(self, force_type: str, sub_type: str, description: str,
            intensity: int = 3, evidence: str = "", source: str = "") -> ForceItem:
        if force_type not in FORCE_TYPES:
            raise ValueError(f"未知力量类型: {force_type}，可选: {FORCE_TYPES}")
        if not 1 <= intensity <= 5:
            raise ValueError(f"强度 {intensity} 超出范围 1-5")
        item = ForceItem(force_type=force_type, sub_type=sub_type,
                         description=description, intensity=intensity,
                         evidence=evidence, source=source)
        self.items.append(item)
        return item

    def by_type(self, force_type: str) -> List[ForceItem]:
        return [i for i in self.items if i.force_type == force_type]

    def by_category(self, category: str) -> List[ForceItem]:
        return [i for i in self.items
                if FORCE_CATEGORIES.get(i.force_type) == category]

    def score(self, force_type: str) -> int:
        return sum(i.intensity for i in self.by_type(force_type))

    def total_generating(self) -> int:
        return sum(i.intensity for i in self.by_category("demand_generating"))

    def total_reducing(self) -> int:
        return sum(i.intensity for i in self.by_category("demand_reducing"))

    def net_demand(self) -> int:
        return self.total_generating() - self.total_reducing()

    def summary(self) -> Dict[str, int]:
        result: Dict[str, int] = {}
        for ft in FORCE_TYPES:
            result[ft] = self.score(ft)
        result["generating"] = self.total_generating()
        result["reducing"] = self.total_reducing()
        result["net"] = self.net_demand()
        return result

    def diagnose(self) -> List[str]:
        insights: List[str] = []
        net = self.net_demand()
        if net < 0:
            insights.append(
                "需求减少力量大于生成力量，客户转换动力不足。"
                "建议优先降低焦虑和惯性。"
            )
        elif net == 0:
            insights.append(
                "需求生成和减少力量持平，客户处于犹豫状态。"
                "需要增强推力/拉力或降低焦虑/惯性来打破平衡。"
            )
        else:
            insights.append("需求生成力量占优，客户有较强转换动力。")

        anxiety_items = self.by_type("anxiety")
        high_anxiety = [i for i in anxiety_items if i.intensity >= 4]
        if high_anxiety:
            insights.append(
                f"发现 {len(high_anxiety)} 项高强度焦虑，"
                "这是隐形竞争对手，应优先解决。"
            )

        inertia_items = self.by_type("inertia")
        high_inertia = [i for i in inertia_items if i.intensity >= 4]
        if high_inertia:
            insights.append(
                f"发现 {len(high_inertia)} 项高强度惯性，"
                "需要设计过渡方案帮助客户建立新习惯。"
            )
        return insights


def get_analysis_template(force_type: str) -> Optional[Dict]:
    for category_data in FORCES_ANALYSIS_TEMPLATE.values():
        if force_type in category_data:
            return category_data[force_type]
    return None


def get_guiding_questions(force_type: str) -> List[str]:
    template = get_analysis_template(force_type)
    if template:
        return template.get("questions", [])
    return []


def render_forces_markdown(profile: ForcesProfile) -> str:
    lines = ["# 进步力量分析\n"]
    summary = profile.summary()
    lines.append(f"**需求生成总分:** {summary['generating']}  ")
    lines.append(f"**需求减少总分:** {summary['reducing']}  ")
    lines.append(f"**净需求得分:** {summary['net']}\n")

    for ft in FORCE_TYPES:
        label = FORCE_LABELS[ft]
        items = profile.by_type(ft)
        lines.append(f"## {label}\n")
        if not items:
            lines.append("（暂无数据）\n")
            continue
        for item in items:
            lines.append(f"- **[{item.intensity}/5]** {item.description}")
            if item.sub_type:
                lines.append(f"  - 子类型: {item.sub_type}")
            if item.evidence:
                lines.append(f"  - 证据: {item.evidence}")
        lines.append("")

    diagnostics = profile.diagnose()
    if diagnostics:
        lines.append("## 诊断洞察\n")
        for d in diagnostics:
            lines.append(f"- {d}")
    return "\n".join(lines)
