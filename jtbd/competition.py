"""JTBD 竞争分析模块

对应 SKILL.md 执行能力五：JTBD 竞争分析。
识别真正的竞争对手、验证竞争关系、进行四力对比。
"""

from dataclasses import dataclass, field
from typing import Dict, List

from .config import FORCE_TYPES, FORCE_LABELS


COMPETITOR_CATEGORIES = ("direct", "indirect", "non_consumption")

CATEGORY_LABELS: Dict[str, str] = {
    "direct": "直接竞品",
    "indirect": "间接竞品",
    "non_consumption": "非消费方案",
}

CATEGORY_DESCRIPTIONS: Dict[str, str] = {
    "direct": "功能相似的产品",
    "indirect": "不同品类但解决同一Job的产品",
    "non_consumption": "用户自己的临时解决办法、忍受现状",
}


@dataclass
class SwitchEvidence:
    """切换证据"""
    from_product: str
    to_product: str
    user_count: int = 0
    switch_reason: str = ""


@dataclass
class ForceComparison:
    """与竞品的四力对比"""
    competitor_name: str
    push_advantage: str = ""
    pull_advantage: str = ""
    anxiety_disadvantage: str = ""
    inertia_disadvantage: str = ""


@dataclass
class Competitor:
    """竞争者"""
    name: str
    category: str
    description: str = ""
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    force_comparison: ForceComparison = None

    def __post_init__(self):
        if self.force_comparison is None:
            self.force_comparison = ForceComparison(competitor_name=self.name)


@dataclass
class CompetitiveAnalysis:
    """完整竞争分析"""
    product_name: str
    target_job: str = ""
    competitors: List[Competitor] = field(default_factory=list)
    switch_evidence: List[SwitchEvidence] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)
    strategies: List[str] = field(default_factory=list)


