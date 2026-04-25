"""JTBD Desired Outcome Statement 生成与管理模块

基于 Ulwick ODI 方法论的 Desired Outcome Statement 工具。

标准格式: Direction + Performance Metric + Object of Control + Contextual Clarifier

例如:
- Minimize the time it takes to find a suitable hotel when traveling for business
- Minimize the likelihood of booking a hotel that doesn't match its photos

Direction (方向): Minimize / Maximize / Increase / Reduce
Performance Metric (绩效指标): the time, the likelihood, the number, the effort
Object of Control (控制对象): 客户试图控制的事物
Contextual Clarifier (情境限定): 发生的具体情境
"""

from dataclasses import dataclass, field
from typing import Dict, List


OUTCOME_DIRECTIONS = (
    "minimize",
    "maximize",
    "increase",
    "reduce",
)

DIRECTION_LABELS: Dict[str, str] = {
    "minimize": "最小化 (Minimize)",
    "maximize": "最大化 (Maximize)",
    "increase": "增加 (Increase)",
    "reduce": "减少 (Reduce)",
}

COMMON_METRICS = (
    "the time it takes to",
    "the likelihood of",
    "the number of",
    "the effort required to",
    "the cost of",
    "the frequency of",
    "the degree to which",
    "the ability to",
    "the accuracy of",
    "the completeness of",
    "the reliability of",
    "the risk of",
)

METRIC_LABELS: Dict[str, str] = {
    "the time it takes to": "所需时间",
    "the likelihood of": "可能性",
    "the number of": "数量",
    "the effort required to": "所需精力",
    "the cost of": "成本",
    "the frequency of": "频率",
    "the degree to which": "程度",
    "the ability to": "能力",
    "the accuracy of": "准确度",
    "the completeness of": "完整度",
    "the reliability of": "可靠性",
    "the risk of": "风险",
}

NEED_TYPES = (
    "core_functional",
    "related_job",
    "emotional",
    "social",
    "consumption_chain",
    "financial",
)

NEED_TYPE_LABELS: Dict[str, str] = {
    "core_functional": "核心功能需求",
    "related_job": "相关Job需求",
    "emotional": "情感需求",
    "social": "社会需求",
    "consumption_chain": "消费链需求",
    "financial": "财务需求",
}


@dataclass
class DesiredOutcome:
    """一条 Desired Outcome Statement"""
    direction: str
    metric: str
    object_of_control: str
    clarifier: str = ""
    need_type: str = "core_functional"
    job_map_stage: str = ""
    importance: int = 5
    satisfaction: int = 5

    @property
    def statement(self) -> str:
        parts = [self.direction.capitalize(), self.metric, self.object_of_control]
        if self.clarifier:
            parts.append(self.clarifier)
        return " ".join(parts)

    @property
    def statement_zh(self) -> str:
        dir_zh = {"minimize": "最小化", "maximize": "最大化",
                  "increase": "增加", "reduce": "减少"}.get(self.direction, self.direction)
        return f"{dir_zh} {self.object_of_control} 的 {METRIC_LABELS.get(self.metric, self.metric)}"

    @property
    def opportunity(self) -> float:
        return self.importance + max(self.importance - self.satisfaction, 0)

    def validate(self) -> List[str]:
        issues: List[str] = []
        if self.direction not in OUTCOME_DIRECTIONS:
            issues.append(
                f"方向 '{self.direction}' 不在推荐列表中，"
                f"建议使用: {', '.join(OUTCOME_DIRECTIONS)}"
            )
        if len(self.object_of_control) < 3:
            issues.append("控制对象描述过于简短")
        if self.importance < 1 or self.importance > 10:
            issues.append(f"重要性 {self.importance} 超出范围 1-10")
        if self.satisfaction < 1 or self.satisfaction > 10:
            issues.append(f"满意度 {self.satisfaction} 超出范围 1-10")
        return issues


