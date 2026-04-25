"""JTBD 分析引擎

提供完整的 JTBD 分析流程，包括多格式 JTBD 描述生成、进步系统分析、
竞争格局梳理和综合报告输出。

v3.0 新增:
- 多格式JTBD描述支持: Klement格式、Desired Outcome Statement、Job Story、传统格式
- statement_format字段区分不同描述格式
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import (
    AnalysisConfig,
    FORCE_LABELS,
    FORCE_CATEGORIES,
    JTBD_STATEMENT_VERBS,
)
from .templates import (
    COMPETITIVE_ANALYSIS_TEMPLATE,
    INNOVATION_CHECKLIST,
    REPORT_TEMPLATE,
)
from .utils import load_knowledge, search_knowledge


STATEMENT_FORMATS = ("klement", "outcome", "job_story", "traditional")

STATEMENT_FORMAT_LABELS: Dict[str, str] = {
    "klement": "Klement格式 — [动作短语] + [挣扎]，这样我就能 + [期望]",
    "outcome": "Desired Outcome — [Direction] + [Metric] + [Object] + [Clarifier]",
    "job_story": "Job Story — When [情境], I want to [动机], so I can [期望结果]",
    "traditional": "传统格式 — As a [角色], I want to [动作], so that [结果]",
}


@dataclass
class JTBDStatement:
    """一条 JTBD 描述（支持多格式）"""

    verb: str
    struggle: str
    desired_outcome: str
    statement_format: str = "klement"
    situation: str = ""
    role: str = ""
    direction: str = ""
    metric: str = ""
    object_of_control: str = ""
    clarifier: str = ""

    def render(self) -> str:
        if self.statement_format == "outcome" and self.direction:
            parts = [self.direction.capitalize(), self.metric, self.object_of_control]
            if self.clarifier:
                parts.append(self.clarifier)
            return " ".join(p for p in parts if p)

        if self.statement_format == "job_story" and self.situation:
            return f"When {self.situation}, I want to {self.struggle}, so I can {self.desired_outcome}"

        if self.statement_format == "traditional" and self.role:
            return f"As a {self.role}, I want to {self.struggle}, so that {self.desired_outcome}"

        return f"{self.verb} {self.struggle}，这样我就能 {self.desired_outcome}"

    def render_zh(self) -> str:
        if self.statement_format == "outcome" and self.direction:
            dir_zh = {"minimize": "最小化", "maximize": "最大化",
                      "increase": "增加", "reduce": "减少"}.get(self.direction.lower(), self.direction)
            obj = self.object_of_control or self.struggle
            return f"{dir_zh} {obj}"

        if self.statement_format == "job_story" and self.situation:
            return f"当{self.situation}时，我想要{self.struggle}，这样我就能{self.desired_outcome}"

        if self.statement_format == "traditional" and self.role:
            return f"作为{self.role}，我想要{self.struggle}，从而{self.desired_outcome}"

        return f"{self.verb} {self.struggle}，这样我就能 {self.desired_outcome}"

    def validate(self) -> List[str]:
        issues: List[str] = []

        if self.statement_format == "klement":
            if self.verb.lower() not in [v.lower() for v in JTBD_STATEMENT_VERBS]:
                issues.append(
                    f"动作短语 '{self.verb}' 不在推荐列表中，"
                    f"建议使用: {', '.join(JTBD_STATEMENT_VERBS)}"
                )

        if self.statement_format == "outcome":
            if not self.direction:
                issues.append("Desired Outcome格式需要指定direction (minimize/maximize/increase/reduce)")
            if not self.object_of_control:
                issues.append("Desired Outcome格式需要指定object_of_control")

        if self.statement_format == "job_story":
            if not self.situation:
                issues.append("Job Story格式需要指定situation (When...)")

        if self.statement_format == "traditional":
            if not self.role:
                issues.append("传统格式需要指定role (As a...)")

        if len(self.struggle) < 5:
            issues.append("挣扎描述过于简短，建议更具体地描述客户面临的困境")
        if len(self.desired_outcome) < 5:
            issues.append("期望结果过于简短，建议更具体地描述客户想要达到的状态")
        return issues


@dataclass
class ForceEntry:
    """单条力量分析条目"""

    force_type: str
    description: str
    intensity: int = 3
    evidence: str = ""

    def validate(self) -> List[str]:
        issues: List[str] = []
        if self.force_type not in FORCE_LABELS:
            issues.append(f"未知力量类型: {self.force_type}")
        if not 1 <= self.intensity <= 5:
            issues.append(f"强度 {self.intensity} 超出范围，应在 1-5 之间")
        return issues


@dataclass
class CompetitorEntry:
    """竞争者条目"""

    name: str
    category: str
    why_chosen: str = ""
    why_left: str = ""
    limitations: str = ""


@dataclass
class JTBDAnalysis:
    """完整的 JTBD 分析结果"""

    project_name: str
    overview: str = ""
    statements: List[JTBDStatement] = field(default_factory=list)
    forces: List[ForceEntry] = field(default_factory=list)
    competitors: List[CompetitorEntry] = field(default_factory=list)
    innovation_opportunities: List[str] = field(default_factory=list)
    action_items: List[str] = field(default_factory=list)

    def get_forces_by_type(self, force_type: str) -> List[ForceEntry]:
        return [f for f in self.forces if f.force_type == force_type]

    def get_forces_by_category(self, category: str) -> List[ForceEntry]:
        return [
            f for f in self.forces
            if FORCE_CATEGORIES.get(f.force_type) == category
        ]

    def get_demand_balance(self) -> Dict[str, int]:
        generating = self.get_forces_by_category("demand_generating")
        reducing = self.get_forces_by_category("demand_reducing")
        gen_score = sum(f.intensity for f in generating) if generating else 0
        red_score = sum(f.intensity for f in reducing) if reducing else 0
        return {
            "generating_total": gen_score,
            "reducing_total": red_score,
            "net_demand": gen_score - red_score,
        }

    def get_statements_by_format(self, fmt: str) -> List[JTBDStatement]:
        return [s for s in self.statements if s.statement_format == fmt]


class JTBDAnalyzer:
    """JTBD 分析器

    提供创建、管理和输出 JTBD 分析的完整 API。

    用法示例::

        analyzer = JTBDAnalyzer("旅行预订平台")

        # Klement格式 (默认)
        analyzer.add_statement("Help me", "在出差时快速找到合适的住处", "专注于工作而不是为住宿烦恼")

        # Desired Outcome Statement格式
        analyzer.add_outcome_statement(
            direction="minimize", metric="the time it takes to",
            object_of_control="find a hotel meeting company standards",
            clarifier="when booking for business trips",
        )

        # Job Story格式
        analyzer.add_job_story(
            situation="出差日期确定后",
            want="快速找到符合公司差标的酒店",
            outcome="不浪费时间在住宿问题上",
        )

        # 传统格式
        analyzer.add_traditional_statement(
            role="商旅经理", want="一键预订合规酒店", outcome="提高差旅管理效率",
        )

        analyzer.add_force("push", "频繁出差导致每次都要花大量时间找酒店", intensity=4)
        report = analyzer.generate_report()
        print(report)
    """

    def __init__(self, project_name: str, config: Optional[AnalysisConfig] = None):
        self.config = config or AnalysisConfig()
        self.config.validate()
        self.analysis = JTBDAnalysis(project_name=project_name)

    def set_overview(self, overview: str) -> None:
        self.analysis.overview = overview

    def add_statement(
        self, verb: str, struggle: str, desired_outcome: str
    ) -> JTBDStatement:
        stmt = JTBDStatement(
            verb=verb, struggle=struggle, desired_outcome=desired_outcome,
            statement_format="klement",
        )
        issues = stmt.validate()
        if issues:
            import warnings
            for issue in issues:
                warnings.warn(issue)
        self.analysis.statements.append(stmt)
        return stmt

    def add_outcome_statement(
        self, direction: str, metric: str = "",
        object_of_control: str = "", clarifier: str = "",
    ) -> JTBDStatement:
        stmt = JTBDStatement(
            verb="", struggle=object_of_control,
            desired_outcome=clarifier or object_of_control,
            statement_format="outcome",
            direction=direction, metric=metric,
            object_of_control=object_of_control, clarifier=clarifier,
        )
        issues = stmt.validate()
        if issues:
            import warnings
            for issue in issues:
                warnings.warn(issue)
        self.analysis.statements.append(stmt)
        return stmt

    def add_job_story(
        self, situation: str, want: str, outcome: str,
    ) -> JTBDStatement:
        stmt = JTBDStatement(
            verb="", struggle=want, desired_outcome=outcome,
            statement_format="job_story", situation=situation,
        )
        issues = stmt.validate()
        if issues:
            import warnings
            for issue in issues:
                warnings.warn(issue)
        self.analysis.statements.append(stmt)
        return stmt

    def add_traditional_statement(
        self, role: str, want: str, outcome: str,
    ) -> JTBDStatement:
        stmt = JTBDStatement(
            verb="", struggle=want, desired_outcome=outcome,
            statement_format="traditional", role=role,
        )
        issues = stmt.validate()
        if issues:
            import warnings
            for issue in issues:
                warnings.warn(issue)
        self.analysis.statements.append(stmt)
        return stmt

    def add_force(
        self,
        force_type: str,
        description: str,
        intensity: int = 3,
        evidence: str = "",
    ) -> ForceEntry:
        entry = ForceEntry(
            force_type=force_type,
            description=description,
            intensity=intensity,
            evidence=evidence,
        )
        issues = entry.validate()
        if issues:
            raise ValueError("; ".join(issues))
        self.analysis.forces.append(entry)
        return entry

    def add_competitor(
        self,
        name: str,
        category: str = "direct_competitors",
        why_chosen: str = "",
        why_left: str = "",
        limitations: str = "",
    ) -> CompetitorEntry:
        if category not in COMPETITIVE_ANALYSIS_TEMPLATE:
            valid = ", ".join(COMPETITIVE_ANALYSIS_TEMPLATE.keys())
            raise ValueError(f"未知竞争者类别: {category}，可选: {valid}")
        entry = CompetitorEntry(
            name=name,
            category=category,
            why_chosen=why_chosen,
            why_left=why_left,
            limitations=limitations,
        )
        self.analysis.competitors.append(entry)
        return entry

    def add_innovation_opportunity(self, description: str) -> None:
        self.analysis.innovation_opportunities.append(description)

    def add_action_item(self, action: str) -> None:
        self.analysis.action_items.append(action)

    def get_demand_balance(self) -> Dict[str, int]:
        return self.analysis.get_demand_balance()

    def run_innovation_checklist(self) -> Dict[str, bool]:
        return {item: False for item in INNOVATION_CHECKLIST}

    def get_reference(self, topic: str) -> str:
        return load_knowledge(topic)

    def search_reference(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)

    def generate_report(self) -> str:
        a = self.analysis

        jtbd_lines = []
        for i, stmt in enumerate(a.statements, 1):
            fmt_label = STATEMENT_FORMAT_LABELS.get(stmt.statement_format, "")
            format_tag = f" [{fmt_label.split('—')[0].strip()}]" if stmt.statement_format != "klement" else ""
            jtbd_lines.append(f"{i}. {stmt.render()}{format_tag}")
            if stmt.statement_format != "klement":
                zh = stmt.render_zh()
                if zh != stmt.render():
                    jtbd_lines.append(f"   中文: {zh}")
        jtbd_text = "\n".join(jtbd_lines) if jtbd_lines else "（尚未定义）"

        def _render_force(force_type: str) -> str:
            entries = a.get_forces_by_type(force_type)
            if not entries:
                return "（尚未分析）"
            lines = []
            for e in entries:
                line = f"- **[强度 {e.intensity}/5]** {e.description}"
                if e.evidence:
                    line += f"\n  - 证据: {e.evidence}"
                lines.append(line)
            return "\n".join(lines)

        comp_lines = []
        for c in a.competitors:
            label = COMPETITIVE_ANALYSIS_TEMPLATE.get(c.category, {}).get("label", c.category)
            parts = [f"- **{c.name}** ({label})"]
            if c.why_chosen:
                parts.append(f"  - 选择原因: {c.why_chosen}")
            if c.why_left:
                parts.append(f"  - 离开原因: {c.why_left}")
            if c.limitations:
                parts.append(f"  - 局限性: {c.limitations}")
            comp_lines.append("\n".join(parts))
        comp_text = "\n".join(comp_lines) if comp_lines else "（尚未分析）"

        innov_lines = [f"- {opp}" for opp in a.innovation_opportunities]
        innov_text = "\n".join(innov_lines) if innov_lines else "（尚未发现）"

        action_lines = [f"{i}. {act}" for i, act in enumerate(a.action_items, 1)]
        action_text = "\n".join(action_lines) if action_lines else "（尚未制定）"

        return REPORT_TEMPLATE.format(
            title=f"JTBD 分析报告 — {a.project_name}",
            overview=a.overview or "（尚未填写）",
            jtbd_statement=jtbd_text,
            push_analysis=_render_force("push"),
            pull_analysis=_render_force("pull"),
            anxiety_analysis=_render_force("anxiety"),
            inertia_analysis=_render_force("inertia"),
            competition_analysis=comp_text,
            innovation_opportunities=innov_text,
            action_items=action_text,
        )

    def export_json(self) -> Dict:
        a = self.analysis
        return {
            "project_name": a.project_name,
            "overview": a.overview,
            "statements": [
                {
                    "verb": s.verb, "struggle": s.struggle,
                    "desired_outcome": s.desired_outcome,
                    "format": s.statement_format,
                    "rendered": s.render(),
                    "rendered_zh": s.render_zh(),
                    "situation": s.situation,
                    "role": s.role,
                    "direction": s.direction,
                    "metric": s.metric,
                    "object_of_control": s.object_of_control,
                    "clarifier": s.clarifier,
                }
                for s in a.statements
            ],
            "forces": [
                {
                    "type": f.force_type,
                    "description": f.description,
                    "intensity": f.intensity,
                    "evidence": f.evidence,
                }
                for f in a.forces
            ],
            "competitors": [
                {
                    "name": c.name,
                    "category": c.category,
                    "why_chosen": c.why_chosen,
                    "why_left": c.why_left,
                    "limitations": c.limitations,
                }
                for c in a.competitors
            ],
            "demand_balance": a.get_demand_balance(),
            "innovation_opportunities": a.innovation_opportunities,
            "action_items": a.action_items,
        }
