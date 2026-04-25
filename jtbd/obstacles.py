"""JTBD 采用障碍诊断模块

基于 Wunker《Jobs to Be Done: A Roadmap》的 Obstacles 框架。

6种采用障碍 (Adoption Obstacles):
1. 缺乏知识 (Lack of Knowledge) — 客户不知道解决方案存在
2. 行为改变 (Behavior Change) — 需要改变根深蒂固的习惯
3. 多决策者 (Multiple Decision Makers) — 购买决策涉及多人
4. 高成本 (High Cost) — 价格或总拥有成本过高
5. 高风险 (High Risk) — 采用失败的后果严重
6. 不熟悉类别 (Unfamiliar Category) — 全新品类缺乏参照

4种使用障碍 (Usage Obstacles):
1. 有限基础设施 (Limited Infrastructure) — 缺乏支持使用的配套
2. 使用痛点 (Usage Pain Points) — 使用过程中体验差
3. 酷但没更好 (Cool But Not Better) — 新奇但没有真正进步
4. 未定向 (Undirected) — 不知道如何获得最大价值

5种对抗惯性方法:
1. 降低试用门槛 (Lower Trial Barriers)
2. 证明收益 (Prove Benefits)
3. 社交证明 (Social Proof)
4. 减少转换成本 (Reduce Switching Costs)
5. 创造紧迫感 (Create Urgency)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


ADOPTION_OBSTACLES = (
    "lack_of_knowledge",
    "behavior_change",
    "multiple_decision_makers",
    "high_cost",
    "high_risk",
    "unfamiliar_category",
)

USAGE_OBSTACLES = (
    "limited_infrastructure",
    "usage_pain_points",
    "cool_but_not_better",
    "undirected",
)

ALL_OBSTACLE_TYPES = ADOPTION_OBSTACLES + USAGE_OBSTACLES

OBSTACLE_LABELS: Dict[str, str] = {
    "lack_of_knowledge": "缺乏知识",
    "behavior_change": "行为改变",
    "multiple_decision_makers": "多决策者",
    "high_cost": "高成本",
    "high_risk": "高风险",
    "unfamiliar_category": "不熟悉类别",
    "limited_infrastructure": "有限基础设施",
    "usage_pain_points": "使用痛点",
    "cool_but_not_better": "酷但没更好",
    "undirected": "未定向",
}

OBSTACLE_DESCRIPTIONS: Dict[str, str] = {
    "lack_of_knowledge": "客户不知道解决方案的存在，或不理解它如何解决自己的问题",
    "behavior_change": "采用新方案需要客户改变根深蒂固的习惯或工作流程",
    "multiple_decision_makers": "购买/采用决策涉及多个利益相关者，增加决策复杂度",
    "high_cost": "价格或总拥有成本（包括学习成本、迁移成本）超出客户预期",
    "high_risk": "采用失败的后果严重（财务损失、职业风险、社交风险）",
    "unfamiliar_category": "产品属于全新品类，客户缺乏参照标准来评估",
    "limited_infrastructure": "缺乏支持产品使用的配套设施或生态系统",
    "usage_pain_points": "使用过程中存在摩擦点，降低产品价值感知",
    "cool_but_not_better": "产品新奇有趣但没有在客户的核心Job上带来真正进步",
    "undirected": "客户不知道如何使用产品获得最大价值，缺乏引导",
}

OBSTACLE_COUNTERMEASURES: Dict[str, List[str]] = {
    "lack_of_knowledge": [
        "内容营销：用客户语言描述痛点和解决方案",
        "场景化展示：演示产品如何解决具体问题",
        "口碑传播：让满意客户分享使用故事",
    ],
    "behavior_change": [
        "渐进式迁移：不要求一次性全部切换",
        "兼容模式：支持与旧方案共存",
        "习惯桥接：将新功能嵌入现有工作流",
    ],
    "multiple_decision_makers": [
        "角色化价值主张：为每个决策者准备针对性信息",
        "共识工具：提供帮助推动内部决策的材料",
        "试用体验：让关键决策者亲身体验产品价值",
    ],
    "high_cost": [
        "ROI计算器：量化解决方案带来的收益",
        "阶梯定价：提供入门级选项降低门槛",
        "对比展示：与当前方案的总成本对比（含时间成本）",
    ],
    "high_risk": [
        "保证承诺：无效退款、满意保证",
        "案例背书：展示同类客户的成功案例",
        "小范围试点：支持在有限范围内先试用",
    ],
    "unfamiliar_category": [
        "类比定位：用熟悉的品类帮助客户理解",
        "教育内容：帮助客户建立评估标准",
        "引导体验：设计首次使用的'Aha时刻'",
    ],
    "limited_infrastructure": [
        "提供配套工具或服务弥补基础设施缺口",
        "与生态合作伙伴合作提供完整解决方案",
        "设计离线或降级使用模式",
    ],
    "usage_pain_points": [
        "简化核心流程，减少操作步骤",
        "提供情境化帮助和引导",
        "收集使用反馈持续优化体验",
    ],
    "cool_but_not_better": [
        "回归核心Job，确保产品真正解决客户问题",
        "量化进步：让客户能感知到具体的改善",
        "去除不创造价值的花哨功能",
    ],
    "undirected": [
        "新用户引导流程（Onboarding）",
        "最佳实践指南和模板",
        "主动推荐下一步行动",
    ],
}

INERTIA_COUNTERMEASURES = (
    "lower_trial_barriers",
    "prove_benefits",
    "social_proof",
    "reduce_switching_costs",
    "create_urgency",
)

INERTIA_LABELS: Dict[str, str] = {
    "lower_trial_barriers": "降低试用门槛",
    "prove_benefits": "证明收益",
    "social_proof": "社交证明",
    "reduce_switching_costs": "减少转换成本",
    "create_urgency": "创造紧迫感",
}

INERTIA_TACTICS: Dict[str, List[str]] = {
    "lower_trial_barriers": [
        "免费试用期、Freemium模式",
        "无需注册即可体验核心功能",
        "一键导入旧数据/设置",
    ],
    "prove_benefits": [
        "对比演示：新旧方案的效果差异",
        "ROI计算器：量化节省的时间和成本",
        "客户证言：真实用户的改变故事",
    ],
    "social_proof": [
        "展示同行/同事的使用情况",
        "行业标杆案例",
        "用户社区和口碑传播",
    ],
    "reduce_switching_costs": [
        "提供数据迁移工具",
        "兼容旧系统/格式",
        "提供切换指南和专属支持",
    ],
    "create_urgency": [
        "量化不行动的成本（每天浪费X分钟）",
        "限时优惠或早鸟价格",
        "展示竞争对手/同行已在使用",
    ],
}


@dataclass
class ObstacleItem:
    """单个障碍项"""
    obstacle_type: str
    description: str
    severity: int = 3
    evidence: str = ""
    countermeasures: List[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return OBSTACLE_LABELS.get(self.obstacle_type, self.obstacle_type)

    @property
    def is_adoption(self) -> bool:
        return self.obstacle_type in ADOPTION_OBSTACLES

    @property
    def category(self) -> str:
        return "adoption" if self.is_adoption else "usage"


@dataclass
class ObstacleDiagnosis:
    """完整障碍诊断结果"""
    product_name: str
    target_job: str = ""
    obstacles: List[ObstacleItem] = field(default_factory=list)
    inertia_strategies: List[str] = field(default_factory=list)

    def adoption_obstacles(self) -> List[ObstacleItem]:
        return [o for o in self.obstacles if o.is_adoption]

    def usage_obstacles(self) -> List[ObstacleItem]:
        return [o for o in self.obstacles if not o.is_adoption]

    def top_obstacles(self, n: int = 3) -> List[ObstacleItem]:
        return sorted(self.obstacles, key=lambda x: x.severity, reverse=True)[:n]


class ObstacleAnalyzer:
    """障碍诊断工具

    用法示例::

        analyzer = ObstacleAnalyzer("旅行预订平台")
        analyzer.set_target_job("管理商务出差的住宿安排")

        analyzer.add_obstacle(
            "behavior_change",
            "用户已习惯使用携程，切换到新平台需要改变既有流程",
            severity=4,
            evidence="访谈中80%用户提到习惯性打开携程",
        )
        analyzer.add_obstacle(
            "high_risk",
            "担心新平台酒店信息不准确导致出差体验差",
            severity=3,
        )

        analyzer.add_inertia_strategy("lower_trial_barriers")
        analyzer.add_inertia_strategy("prove_benefits")

        diagnosis = analyzer.build()
        print(ObstacleAnalyzer.render_markdown(diagnosis))
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._job = ""
        self._obstacles: List[ObstacleItem] = []
        self._inertia_strategies: List[str] = []

    def set_target_job(self, job: str) -> "ObstacleAnalyzer":
        self._job = job
        return self

    def add_obstacle(self, obstacle_type: str, description: str,
                     severity: int = 3, evidence: str = "",
                     custom_countermeasures: Optional[List[str]] = None) -> "ObstacleAnalyzer":
        if obstacle_type not in ALL_OBSTACLE_TYPES:
            raise ValueError(
                f"未知障碍类型: {obstacle_type}，"
                f"可选: {ALL_OBSTACLE_TYPES}"
            )
        if not 1 <= severity <= 5:
            raise ValueError(f"严重程度 {severity} 超出范围 1-5")

        countermeasures = list(custom_countermeasures or [])
        if not countermeasures:
            countermeasures = list(OBSTACLE_COUNTERMEASURES.get(obstacle_type, []))

        item = ObstacleItem(
            obstacle_type=obstacle_type,
            description=description,
            severity=severity,
            evidence=evidence,
            countermeasures=countermeasures,
        )
        self._obstacles.append(item)
        return self

    def add_inertia_strategy(self, strategy: str) -> "ObstacleAnalyzer":
        if strategy not in INERTIA_COUNTERMEASURES:
            raise ValueError(
                f"未知惯性策略: {strategy}，可选: {INERTIA_COUNTERMEASURES}"
            )
        self._inertia_strategies.append(strategy)
        return self

    def build(self) -> ObstacleDiagnosis:
        return ObstacleDiagnosis(
            product_name=self._product,
            target_job=self._job,
            obstacles=list(self._obstacles),
            inertia_strategies=list(self._inertia_strategies),
        )

    @staticmethod
    def render_markdown(diagnosis: ObstacleDiagnosis) -> str:
        lines = [f"# 采用障碍诊断 — {diagnosis.product_name}\n"]
        if diagnosis.target_job:
            lines.append(f"**目标 Job:** {diagnosis.target_job}\n")

        adoption = diagnosis.adoption_obstacles()
        if adoption:
            lines.append(f"## 采用障碍 ({len(adoption)}项)\n")
            lines.append("*阻止客户从当前方案切换到新方案的障碍*\n")
            for item in sorted(adoption, key=lambda x: x.severity, reverse=True):
                severity_bar = "🔴" * item.severity + "⚪" * (5 - item.severity)
                lines.append(f"### {item.label} [{severity_bar}]\n")
                lines.append(f"**描述:** {item.description}\n")
                if item.evidence:
                    lines.append(f"**证据:** {item.evidence}\n")
                if item.countermeasures:
                    lines.append("**对策建议:**\n")
                    for cm in item.countermeasures:
                        lines.append(f"- {cm}")
                lines.append("")

        usage = diagnosis.usage_obstacles()
        if usage:
            lines.append(f"## 使用障碍 ({len(usage)}项)\n")
            lines.append("*影响客户持续使用和获得价值的障碍*\n")
            for item in sorted(usage, key=lambda x: x.severity, reverse=True):
                severity_bar = "🔴" * item.severity + "⚪" * (5 - item.severity)
                lines.append(f"### {item.label} [{severity_bar}]\n")
                lines.append(f"**描述:** {item.description}\n")
                if item.evidence:
                    lines.append(f"**证据:** {item.evidence}\n")
                if item.countermeasures:
                    lines.append("**对策建议:**\n")
                    for cm in item.countermeasures:
                        lines.append(f"- {cm}")
                lines.append("")

        if diagnosis.inertia_strategies:
            lines.append("## 对抗惯性策略\n")
            for strategy in diagnosis.inertia_strategies:
                label = INERTIA_LABELS.get(strategy, strategy)
                tactics = INERTIA_TACTICS.get(strategy, [])
                lines.append(f"### {label}\n")
                for t in tactics:
                    lines.append(f"- {t}")
                lines.append("")

        if not diagnosis.obstacles:
            lines.append("*尚未识别任何障碍。*\n")
            lines.append("**建议检查以下类型的障碍:**\n")
            lines.append("**采用障碍:**\n")
            for obs in ADOPTION_OBSTACLES:
                lines.append(f"- [ ] {OBSTACLE_LABELS[obs]}: {OBSTACLE_DESCRIPTIONS[obs]}")
            lines.append("\n**使用障碍:**\n")
            for obs in USAGE_OBSTACLES:
                lines.append(f"- [ ] {OBSTACLE_LABELS[obs]}: {OBSTACLE_DESCRIPTIONS[obs]}")

        top = diagnosis.top_obstacles(3)
        if top:
            lines.append("\n## 优先处理建议\n")
            lines.append("按严重程度排序，以下障碍应优先解决：\n")
            for i, obs in enumerate(top, 1):
                lines.append(f"{i}. **{obs.label}** (严重程度: {obs.severity}/5) — {obs.description}")

        return "\n".join(lines)

    @staticmethod
    def render_json(diagnosis: ObstacleDiagnosis) -> Dict:
        return {
            "product": diagnosis.product_name,
            "target_job": diagnosis.target_job,
            "adoption_obstacles": [
                {
                    "type": o.obstacle_type,
                    "label": o.label,
                    "description": o.description,
                    "severity": o.severity,
                    "evidence": o.evidence,
                    "countermeasures": o.countermeasures,
                }
                for o in diagnosis.adoption_obstacles()
            ],
            "usage_obstacles": [
                {
                    "type": o.obstacle_type,
                    "label": o.label,
                    "description": o.description,
                    "severity": o.severity,
                    "evidence": o.evidence,
                    "countermeasures": o.countermeasures,
                }
                for o in diagnosis.usage_obstacles()
            ],
            "inertia_strategies": [
                {
                    "strategy": s,
                    "label": INERTIA_LABELS.get(s, s),
                    "tactics": INERTIA_TACTICS.get(s, []),
                }
                for s in diagnosis.inertia_strategies
            ],
            "top_obstacles": [
                {"type": o.obstacle_type, "label": o.label, "severity": o.severity}
                for o in diagnosis.top_obstacles()
            ],
        }