@dataclass
class OutcomeSet:
    """一组 Desired Outcome Statements"""
    job_statement: str
    outcomes: List[DesiredOutcome] = field(default_factory=list)

    def by_type(self, need_type: str) -> List[DesiredOutcome]:
        return [o for o in self.outcomes if o.need_type == need_type]

    def by_stage(self, stage: str) -> List[DesiredOutcome]:
        return [o for o in self.outcomes if o.job_map_stage == stage]

    def get_underserved(self, threshold: float = 12.0) -> List[DesiredOutcome]:
        return sorted(
            [o for o in self.outcomes if o.opportunity >= threshold],
            key=lambda x: x.opportunity, reverse=True,
        )

    def get_overserved(self, threshold: float = 6.0) -> List[DesiredOutcome]:
        return [o for o in self.outcomes if o.opportunity <= threshold and o.importance <= 5]

    def get_opportunity_landscape(self) -> Dict[str, List[DesiredOutcome]]:
        underserved = [o for o in self.outcomes if o.opportunity >= 12]
        appropriately_served = [o for o in self.outcomes if 8 <= o.opportunity < 12]
        overserved = [o for o in self.outcomes if o.opportunity < 8]
        return {
            "underserved": sorted(underserved, key=lambda x: x.opportunity, reverse=True),
            "appropriately_served": sorted(appropriately_served, key=lambda x: x.opportunity, reverse=True),
            "overserved": sorted(overserved, key=lambda x: x.opportunity, reverse=True),
        }


