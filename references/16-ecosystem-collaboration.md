# JTBD 跨技能协作指南

> Jobs-to-be-Done 如何与 AliDujie 生态系统中的其他技能协作

---

## JTBD 在生态系统中的位置

JTBD 是 7 技能工作流的 **需求洞察层**，理解"用户为什么这样做"：

```
Persona → JTBD (你在这里) → UDM → QuantUX → VPD → SWD
```

## JTBD 与其他技能的协作

### JTBD → UDM：从洞察到研究方法

JTBD 发现核心 Jobs 和痛点后，UDM 提供验证这些洞察的研究方法：

| JTBD 输出 | → UDM 输入 | 推荐方法 |
|-----------|-----------|---------|
| 核心 Job 描述 | 研究目标 | 情境访谈 |
| 痛点严重度 | 访谈重点 | 关键事件法 |
| 替代方案（Workaround） | 观察对象 | 影随观察 |
| 四力分析结果 | 研究框架 | 日记研究 |
| 机会评分 Top 3 | 优先级 | 焦点小组 |

### JTBD → QuantUX：从定性到定量

JTBD 的机会评分需要 QuantUX 的统计验证：

| JTBD 输出 | → QuantUX 输入 | 验证方法 |
|-----------|---------------|---------|
| Opportunity Score | 优先级排序 | MaxDiff 分析 |
| 四力分析 | 用户分群 | 聚类分析 |
| Job 满意度 | 基线测量 | HEART 指标 |
| 用户细分 | A/B 分组 | 分层测试 |

### JTBD → VPD：从需求到价值主张

JTBD 发现的 Jobs 直接映射到 VPD 画布：

| JTBD 输出 | → VPD 画布位置 |
|-----------|---------------|
| Functional Job | 客户工作（功能性） |
| Emotional Job | 客户工作（情感性） |
| Social Job | 客户工作（社会性） |
| Pain + Severity | 客户痛点（量化） |
| Expected Outcome | 客户收益（期望的） |

### JTBD → SWD：从数据到叙事

JTBD 的机会评分和四力分析是天然的故事素材：

| JTBD 输出 | → SWD 呈现 | 推荐图表 |
|-----------|-----------|---------|
| Opportunity Atlas | 机会地图 | 气泡图 |
| 四力分析 | 力场图 | 力场图 |
| Job 重要性 vs 满意度 | 差距分析 | 散点图 |

## JTBD 独立使用 vs 协作使用

### 适合独立使用的场景

- **产品方向评估**：用 JTBD 评估新功能是否解决核心 Job
- **竞品分析**：比较竞品对同一 Job 的解决程度
- **用户访谈设计**：用 JTBD 框架引导访谈
- **优先级排序**：用机会评分排序需求

### 适合协作使用的场景

- **完整产品优化**：JTBD → VPD → QuantUX → SWD
- **新市场进入**：Persona → JTBD → UDM → QuantUX
- **投资决策**：JTBD → VPD (商业化路径) → SWD

## 端到端工作流示例

### 场景：旅行平台功能优先级

```python
# === 阶段 1: JTBD 发现机会 ===
from jtbd import JTBDSkill

jtbd = JTBDSkill("旅行平台")
# 发现 Top 3 Jobs:
# 1. "快速找到性价比最优的住宿" (Opportunity: 8.2)
# 2. "一站式管理行程" (Opportunity: 7.5)
# 3. "简化差旅报销" (Opportunity: 6.8)

# === 阶段 2: VPD 设计价值主张 ===
from vpd import VPDSkill

vpd = VPDSkill("旅行平台", "商旅用户")
canvas = vpd.analyze_canvas(
    product_name="商旅优选",
    jobs=["快速找酒店", "行程管理", "报销简化"],
    pains=["搜索耗时", "行程分散", "报销繁琐"],
    gains=["一键预订", "统一管理", "自动报销"]
)

# === 阶段 3: QuantUX 验证优先级 ===
from quantux import QuantUXSkill

quantux = QuantUXSkill("旅行平台")
maxdiff = quantux.run_maxdiff(
    items=["智能推荐", "行程管理", "自动报销", "价格提醒"],
    n_respondents=300
)
# → "智能推荐" 偏好份额最高 (35%)

# === 阶段 4: SWD 呈现决策 ===
from swd import SWDSkill

swd = SWDSkill("功能优先级汇报")
story = swd.build_story(
    protagonist="产品团队",
    imbalance="资源有限，无法同时推进 3 个功能",
    resolution="数据驱动优先级: 智能推荐 > 行程管理 > 报销"
)
```

## JTBD 的 CEO 决策视角

JTBD 内置 CEO 级决策支持：

| 模块 | CEO 关注 | 输出 |
|------|---------|------|
| 机会评分 | 哪个机会最大？ | 量化排序 |
| 四力分析 | 用户为什么换/不换？ | 战略杠杆 |
| 竞品对标 | 我们在哪落后？ | 竞争定位 |
| 市场机会 | 值得投入多少？ | ROI 估算 |

---

*本文档是 AliDujie JTBD Knowledge 技能生态系统的补充参考。*
