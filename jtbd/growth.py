"""JTBD 增长与留存策略模块

对应 SKILL.md 执行能力七：JTBD 增长与留存策略。
"""

from dataclasses import dataclass, field
from typing import Dict, List


CHURN_TYPES = ("job_done", "better_alternative", "no_progress")

CHURN_LABELS: Dict[str, str] = {
    "job_done": "Job Done — 客户完成了任务，不再需要产品",
    "better_alternative": "更好替代 — 客户找到了更好的解决方案",
    "no_progress": "未实现进步 — 客户没有感受到进步",
}

CHURN_STRATEGIES: Dict[str, str] = {
    "job_done": "帮客户发现新的 Job，解锁新渴望",
    "better_alternative": "分析竞品优势，消除权衡",
    "no_progress": "优化新用户引导，帮助建立使用习惯",
}

GROWTH_LEVERS = ("upstream", "downstream", "lateral")

LEVER_LABELS: Dict[str, str] = {
    "upstream": "上游机会 — 客户在使用我们之前需要什么",
    "downstream": "下游机会 — 客户实现进步后面临什么新挑战",
    "lateral": "横向机会 — 同一客户还有什么其他 Job",
}


@dataclass
class GrowthOpportunity:
    lever: str
    description: str
    potential_product: str = ""
    priority: int = 3


@dataclass
class ChurnSegment:
    churn_type: str
    description: str
    user_count: int = 0
    strategy: str = ""

    def __post_init__(self):
        if not self.strategy:
            self.strategy = CHURN_STRATEGIES.get(self.churn_type, "")


@dataclass
class KeyHabit:
    habit: str
    best_user_pct: int = 0
    churned_user_pct: int = 0
    timeframe: str = ""


@dataclass
class GrowthPlan:
    product_name: str
    target_job: str = ""
    growth_opportunities: List[GrowthOpportunity] = field(default_factory=list)
    churn_segments: List[ChurnSegment] = field(default_factory=list)
    key_habits: List[KeyHabit] = field(default_factory=list)
    flywheel_steps: List[str] = field(default_factory=list)
    action_items: List[str] = field(default_factory=list)