class CompetitionAnalyzer:
    """竞争分析器

    用法示例::

        analyzer = CompetitionAnalyzer("旅行预订平台")
        analyzer.set_target_job("在出差时快速找到合适的住处")
        analyzer.add_competitor("携程", "direct", strengths=["酒店数量多"], weaknesses=["界面复杂"])
        analyzer.add_competitor("朋友推荐", "non_consumption", strengths=["信任度高"], weaknesses=["选择有限"])
        analyzer.add_switch("携程", "旅行预订平台", 15, "界面更简洁，价格更透明")
        analyzer.set_force_comparison("携程", push_advantage="携程界面复杂导致用户流失",
                                       pull_advantage="更简洁的搜索体验",
                                       anxiety_disadvantage="新平台酒店数量是否够多",
                                       inertia_disadvantage="用户已有携程会员积分")
        print(analyzer.render_markdown())
    """

    def __init__(self, product_name: str):
        self.analysis = CompetitiveAnalysis(product_name=product_name)

    def set_target_job(self, job: str) -> None:
        self.analysis.target_job = job

    def add_competitor(self, name: str, category: str = "direct",
                       description: str = "",
                       strengths: List[str] = None,
                       weaknesses: List[str] = None) -> Competitor:
        if category not in COMPETITOR_CATEGORIES:
            raise ValueError(f"未知类别: {category}，可选: {COMPETITOR_CATEGORIES}")
        comp = Competitor(
            name=name, category=category, description=description,
            strengths=strengths or [], weaknesses=weaknesses or [],
        )
        self.analysis.competitors.append(comp)
        return comp

    def add_switch(self, from_product: str, to_product: str,
                   user_count: int = 0, reason: str = "") -> SwitchEvidence:
        evidence = SwitchEvidence(
            from_product=from_product, to_product=to_product,
            user_count=user_count, switch_reason=reason,
        )
        self.analysis.switch_evidence.append(evidence)
        return evidence

    def set_force_comparison(self, competitor_name: str,
                             push_advantage: str = "",
                             pull_advantage: str = "",
                             anxiety_disadvantage: str = "",
                             inertia_disadvantage: str = "") -> None:
        for comp in self.analysis.competitors:
            if comp.name == competitor_name:
                comp.force_comparison = ForceComparison(
                    competitor_name=competitor_name,
                    push_advantage=push_advantage,
                    pull_advantage=pull_advantage,
                    anxiety_disadvantage=anxiety_disadvantage,
                    inertia_disadvantage=inertia_disadvantage,
                )
                return
        raise ValueError(f"未找到竞争者: {competitor_name}")

    def add_insight(self, insight: str) -> None:
        self.analysis.insights.append(insight)

    def add_strategy(self, strategy: str) -> None:
        self.analysis.strategies.append(strategy)

    def auto_insights(self) -> List[str]:
        insights: List[str] = []
        a = self.analysis

        by_cat: Dict[str, List[Competitor]] = {}
        for c in a.competitors:
            by_cat.setdefault(c.category, []).append(c)

        if "indirect" in by_cat:
            names = [c.name for c in by_cat["indirect"]]
            insights.append(
                f"发现 {len(names)} 个间接竞品（{', '.join(names)}），"
                "说明用户的 Job 可以被不同品类的产品满足，竞争范围比预期更广。"
            )

        if "non_consumption" in by_cat:
            insights.append(
                "存在非消费方案，说明部分用户选择忍受现状或自行解决。"
                "这些用户是潜在增长来源，需要降低采用门槛。"
            )

        if a.switch_evidence:
            inbound = [e for e in a.switch_evidence if e.to_product == a.product_name]
            outbound = [e for e in a.switch_evidence if e.from_product == a.product_name]
            if inbound:
                total_in = sum(e.user_count for e in inbound)
                insights.append(f"有 {total_in} 位用户从其他方案切换到 {a.product_name}。")
            if outbound:
                total_out = sum(e.user_count for e in outbound)
                insights.append(f"有 {total_out} 位用户从 {a.product_name} 切换到其他方案，需要关注流失原因。")

        self.analysis.insights.extend(insights)
        return insights

    def render_markdown(self) -> str:
        a = self.analysis
        lines = [f"# JTBD 竞争分析 — {a.product_name}\n"]

        if a.target_job:
            lines.append(f"**目标 Job:** {a.target_job}\n")

        for cat in COMPETITOR_CATEGORIES:
            comps = [c for c in a.competitors if c.category == cat]
            if not comps:
                continue
            lines.append(f"## {CATEGORY_LABELS[cat]}\n")
            lines.append(f"*{CATEGORY_DESCRIPTIONS[cat]}*\n")
            for c in comps:
                lines.append(f"### {c.name}\n")
                if c.description:
                    lines.append(f"{c.description}\n")
                if c.strengths:
                    lines.append("**优势:**")
                    for s in c.strengths:
                        lines.append(f"- {s}")
                if c.weaknesses:
                    lines.append("**劣势:**")
                    for w in c.weaknesses:
                        lines.append(f"- {w}")

                fc = c.force_comparison
                if fc and any([fc.push_advantage, fc.pull_advantage, fc.anxiety_disadvantage, fc.inertia_disadvantage]):
                    lines.append(f"\n**四力对比（vs {c.name}）:**")
                    if fc.push_advantage:
                        lines.append(f"- 推力优势: {fc.push_advantage}")
                    if fc.pull_advantage:
                        lines.append(f"- 拉力优势: {fc.pull_advantage}")
                    if fc.anxiety_disadvantage:
                        lines.append(f"- 焦虑劣势: {fc.anxiety_disadvantage}")
                    if fc.inertia_disadvantage:
                        lines.append(f"- 惯性劣势: {fc.inertia_disadvantage}")
                lines.append("")

        if a.switch_evidence:
            lines.append("## 切换证据\n")
            for e in a.switch_evidence:
                count = f"（{e.user_count}人）" if e.user_count else ""
                lines.append(f"- {e.from_product} → {e.to_product} {count}")
                if e.switch_reason:
                    lines.append(f"  - 原因: {e.switch_reason}")
            lines.append("")

        if a.insights:
            lines.append("## 竞争洞察\n")
            for ins in a.insights:
                lines.append(f"- {ins}")
            lines.append("")

        if a.strategies:
            lines.append("## 竞争策略建议\n")
            for i, s in enumerate(a.strategies, 1):
                lines.append(f"{i}. {s}")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        a = self.analysis
        return {
            "product": a.product_name,
            "target_job": a.target_job,
            "competitors": [
                {"name": c.name, "category": c.category,
                 "strengths": c.strengths, "weaknesses": c.weaknesses}
                for c in a.competitors
            ],
            "switch_evidence": [
                {"from": e.from_product, "to": e.to_product,
                 "count": e.user_count, "reason": e.switch_reason}
                for e in a.switch_evidence
            ],
            "insights": a.insights,
            "strategies": a.strategies,
        }