class OutcomeBuilder:
    """Desired Outcome Statement 构建器

    用法示例::

        builder = OutcomeBuilder("管理商务出差的住宿安排")
        builder.add_outcome(
            direction="minimize",
            metric="the time it takes to",
            object_of_control="find a hotel that meets company travel standards",
            clarifier="when booking for business trips",
            importance=9, satisfaction=3,
            job_map_stage="locate",
        )
        builder.add_outcome(
            direction="minimize",
            metric="the likelihood of",
            object_of_control="booking a hotel that doesn't match its photos",
            importance=8, satisfaction=4,
            need_type="emotional",
        )
        outcome_set = builder.build()
        print(OutcomeBuilder.render_markdown(outcome_set))
    """

    def __init__(self, job_statement: str):
        self._job = job_statement
        self._outcomes: List[DesiredOutcome] = []

    def add_outcome(self, direction: str, metric: str,
                    object_of_control: str, clarifier: str = "",
                    need_type: str = "core_functional",
                    job_map_stage: str = "",
                    importance: int = 5,
                    satisfaction: int = 5) -> "OutcomeBuilder":
        outcome = DesiredOutcome(
            direction=direction, metric=metric,
            object_of_control=object_of_control, clarifier=clarifier,
            need_type=need_type, job_map_stage=job_map_stage,
            importance=importance, satisfaction=satisfaction,
        )
        issues = outcome.validate()
        if issues:
            import warnings
            for issue in issues:
                warnings.warn(issue)
        self._outcomes.append(outcome)
        return self

    def add_outcome_simple(self, direction: str,
                           description_zh: str,
                           importance: int = 5,
                           satisfaction: int = 5,
                           need_type: str = "core_functional",
                           job_map_stage: str = "") -> "OutcomeBuilder":
        outcome = DesiredOutcome(
            direction=direction,
            metric="",
            object_of_control=description_zh,
            need_type=need_type,
            job_map_stage=job_map_stage,
            importance=importance,
            satisfaction=satisfaction,
        )
        self._outcomes.append(outcome)
        return self

    def build(self) -> OutcomeSet:
        return OutcomeSet(
            job_statement=self._job,
            outcomes=list(self._outcomes),
        )

    @staticmethod
    def render_markdown(outcome_set: OutcomeSet) -> str:
        lines = [f"# Desired Outcome Statements\n"]
        lines.append(f"**Job:** {outcome_set.job_statement}\n")

        landscape = outcome_set.get_opportunity_landscape()

        if landscape["underserved"]:
            lines.append(f"## 未被充分满足的需求 (Underserved) — {len(landscape['underserved'])}条\n")
            lines.append("*机会分≥12，优先创新方向*\n")
            lines.append("| # | 需求 | 类型 | 重要性 | 满意度 | 机会分 |")
            lines.append("|---|------|------|--------|--------|--------|")
            for i, o in enumerate(landscape["underserved"], 1):
                type_label = NEED_TYPE_LABELS.get(o.need_type, o.need_type)
                desc = o.statement if o.metric else o.object_of_control
                lines.append(
                    f"| {i} | {desc} | {type_label} "
                    f"| {o.importance} | {o.satisfaction} | {o.opportunity:.1f} |"
                )
            lines.append("")

        if landscape["appropriately_served"]:
            lines.append(f"## 基本满足的需求 (Appropriately Served) — {len(landscape['appropriately_served'])}条\n")
            lines.append("| # | 需求 | 类型 | 重要性 | 满意度 | 机会分 |")
            lines.append("|---|------|------|--------|--------|--------|")
            for i, o in enumerate(landscape["appropriately_served"], 1):
                type_label = NEED_TYPE_LABELS.get(o.need_type, o.need_type)
                desc = o.statement if o.metric else o.object_of_control
                lines.append(
                    f"| {i} | {desc} | {type_label} "
                    f"| {o.importance} | {o.satisfaction} | {o.opportunity:.1f} |"
                )
            lines.append("")

        if landscape["overserved"]:
            lines.append(f"## 过度满足的需求 (Overserved) — {len(landscape['overserved'])}条\n")
            lines.append("*可考虑简化以降低成本（颠覆式创新机会）*\n")
            lines.append("| # | 需求 | 类型 | 重要性 | 满意度 | 机会分 |")
            lines.append("|---|------|------|--------|--------|--------|")
            for i, o in enumerate(landscape["overserved"], 1):
                type_label = NEED_TYPE_LABELS.get(o.need_type, o.need_type)
                desc = o.statement if o.metric else o.object_of_control
                lines.append(
                    f"| {i} | {desc} | {type_label} "
                    f"| {o.importance} | {o.satisfaction} | {o.opportunity:.1f} |"
                )
            lines.append("")

        by_type_counts: Dict[str, int] = {}
        for o in outcome_set.outcomes:
            by_type_counts[o.need_type] = by_type_counts.get(o.need_type, 0) + 1
        if by_type_counts:
            lines.append("## 需求类型分布\n")
            for nt in NEED_TYPES:
                if nt in by_type_counts:
                    lines.append(f"- {NEED_TYPE_LABELS[nt]}: {by_type_counts[nt]}条")
            lines.append("")

        total = len(outcome_set.outcomes)
        underserved_count = len(landscape["underserved"])
        if total > 0:
            lines.append("## 机会概览\n")
            lines.append(f"- 总需求数: {total}")
            lines.append(f"- 未充分满足: {underserved_count} ({underserved_count*100//total}%)")
            lines.append(f"- 基本满足: {len(landscape['appropriately_served'])}")
            lines.append(f"- 过度满足: {len(landscape['overserved'])}")

        return "\n".join(lines)

    @staticmethod
    def render_json(outcome_set: OutcomeSet) -> Dict:
        landscape = outcome_set.get_opportunity_landscape()
        return {
            "job_statement": outcome_set.job_statement,
            "total_outcomes": len(outcome_set.outcomes),
            "landscape": {
                category: [
                    {
                        "statement": o.statement if o.metric else o.object_of_control,
                        "direction": o.direction,
                        "need_type": o.need_type,
                        "job_map_stage": o.job_map_stage,
                        "importance": o.importance,
                        "satisfaction": o.satisfaction,
                        "opportunity": o.opportunity,
                    }
                    for o in outcomes
                ]
                for category, outcomes in landscape.items()
            },
        }
