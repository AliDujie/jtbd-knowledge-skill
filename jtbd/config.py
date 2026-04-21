"""JTBD Skill 配置模块

定义知识库路径、分析维度、默认参数等全局配置。
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List


KNOWLEDGE_BASE_DIR = Path(__file__).parent.parent

KNOWLEDGE_FILES: Dict[str, str] = {
    "theory": "01-theory-foundation.md",
    "principles": "02-principles.md",
    "forces": "03-forces-of-progress.md",
    "system": "04-system-of-progress.md",
    "research": "05-research-methods.md",
    "analysis": "06-analysis-framework.md",
    "innovation": "07-innovation-guide.md",
    "business": "08-business-decisions.md",
    "cases": "09-case-studies.md",
    "models": "10-two-models.md",
    "reference": "11-quick-reference.md",
}

FORCE_TYPES = ("push", "pull", "anxiety", "inertia")

FORCE_LABELS: Dict[str, str] = {
    "push": "推力 (Push)",
    "pull": "拉力 (Pull)",
    "anxiety": "焦虑 (Anxiety)",
    "inertia": "惯性 (Inertia)",
}

FORCE_CATEGORIES: Dict[str, str] = {
    "push": "demand_generating",
    "pull": "demand_generating",
    "anxiety": "demand_reducing",
    "inertia": "demand_reducing",
}

PROGRESS_SYSTEM_STAGES = (
    "imagine",
    "search",
    "use",
    "realize",
)

PROGRESS_SYSTEM_LABELS: Dict[str, str] = {
    "imagine": "想象更好的生活 (New Me)",
    "search": "搜索和选择解决方案",
    "use": "使用解决方案实现进步",
    "realize": "实现新我 → 新渴望出现",
}

INTERVIEW_DIMENSIONS = (
    "competition",
    "push",
    "pull",
    "anxiety",
    "validation",
)

JTBD_STATEMENT_VERBS = (
    "help me",
    "give me",
    "take away",
    "free me",
    "equip me",
    "make the",
)

INNOVATION_SIGNALS = (
    "compensating_behavior",
    "unexpected_users",
    "upstream_opportunity",
    "downstream_opportunity",
    "churn_insight",
)


@dataclass
class AnalysisConfig:
    """分析任务的运行时配置"""

    include_forces: List[str] = field(default_factory=lambda: list(FORCE_TYPES))
    include_stages: List[str] = field(
        default_factory=lambda: list(PROGRESS_SYSTEM_STAGES)
    )
    interview_dimensions: List[str] = field(
        default_factory=lambda: list(INTERVIEW_DIMENSIONS)
    )
    max_questions_per_dimension: int = 5
    output_format: str = "markdown"
    language: str = "zh"

    def validate(self) -> None:
        for f in self.include_forces:
            if f not in FORCE_TYPES:
                raise ValueError(f"未知的力量类型: {f}，可选: {FORCE_TYPES}")
        for s in self.include_stages:
            if s not in PROGRESS_SYSTEM_STAGES:
                raise ValueError(f"未知的阶段: {s}，可选: {PROGRESS_SYSTEM_STAGES}")
        if self.output_format not in ("markdown", "json", "text"):
            raise ValueError(
                f"未知的输出格式: {self.output_format}，可选: markdown, json, text"
            )
