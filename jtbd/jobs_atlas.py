"""JTBD Jobs Atlas 构建模块

基于 Wunker《Jobs to Be Done: A Roadmap》的 Jobs Atlas 框架。

Jobs Atlas 七维度:
Part 1 — 理解现状:
  1. Jobs: 客户试图完成的核心Job
  2. Job Drivers (ABC): Attitudes(社会性驱动) + Background(长期驱动) + Circumstances(短期驱动)
  3. Current Approaches & Pain Points: 当前方案及其痛点

Part 2 — 评估成功标准与障碍:
  4. Success Criteria: 客户如何定义"做好了"
  5. Obstacles: 采用和使用中的障碍

Part 3 — 衡量价值与竞争:
  6. Value: 解决方案为客户创造的价值（功能性、情感性、社会性）
  7. Competition: 从Job视角重新定义竞争边界
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


ATLAS_DIMENSIONS = (
    "jobs",
    "job_drivers",
    "current_approaches",
    "success_criteria",
    "obstacles",
    "value",
    "competition",
)

DIMENSION_LABELS: Dict[str, str] = {
    "jobs": "Jobs (核心Job)",
    "job_drivers": "Job Drivers (ABC驱动因素)",
    "current_approaches": "Current Approaches (当前方案与痛点)",
    "success_criteria": "Success Criteria (成功标准)",
    "obstacles": "Obstacles (障碍)",
    "value": "Value (价值)",
    "competition": "Competition (竞争)",
}

DIMENSION_PARTS: Dict[str, str] = {
    "jobs": "Part 1: 理解现状",
    "job_drivers": "Part 1: 理解现状",
    "current_approaches": "Part 1: 理解现状",
    "success_criteria": "Part 2: 评估成功与障碍",
    "obstacles": "Part 2: 评估成功与障碍",
    "value": "Part 3: 衡量价值与竞争",
    "competition": "Part 3: 衡量价值与竞争",
}

DRIVER_TYPES = ("attitudes", "background", "circumstances")

DRIVER_LABELS: Dict[str, str] = {
    "attitudes": "Attitudes (社会性驱动)",
    "background": "Background (长期驱动)",
    "circumstances": "Circumstances (短期驱动)",
}

DRIVER_DESCRIPTIONS: Dict[str, str] = {
    "attitudes": "社会性、文化性驱动因素，如价值观、社会期望、同辈压力",
    "background": "长期持续的驱动因素，如职业角色、家庭结构、经济状况",
    "circumstances": "短期、情境性的驱动因素，如时间压力、地理位置、特殊事件",
}

VALUE_TYPES = ("functional", "emotional", "social")

VALUE_LABELS: Dict[str, str] = {
    "functional": "功能性价值",
    "emotional": "情感性价值",
    "social": "社会性价值",
}


@dataclass
class JobDriver:
    """ABC Job Driver"""
    driver_type: str
    description: str
    influence_level: int = 3
    evidence: str = ""

    @property
    def label(self) -> str:
        return DRIVER_LABELS.get(self.driver_type, self.driver_type)


@dataclass
class CurrentApproach:
    """当前方案"""
    name: str
    description: str = ""
    pain_points: List[str] = field(default_factory=list)
    workarounds: List[str] = field(default_factory=list)


@dataclass
class SuccessCriterion:
    """成功标准"""
    criterion: str
    measurement: str = ""
    current_score: int = 0
    target_score: int = 10
    priority: int = 3


@dataclass
class ValueItem:
    """价值项"""
    value_type: str
    description: str
    magnitude: int = 3
    evidence: str = ""

    @property
    def label(self) -> str:
        return VALUE_LABELS.get(self.value_type, self.value_type)


@dataclass
class CompetitorView:
    """Job视角的竞争者"""
    name: str
    job_overlap: str = ""
    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    threat_level: int = 3


@dataclass
class JobsAtlas:
    """完整的 Jobs Atlas"""
    product_name: str
    core_job: str = ""
    related_jobs: List[str] = field(default_factory=list)
    drivers: List[JobDriver] = field(default_factory=list)
    current_approaches: List[CurrentApproach] = field(default_factory=list)
    success_criteria: List[SuccessCriterion] = field(default_factory=list)
    obstacles: List[str] = field(default_factory=list)
    values: List[ValueItem] = field(default_factory=list)
    competitors: List[CompetitorView] = field(default_factory=list)

    def completeness(self) -> Dict[str, bool]:
        return {
            "jobs": bool(self.core_job),
            "job_drivers": len(self.drivers) > 0,
            "current_approaches": len(self.current_approaches) > 0,
            "success_criteria": len(self.success_criteria) > 0,
            "obstacles": len(self.obstacles) > 0,
            "value": len(self.values) > 0,
            "competition": len(self.competitors) > 0,
        }

    def completeness_pct(self) -> int:
        checks = self.completeness()
        filled = sum(1 for v in checks.values() if v)
        return round(filled * 100 / len(checks))

    def drivers_by_type(self, driver_type: str) -> List[JobDriver]:
        return [d for d in self.drivers if d.driver_type == driver_type]

    def values_by_type(self, value_type: str) -> List[ValueItem]:
        return [v for v in self.values if v.value_type == value_type]


class JobsAtlasBuilder:
    """Jobs Atlas 引导式构建器

    用法示例::

        builder = JobsAtlasBuilder("旅行预订平台")

        # Part 1: 理解现状
        builder.set_core_job("管理商务出差的住宿安排")
        builder.add_related_job("规划出差行程")
        builder.add_driver("circumstances", "临时出差通知，时间紧迫", influence_level=5)
        builder.add_driver("background", "频繁出差的商旅人士", influence_level=4)
        builder.add_driver("attitudes", "公司要求控制差旅成本", influence_level=3)
        builder.add_current_approach("携程", pain_points=["界面复杂", "比价耗时"])

        # Part 2: 成功标准与障碍
        builder.add_success_criterion("预订时间不超过10分钟", priority=5)
        builder.add_obstacle("需要在多个平台比价")

        # Part 3: 价值与竞争
        builder.add_value("functional", "节省预订时间50%", magnitude=4)
        builder.add_value("emotional", "出差不再焦虑", magnitude=3)
        builder.add_competitor("携程", job_overlap="商旅住宿预订", threat_level=4)

        atlas = builder.build()
        print(JobsAtlasBuilder.render_markdown(atlas))
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._core_job = ""
        self._related_jobs: List[str] = []
        self._drivers: List[JobDriver] = []
        self._approaches: List[CurrentApproach] = []
        self._criteria: List[SuccessCriterion] = []
        self._obstacles: List[str] = []
        self._values: List[ValueItem] = []
        self._competitors: List[CompetitorView] = []

    def set_core_job(self, job: str) -> "JobsAtlasBuilder":
        self._core_job = job
        return self

    def add_related_job(self, job: str) -> "JobsAtlasBuilder":
        self._related_jobs.append(job)
        return self

    def add_driver(self, driver_type: str, description: str,
                   influence_level: int = 3,
                   evidence: str = "") -> "JobsAtlasBuilder":
        if driver_type not in DRIVER_TYPES:
            raise ValueError(f"未知驱动类型: {driver_type}，可选: {DRIVER_TYPES}")
        if not 1 <= influence_level <= 5:
            raise ValueError(f"影响力 {influence_level} 超出范围 1-5")
        self._drivers.append(JobDriver(
            driver_type=driver_type, description=description,
            influence_level=influence_level, evidence=evidence,
        ))
        return self

    def add_current_approach(self, name: str, description: str = "",
                             pain_points: Optional[List[str]] = None,
                             workarounds: Optional[List[str]] = None) -> "JobsAtlasBuilder":
        self._approaches.append(CurrentApproach(
            name=name, description=description,
            pain_points=pain_points or [], workarounds=workarounds or [],
        ))
        return self

    def add_success_criterion(self, criterion: str, measurement: str = "",
                              current_score: int = 0, target_score: int = 10,
                              priority: int = 3) -> "JobsAtlasBuilder":
        self._criteria.append(SuccessCriterion(
            criterion=criterion, measurement=measurement,
            current_score=current_score, target_score=target_score,
            priority=priority,
        ))
        return self

    def add_obstacle(self, description: str) -> "JobsAtlasBuilder":
        self._obstacles.append(description)
        return self

    def add_value(self, value_type: str, description: str,
                  magnitude: int = 3, evidence: str = "") -> "JobsAtlasBuilder":
        if value_type not in VALUE_TYPES:
            raise ValueError(f"未知价值类型: {value_type}，可选: {VALUE_TYPES}")
        if not 1 <= magnitude <= 5:
            raise ValueError(f"价值大小 {magnitude} 超出范围 1-5")
        self._values.append(ValueItem(
            value_type=value_type, description=description,
            magnitude=magnitude, evidence=evidence,
        ))
        return self

    def add_competitor(self, name: str, job_overlap: str = "",
                       strengths: Optional[List[str]] = None,
                       weaknesses: Optional[List[str]] = None,
                       threat_level: int = 3) -> "JobsAtlasBuilder":
        if not 1 <= threat_level <= 5:
            raise ValueError(f"威胁程度 {threat_level} 超出范围 1-5")
        self._competitors.append(CompetitorView(
            name=name, job_overlap=job_overlap,
            strengths=strengths or [], weaknesses=weaknesses or [],
            threat_level=threat_level,
        ))
        return self

    def build(self) -> JobsAtlas:
        return JobsAtlas(
            product_name=self._product,
            core_job=self._core_job,
            related_jobs=self._related_jobs,
            drivers=self._drivers,
            current_approaches=self._approaches,
            success_criteria=self._criteria,
            obstacles=self._obstacles,
            values=self._values,
            competitors=self._competitors,
        )

    @staticmethod
    def render_markdown(atlas: JobsAtlas) -> str:
        lines = [f"# Jobs Atlas — {atlas.product_name}\n"]

        comp = atlas.completeness()
        pct = atlas.completeness_pct()
        filled = sum(1 for v in comp.values() if v)
        total = len(comp)
        lines.append(f"**完成度:** {pct}% ({filled}/{total}维度)\n")

        unfilled = [DIMENSION_LABELS[k] for k, v in comp.items() if not v]
        if unfilled:
            lines.append("**待填充维度:**")
            for u in unfilled:
                lines.append(f"- [ ] {u}")
            lines.append("")

        lines.append("---\n")
        lines.append("## Part 1: 理解现状\n")

        lines.append("### 1. Jobs\n")
        if atlas.core_job:
            lines.append(f"**核心Job:** {atlas.core_job}\n")
        if atlas.related_jobs:
            lines.append("**相关Jobs:**")
            for j in atlas.related_jobs:
                lines.append(f"- {j}")
            lines.append("")

        lines.append("### 2. Job Drivers (ABC)\n")
        for dt in DRIVER_TYPES:
            drivers = atlas.drivers_by_type(dt)
            label = DRIVER_LABELS[dt]
            desc = DRIVER_DESCRIPTIONS[dt]
            lines.append(f"**{label}**")
            lines.append(f"*{desc}*\n")
            if drivers:
                for d in sorted(drivers, key=lambda x: x.influence_level, reverse=True):
                    influence_bar = "█" * d.influence_level + "░" * (5 - d.influence_level)
                    lines.append(f"- [{influence_bar}] {d.description}")
                    if d.evidence:
                        lines.append(f"  - 证据: {d.evidence}")
            else:
                lines.append("- *(待填充)*")
            lines.append("")

        lines.append("### 3. Current Approaches & Pain Points\n")
        if atlas.current_approaches:
            for approach in atlas.current_approaches:
                lines.append(f"**{approach.name}**")
                if approach.description:
                    lines.append(f"{approach.description}\n")
                if approach.pain_points:
                    lines.append("痛点:")
                    for p in approach.pain_points:
                        lines.append(f"- ❌ {p}")
                if approach.workarounds:
                    lines.append("替代方案/变通方法:")
                    for w in approach.workarounds:
                        lines.append(f"- 🔧 {w}")
                lines.append("")
        else:
            lines.append("*(待填充)*\n")

        lines.append("---\n")
        lines.append("## Part 2: 评估成功与障碍\n")

        lines.append("### 4. Success Criteria\n")
        if atlas.success_criteria:
            sorted_criteria = sorted(atlas.success_criteria, key=lambda x: x.priority, reverse=True)
            lines.append("| 优先级 | 成功标准 | 当前得分 | 目标得分 | 差距 |")
            lines.append("|--------|----------|----------|----------|------|")
            for sc in sorted_criteria:
                gap = sc.target_score - sc.current_score
                lines.append(
                    f"| P{6-sc.priority} | {sc.criterion} "
                    f"| {sc.current_score}/10 | {sc.target_score}/10 | {gap} |"
                )
            lines.append("")
        else:
            lines.append("*(待填充)*\n")

        lines.append("### 5. Obstacles\n")
        if atlas.obstacles:
            for obs in atlas.obstacles:
                lines.append(f"- ⚠️ {obs}")
            lines.append("")
        else:
            lines.append("*(待填充)*\n")

        lines.append("---\n")
        lines.append("## Part 3: 衡量价值与竞争\n")

        lines.append("### 6. Value\n")
        for vt in VALUE_TYPES:
            values = atlas.values_by_type(vt)
            label = VALUE_LABELS[vt]
            lines.append(f"**{label}:**")
            if values:
                for v in sorted(values, key=lambda x: x.magnitude, reverse=True):
                    mag_bar = "⬛" * v.magnitude + "⬜" * (5 - v.magnitude)
                    lines.append(f"- [{mag_bar}] {v.description}")
                    if v.evidence:
                        lines.append(f"  - 证据: {v.evidence}")
            else:
                lines.append("- *(待填充)*")
            lines.append("")

        lines.append("### 7. Competition\n")
        if atlas.competitors:
            sorted_comps = sorted(atlas.competitors, key=lambda x: x.threat_level, reverse=True)
            for c in sorted_comps:
                threat_bar = "🔴" * c.threat_level + "⚪" * (5 - c.threat_level)
                lines.append(f"**{c.name}** [{threat_bar}]")
                if c.job_overlap:
                    lines.append(f"Job重叠: {c.job_overlap}")
                if c.strengths:
                    lines.append("优势: " + "、".join(c.strengths))
                if c.weaknesses:
                    lines.append("劣势: " + "、".join(c.weaknesses))
                lines.append("")
        else:
            lines.append("*(待填充)*\n")

        return "\n".join(lines)

    @staticmethod
    def render_json(atlas: JobsAtlas) -> Dict:
        return {
            "product": atlas.product_name,
            "completeness_pct": atlas.completeness_pct(),
            "completeness": atlas.completeness(),
            "core_job": atlas.core_job,
            "related_jobs": atlas.related_jobs,
            "drivers": {
                dt: [
                    {
                        "description": d.description,
                        "influence_level": d.influence_level,
                        "evidence": d.evidence,
                    }
                    for d in atlas.drivers_by_type(dt)
                ]
                for dt in DRIVER_TYPES
            },
            "current_approaches": [
                {
                    "name": a.name,
                    "description": a.description,
                    "pain_points": a.pain_points,
                    "workarounds": a.workarounds,
                }
                for a in atlas.current_approaches
            ],
            "success_criteria": [
                {
                    "criterion": sc.criterion,
                    "measurement": sc.measurement,
                    "current_score": sc.current_score,
                    "target_score": sc.target_score,
                    "priority": sc.priority,
                }
                for sc in atlas.success_criteria
            ],
            "obstacles": atlas.obstacles,
            "values": {
                vt: [
                    {"description": v.description, "magnitude": v.magnitude, "evidence": v.evidence}
                    for v in atlas.values_by_type(vt)
                ]
                for vt in VALUE_TYPES
            },
            "competitors": [
                {
                    "name": c.name,
                    "job_overlap": c.job_overlap,
                    "strengths": c.strengths,
                    "weaknesses": c.weaknesses,
                    "threat_level": c.threat_level,
                }
                for c in atlas.competitors
            ],
        }
