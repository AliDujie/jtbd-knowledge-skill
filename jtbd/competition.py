"""JTBD 竞争分析模块

对应 SKILL.md 执行能力五：JTBD 竞争分析。
识别真正的竞争对手、验证竞争关系、进行四力对比。

v3.0 新增:
- Outcome-Based竞争评估 (按Desired Outcome对比竞品满意度)
- 颠覆诊断 (Disruption Diagnostic)
- 竞争力三要素 (Right to Win)
- Jobs视角竞争边界重定义
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import FORCE_LABELS  # noqa: F401 - available for external import


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

RIGHT_TO_WIN_FACTORS = ("capability_fit", "flexibility", "market_perception")

RIGHT_TO_WIN_LABELS: Dict[str, str] = {
    "capability_fit": "能力匹配度 — 满足核心Outcome的技术/资源能力",
    "flexibility": "灵活性 — 快速响应需求变化的组织能力",
    "market_perception": "市场认知 — 用户心智中的品牌定位和信任度",
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
class OutcomeComparison:
    """基于Desired Outcome的竞品对比"""
    outcome_description: str
    our_satisfaction: int = 5
    competitor_name: str = ""
    competitor_satisfaction: int = 5

    @property
    def gap(self) -> int:
        return self.our_satisfaction - self.competitor_satisfaction


@dataclass
class DisruptionDiagnostic:
    """颠覆诊断"""
    disruptor_name: str
    disruptor_advantages: List[str] = field(default_factory=list)
    our_advantages: List[str] = field(default_factory=list)
    adoption_barriers: List[str] = field(default_factory=list)
    threat_level: str = "medium"
    response_strategy: str = ""


@dataclass
class Competitor:
    """竞争者"""
    name: str
    category: str
    description: str = ""
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    force_comparison: Optional[ForceComparison] = None

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
    outcome_comparisons: List[OutcomeComparison] = field(default_factory=list)
    disruption_diagnostics: List[DisruptionDiagnostic] = field(default_factory=list)
    right_to_win: Dict[str, int] = field(default_factory=dict)
    insights: List[str] = field(default_factory=list)
    strategies: List[str] = field(default_factory=list)


class CompetitionAnalyzer:
    """竞争分析器

    用法示例::

        analyzer = CompetitionAnalyzer("旅行预订平台")
        analyzer.set_target_job("在出差时快速找到合适的住处")
        analyzer.add_competitor("携程", "direct", strengths=["酒店数量多"], weaknesses=["界面复杂"])
        analyzer.add_competitor("朋友推荐", "non_consumption", strengths=["信任度高"], weaknesses=["选择有限"])

        # Outcome-Based竞争评估
        analyzer.add_outcome_comparison("快速找到酒店", our_sat=7, competitor="携程", comp_sat=5)
        analyzer.add_outcome_comparison("价格透明度", our_sat=6, competitor="携程", comp_sat=4)

        # 颠覆诊断
        analyzer.add_disruption("AI行程助手",
            disruptor_advantages=["自然语言交互", "个性化推荐"],
            our_advantages=["交易闭环", "售后保障"],
            adoption_barriers=["信任度低", "复杂行程处理差"])

        # 竞争力三要素
        analyzer.set_right_to_win(capability_fit=4, flexibility=3, market_perception=4)

        print(analyzer.render_markdown())
    """

    def __init__(self, product_name: str):
        self.analysis = CompetitiveAnalysis(product_name=product_name)

    def set_target_job(self, job: str) -> None:
        self.analysis.target_job = job

    def add_competitor(self, name: str, category: str = "direct",
                       description: str = "",
                       strengths: Optional[List[str]] = None,
                       weaknesses: Optional[List[str]] = None) -> Competitor:
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

    def add_outcome_comparison(self, outcome: str, our_sat: int,
                               competitor: str, comp_sat: int) -> OutcomeComparison:
        if not 1 <= our_sat <= 10:
            raise ValueError(f"我方满意度 {our_sat} 超出范围 1-10")
        if not 1 <= comp_sat <= 10:
            raise ValueError(f"竞品满意度 {comp_sat} 超出范围 1-10")
        comparison = OutcomeComparison(
            outcome_description=outcome,
            our_satisfaction=our_sat,
            competitor_name=competitor,
            competitor_satisfaction=comp_sat,
        )
        self.analysis.outcome_comparisons.append(comparison)
        return comparison

    def add_disruption(self, disruptor_name: str,
                       disruptor_advantages: Optional[List[str]] = None,
                       our_advantages: Optional[List[str]] = None,
                       adoption_barriers: Optional[List[str]] = None,
                       threat_level: str = "medium",
                       response_strategy: str = "") -> DisruptionDiagnostic:
        if threat_level not in ("low", "medium", "high", "critical"):
            raise ValueError(f"未知威胁等级: {threat_level}，可选: low/medium/high/critical")
        diag = DisruptionDiagnostic(
            disruptor_name=disruptor_name,
            disruptor_advantages=disruptor_advantages or [],
            our_advantages=our_advantages or [],
            adoption_barriers=adoption_barriers or [],
            threat_level=threat_level,
            response_strategy=response_strategy,
        )
        self.analysis.disruption_diagnostics.append(diag)
        return diag

    def set_right_to_win(self, capability_fit: int = 3,
                         flexibility: int = 3,
                         market_perception: int = 3) -> None:
        for name, val in [("capability_fit", capability_fit),
                          ("flexibility", flexibility),
                          ("market_perception", market_perception)]:
            if not 1 <= val <= 5:
                raise ValueError(f"{name} 分数 {val} 超出范围 1-5")
        self.analysis.right_to_win = {
            "capability_fit": capability_fit,
            "flexibility": flexibility,
            "market_perception": market_perception,
        }

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

        if a.outcome_comparisons:
            advantages = [oc for oc in a.outcome_comparisons if oc.gap > 0]
            disadvantages = [oc for oc in a.outcome_comparisons if oc.gap < 0]
            if advantages:
                insights.append(
                    f"在 {len(advantages)} 个Outcome上领先竞品，"
                    f"最大优势: 「{max(advantages, key=lambda x: x.gap).outcome_description}」。"
                )
            if disadvantages:
                insights.append(
                    f"在 {len(disadvantages)} 个Outcome上落后竞品，"
                    f"最大劣势: 「{min(disadvantages, key=lambda x: x.gap).outcome_description}」，"
                    "需优先改善。"
                )

        if a.disruption_diagnostics:
            critical = [d for d in a.disruption_diagnostics if d.threat_level == "critical"]
            if critical:
                names = [d.disruptor_name for d in critical]
                insights.append(f"发现 {len(critical)} 个严重颠覆威胁: {', '.join(names)}，需立即制定应对策略。")

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

        if a.outcome_comparisons:
            lines.append("## Outcome-Based 竞争对比\n")
            lines.append("| Outcome | 我方满意度 | 竞品 | 竞品满意度 | 差距 | 判断 |")
            lines.append("|---------|-----------|------|-----------|------|------|")
            for oc in sorted(a.outcome_comparisons, key=lambda x: x.gap):
                indicator = "领先" if oc.gap > 0 else ("持平" if oc.gap == 0 else "落后")
                lines.append(
                    f"| {oc.outcome_description} | {oc.our_satisfaction}/10 "
                    f"| {oc.competitor_name} | {oc.competitor_satisfaction}/10 "
                    f"| {oc.gap:+d} | {indicator} |"
                )
            lines.append("")

        if a.disruption_diagnostics:
            threat_icons = {"low": "🟢", "medium": "🟡", "high": "🟠", "critical": "🔴"}
            lines.append("## 颠覆诊断\n")
            for diag in a.disruption_diagnostics:
                icon = threat_icons.get(diag.threat_level, "🟡")
                lines.append(f"### {icon} {diag.disruptor_name} (威胁等级: {diag.threat_level})\n")
                if diag.disruptor_advantages:
                    lines.append("**颠覆者优势:**")
                    for adv in diag.disruptor_advantages:
                        lines.append(f"- {adv}")
                if diag.our_advantages:
                    lines.append("**我方优势:**")
                    for adv in diag.our_advantages:
                        lines.append(f"- {adv}")
                if diag.adoption_barriers:
                    lines.append("**颠覆者采用障碍:**")
                    for bar in diag.adoption_barriers:
                        lines.append(f"- {bar}")
                if diag.response_strategy:
                    lines.append(f"\n**应对策略:** {diag.response_strategy}")
                lines.append("")

        if a.right_to_win:
            lines.append("## 竞争力三要素 (Right to Win)\n")
            total = 0
            for factor in RIGHT_TO_WIN_FACTORS:
                score = a.right_to_win.get(factor, 0)
                total += score
                label = RIGHT_TO_WIN_LABELS.get(factor, factor)
                bar = "█" * score + "░" * (5 - score)
                lines.append(f"- **{label}:** {bar} {score}/5")
            lines.append(f"\n**综合竞争力:** {total}/15")
            if total >= 12:
                lines.append("*评估: 竞争地位强势，可进攻性扩张*")
            elif total >= 8:
                lines.append("*评估: 竞争地位中等，需重点补齐短板*")
            else:
                lines.append("*评估: 竞争地位弱势，需寻找差异化方向*")
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
            "outcome_comparisons": [
                {"outcome": oc.outcome_description,
                 "our_satisfaction": oc.our_satisfaction,
                 "competitor": oc.competitor_name,
                 "competitor_satisfaction": oc.competitor_satisfaction,
                 "gap": oc.gap}
                for oc in a.outcome_comparisons
            ],
            "disruption_diagnostics": [
                {"disruptor": d.disruptor_name,
                 "threat_level": d.threat_level,
                 "disruptor_advantages": d.disruptor_advantages,
                 "our_advantages": d.our_advantages,
                 "adoption_barriers": d.adoption_barriers,
                 "response_strategy": d.response_strategy}
                for d in a.disruption_diagnostics
            ],
            "right_to_win": a.right_to_win,
            "switch_evidence": [
                {"from": e.from_product, "to": e.to_product,
                 "count": e.user_count, "reason": e.switch_reason}
                for e in a.switch_evidence
            ],
            "insights": a.insights,
            "strategies": a.strategies,
        }