class GrowthStrategyBuilder:
    """增长与留存策略构建器

    用法示例::

        builder = GrowthStrategyBuilder("旅行预订平台")
        builder.set_target_job("出差时快速找到合适住处")
        builder.add_growth_opportunity("upstream", "出差前的行程规划", "行程助手")
        builder.add_churn_segment("no_progress", "新用户首周未完成预订", 200)
        builder.add_key_habit("首周完成至少1次预订", best_pct=85, churned_pct=20, timeframe="首7天")
        builder.set_flywheel(["客户出差需求", "搜索住处", "快速预订", "满意体验", "下次复用", "推荐同事"])
        plan = builder.build()
        print(builder.render_markdown(plan))
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._job = ""
        self._opportunities: List[GrowthOpportunity] = []
        self._churn: List[ChurnSegment] = []
        self._habits: List[KeyHabit] = []
        self._flywheel: List[str] = []
        self._actions: List[str] = []

    def set_target_job(self, job: str) -> "GrowthStrategyBuilder":
        self._job = job
        return self

    def add_growth_opportunity(self, lever: str, description: str,
                               potential_product: str = "", priority: int = 3) -> "GrowthStrategyBuilder":
        if lever not in GROWTH_LEVERS:
            raise ValueError(f"未知增长杠杆: {lever}，可选: {GROWTH_LEVERS}")
        self._opportunities.append(GrowthOpportunity(
            lever=lever, description=description,
            potential_product=potential_product, priority=priority,
        ))
        return self

    def add_churn_segment(self, churn_type: str, description: str,
                          user_count: int = 0, strategy: str = "") -> "GrowthStrategyBuilder":
        if churn_type not in CHURN_TYPES:
            raise ValueError(f"未知流失类型: {churn_type}，可选: {CHURN_TYPES}")
        self._churn.append(ChurnSegment(
            churn_type=churn_type, description=description,
            user_count=user_count, strategy=strategy,
        ))
        return self

    def add_key_habit(self, habit: str, best_pct: int = 0,
                      churned_pct: int = 0, timeframe: str = "") -> "GrowthStrategyBuilder":
        self._habits.append(KeyHabit(
            habit=habit, best_user_pct=best_pct,
            churned_user_pct=churned_pct, timeframe=timeframe,
        ))
        return self

    def set_flywheel(self, steps: List[str]) -> "GrowthStrategyBuilder":
        self._flywheel = steps
        return self

    def add_action(self, action: str) -> "GrowthStrategyBuilder":
        self._actions.append(action)
        return self

    def build(self) -> GrowthPlan:
        return GrowthPlan(
            product_name=self._product, target_job=self._job,
            growth_opportunities=self._opportunities, churn_segments=self._churn,
            key_habits=self._habits, flywheel_steps=self._flywheel,
            action_items=self._actions,
        )

    @staticmethod
    def render_markdown(plan: GrowthPlan) -> str:
        lines = [f"# 增长与留存策略 — {plan.product_name}\n"]
        if plan.target_job:
            lines.append(f"**目标 Job:** {plan.target_job}\n")

        if plan.flywheel_steps:
            lines.append("## 增长飞轮\n")
            lines.append(" → ".join(plan.flywheel_steps) + " → (循环)\n")

        if plan.growth_opportunities:
            lines.append("## 增长机会\n")
            sorted_opps = sorted(plan.growth_opportunities, key=lambda o: o.priority, reverse=True)
            for opp in sorted_opps:
                label = LEVER_LABELS.get(opp.lever, opp.lever)
                lines.append(f"- **[优先级{opp.priority}]** {opp.description}")
                lines.append(f"  - 类型: {label}")
                if opp.potential_product:
                    lines.append(f"  - 潜在产品/服务: {opp.potential_product}")
            lines.append("")

        if plan.churn_segments:
            lines.append("## 流失分析\n")
            for seg in plan.churn_segments:
                label = CHURN_LABELS.get(seg.churn_type, seg.churn_type)
                count = f"（{seg.user_count}人）" if seg.user_count else ""
                lines.append(f"### {label} {count}\n")
                lines.append(f"{seg.description}\n")
                lines.append(f"**策略:** {seg.strategy}\n")

        if plan.key_habits:
            lines.append("## 关键习惯对比\n")
            lines.append("| 习惯 | 最佳用户 | 流失用户 | 时间窗口 |")
            lines.append("|------|---------|---------|---------|")
            for h in plan.key_habits:
                lines.append(f"| {h.habit} | {h.best_user_pct}% | {h.churned_user_pct}% | {h.timeframe} |")
            lines.append("")
            if plan.key_habits:
                top = plan.key_habits[0]
                lines.append(f"**建议:** 引导新用户在{top.timeframe or '首周'}内完成「{top.habit}」\n")

        if plan.action_items:
            lines.append("## 行动计划\n")
            for i, a in enumerate(plan.action_items, 1):
                lines.append(f"{i}. {a}")

        return "\n".join(lines)

    @staticmethod
    def render_json(plan: GrowthPlan) -> Dict:
        return {
            "product": plan.product_name, "target_job": plan.target_job,
            "flywheel": plan.flywheel_steps,
            "growth_opportunities": [
                {"lever": o.lever, "description": o.description,
                 "potential_product": o.potential_product, "priority": o.priority}
                for o in plan.growth_opportunities
            ],
            "churn_segments": [
                {"type": s.churn_type, "description": s.description,
                 "count": s.user_count, "strategy": s.strategy}
                for s in plan.churn_segments
            ],
            "key_habits": [
                {"habit": h.habit, "best_pct": h.best_user_pct,
                 "churned_pct": h.churned_user_pct, "timeframe": h.timeframe}
                for h in plan.key_habits
            ],
            "actions": plan.action_items,
        }
