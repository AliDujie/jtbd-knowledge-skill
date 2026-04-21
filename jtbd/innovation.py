"""JTBD 创新机会发现模块

提供创新信号识别、机会评估和创新检查清单工具。
"""

from dataclasses import dataclass, field
from typing import Dict, List

from .config import INNOVATION_SIGNALS
from .templates import INNOVATION_CHECKLIST


SIGNAL_LABELS: Dict[str, str] = {
    "compensating_behavior": "补偿行为",
    "unexpected_users": "异常客户",
    "upstream_opportunity": "上游机会",
    "downstream_opportunity": "下游机会",
    "churn_insight": "流失洞察",
}

SIGNAL_DESCRIPTIONS: Dict[str, str] = {
    "compensating_behavior": "客户以非预期方式使用产品、组合多个产品、自己创造解决方案",
    "unexpected_users": "完全出乎意料的用户群，往往揭示新的 Job",
    "upstream_opportunity": "问'之前是什么？'发现的上游需求",
    "downstream_opportunity": "问'接下来是什么？'发现的下游需求",
    "churn_insight": "流失客户可能因为 Job Done 而离开，蕴含新机会",
}

DESIGN_PRINCIPLES = [
    "聚焦情感进步而非功能堆砌",
    "消除权衡而非优化权衡",
    "避免过度工程化——识别并消除不创造价值的功能",
    "开发互补产品而非堆砌功能（避免'瑞士军刀'产品）",
    "将产品组合设计为协同工作的系统",
]

INNOVATION_TRAPS = [
    "不要从解决方案开始（先理解 JTBD）",
    "不要忽视客户动机追随自己偏见",
    "不要相信'非消费者'概念（有 JTBD 就一定在用某种方案）",
    "不要假设低价就能赢（客户最看重进步）",
    "不要用一个产品解决太多 Job",
]


@dataclass
class InnovationSignal:
    """创新信号"""
    signal_type: str
    observation: str
    potential_job: str = ""
    priority: int = 1

    @property
    def label(self) -> str:
        return SIGNAL_LABELS.get(self.signal_type, self.signal_type)


@dataclass
class InnovationOpportunity:
    """创新机会"""
    title: str
    description: str
    signals: List[InnovationSignal] = field(default_factory=list)
    target_job: str = ""
    feasibility: int = 3
    impact: int = 3

    @property
    def score(self) -> int:
        return self.feasibility * self.impact


class InnovationFinder:
    """创新机会发现器

    用法示例::

        finder = InnovationFinder()
        finder.add_signal("compensating_behavior",
                          "用户用Excel手动追踪订单状态",
                          potential_job="实时掌握订单进度")
        finder.add_opportunity("自动订单追踪",
                               "提供实时订单状态推送",
                               feasibility=4, impact=5)
        report = finder.render_markdown()
    """

    def __init__(self) -> None:
        self.signals: List[InnovationSignal] = []
        self.opportunities: List[InnovationOpportunity] = []
        self.checklist_status: Dict[str, bool] = {
            item: False for item in INNOVATION_CHECKLIST
        }

    def add_signal(self, signal_type: str, observation: str,
                   potential_job: str = "", priority: int = 1) -> InnovationSignal:
        if signal_type not in INNOVATION_SIGNALS:
            valid = ", ".join(INNOVATION_SIGNALS)
            raise ValueError(f"未知信号类型: {signal_type}，可选: {valid}")
        sig = InnovationSignal(signal_type=signal_type,
                               observation=observation,
                               potential_job=potential_job,
                               priority=priority)
        self.signals.append(sig)
        return sig

    def add_opportunity(self, title: str, description: str,
                        target_job: str = "",
                        feasibility: int = 3,
                        impact: int = 3) -> InnovationOpportunity:
        opp = InnovationOpportunity(
            title=title, description=description,
            target_job=target_job,
            feasibility=feasibility, impact=impact,
        )
        relevant = [s for s in self.signals
                     if s.potential_job and s.potential_job in target_job]
        opp.signals = relevant
        self.opportunities.append(opp)
        return opp

    def check_item(self, index: int, status: bool = True) -> None:
        items = list(self.checklist_status.keys())
        if 0 <= index < len(items):
            self.checklist_status[items[index]] = status

    def get_signals_by_type(self, signal_type: str) -> List[InnovationSignal]:
        return [s for s in self.signals if s.signal_type == signal_type]

    def get_top_opportunities(self, n: int = 5) -> List[InnovationOpportunity]:
        return sorted(self.opportunities, key=lambda o: o.score, reverse=True)[:n]

    def render_markdown(self) -> str:
        lines = ["# 创新机会分析\n"]

        if self.signals:
            lines.append("## 创新信号\n")
            for sig_type in INNOVATION_SIGNALS:
                sigs = self.get_signals_by_type(sig_type)
                if not sigs:
                    continue
                lines.append(f"### {SIGNAL_LABELS[sig_type]}\n")
                for s in sigs:
                    lines.append(f"- {s.observation}")
                    if s.potential_job:
                        lines.append(f"  - 潜在 Job: {s.potential_job}")
                lines.append("")

        if self.opportunities:
            lines.append("## 创新机会（按优先级排序）\n")
            for opp in self.get_top_opportunities(10):
                lines.append(
                    f"### {opp.title} "
                    f"(可行性:{opp.feasibility} × 影响力:{opp.impact} = {opp.score})\n"
                )
                lines.append(f"{opp.description}\n")
                if opp.target_job:
                    lines.append(f"**目标 Job:** {opp.target_job}\n")

        lines.append("## 创新检查清单\n")
        for item, done in self.checklist_status.items():
            mark = "✅" if done else "⬜"
            lines.append(f"- {mark} {item}")

        lines.append("\n## 设计原则提醒\n")
        for p in DESIGN_PRINCIPLES:
            lines.append(f"- {p}")

        lines.append("\n## 常见陷阱警示\n")
        for t in INNOVATION_TRAPS:
            lines.append(f"- ⚠️ {t}")

        return "\n".join(lines)

    def export_json(self) -> Dict:
        return {
            "signals": [
                {"type": s.signal_type, "label": s.label,
                 "observation": s.observation,
                 "potential_job": s.potential_job,
                 "priority": s.priority}
                for s in self.signals
            ],
            "opportunities": [
                {"title": o.title, "description": o.description,
                 "target_job": o.target_job,
                 "feasibility": o.feasibility,
                 "impact": o.impact, "score": o.score}
                for o in self.get_top_opportunities(10)
            ],
            "checklist": self.checklist_status,
        }
