---
name: jtbd-knowledge-skill
description: >
  JTBD (Jobs to Be Done) 理论与实践工具集。基于 Klement/Christensen/Moesta-Ulwick 三大流派，
  提供 9 项可执行能力（访谈提纲、问卷设计、机会评分、优先级矩阵、竞争分析、营销文案、
  增长策略、JTBD 描述生成、场景库深度分析报告）和 11 篇方法论知识库。
  附带完整 Python API（JTBDAnalyzer / InterviewBuilder / ForcesProfile / InnovationFinder），
  支持四力量化分析、创新信号识别与结构化报告输出，以及CEO决策视角的市场规模估算、优先级评分与商业化可行性分析。
---

# JTBD (Jobs to Be Done) 执行技能

基于 Alan Klement《When Coffee and Kale Compete》的 JTBD 理论。本 Skill 不仅提供理论指导，更具备直接执行能力——可以生成访谈提纲、设计问卷、计算机会分数、输出优先级建议、撰写营销文案等。

## 核心理论

JTBD 是消费者将现有生活状况转变为更理想状态的过程。客户购买产品不是为了拥有它，而是为了成为"更好的自己"。

**进步力量模型（Forces of Progress）**：推力（Push，对现状不满）、拉力（Pull，对更好生活的渴望）、焦虑（Anxiety，对新方案的担忧）、惯性（Inertia，阻止改变的习惯力量）。净推动力 = (推力+拉力) - (焦虑+惯性)。

**九大原则**：客户想要进步而非产品、人有 Job 物品没有、竞争由客户心智定义、采用新方案意味着放弃旧方案、补偿行为=创新机会、重视进步过程而非终点、进步定义价值且对比揭示价值、解决方案在使用时刻之外也提供价值、生产者/消费者/解决方案/Job 是一个系统。

## 触发条件

| 触发词 / 场景 | 激活能力 |
|---|---|
| **全面分析、完整分析、深度分析、全维度分析** | **能力九：场景库 8 模块完整报告** |
| 访谈提纲、访谈问题、用户访谈、深度访谈 | 能力一：生成 JTBD 访谈提纲 |
| 问卷、调查、量化研究、survey | 能力二：设计 JTBD 调查问卷 |
| 机会评估、机会分数、值不值得做、优先级 | 能力三+四：机会评分与优先级矩阵 |
| 竞争分析、竞品、替代方案 | 能力五：JTBD 竞争分析 |
| 文案、营销、广告、落地页、推广 | 能力六：JTBD 营销文案 |
| 增长、留存、流失、churn | 能力七：增长与留存策略 |
| JTBD 描述、Job 描述、整理发现 | 能力八：JTBD 描述生成与验证 |
| 场景库、场景分析、场景合并、JTBD 分析报告 | 能力九：场景库数据分析与报告 |
| 产品创新、新功能、新产品 | 综合运用三+四+五 |
| 市场规模、TAM/SAM/SOM、市场估算 | CEO: 市场规模估算 |
| 优先级评分、资源分配、投入优先 | CEO: 优先级评分与资源分配 |
| 商业化、付费意愿、ROI、Go/No-Go | CEO: 商业化可行性分析 |
| 完整分析 + CEO 决策 | 综合运用 + CEO 决策视角（`analyze(include_ceo_analysis=True)`） |

## 执行能力概览

**能力一：生成 JTBD 访谈提纲** — 收集产品名称、目标用户、访谈目的后，确定访谈对象类型，从 6 个模块（挣扎时刻/竞争格局/推力拉力/焦虑惯性/进步验证/功能验证）组合生成结构化提纲，附执行建议。详见 `references/05-research-methods.md`。

**能力二：设计 JTBD 调查问卷** — 支持筛选型/验证型/竞争型三类问卷，输出完整问卷（题目+选项+跳转逻辑+预计时长）。详见 `references/05-research-methods.md`。

**能力三：计算 JTBD 机会分数** — 综合四个维度评分：挣扎强度(30%)、替代方案满意度(25%)、市场规模(25%)、预算可获取性(20%)。4.0-5.0=高机会，3.0-3.9=中等，2.0-2.9=低，1.0-1.9=不建议。详见 `references/06-analysis-framework.md`。

**能力四：输出优先级矩阵** — 对多个 Job 标准化描述、四力分析、机会评分后输出排序矩阵和行动建议。详见 `references/06-analysis-framework.md`。

**能力五：JTBD 竞争分析** — 识别直接竞品/间接竞品/非消费方案，验证竞争关系（找到实际切换用户），分析四力对比，输出竞争地图。详见 `references/08-business-decisions.md`。

**能力六：生成 JTBD 营销文案** — 按挣扎共鸣→进步愿景→消除焦虑→克服惯性→行动号召结构，从三个不同角度（推力/拉力/焦虑消除）生成文案方案。详见 `references/08-business-decisions.md`。

**能力七：增长与留存策略** — 识别上游/下游/横向增长机会，按三种流失原因（Job Done/更好替代/未实现进步）生成针对性策略。详见 `references/08-business-decisions.md`。

**能力八：JTBD 描述生成与验证** — 从访谈记录提取要素，生成标准 JTBD 描述（`[动作]+[挣扎]，这样我就能+[进步]`），用三个测试问题验证质量。详见 `references/06-analysis-framework.md`。

**能力九：场景库数据分析与报告** — 最复杂的执行能力。读取场景库 Excel，经过数据解析→场景语义合并→二级主题四力分析→报告生成→部署交付 5 个阶段，输出 8 模块 HTML 交互报告。场景分层遵循四原则（不过于抽象、粒度对齐业务动作、灵活层级深度、100%覆盖零遗漏）。详见 `references/06-analysis-framework.md`。

## CEO 决策视角

在 JTBD 分析完成后，自动附加商业决策支持分析：

**CEO 方法一：市场规模估算** — 基于 JTBD 分析结果估算 TAM/SAM/SOM，输出关键假设和分阶段验证计划（定性→定量→MVP→试点）。

**API:** `skill.generate_market_size_estimate(jobs)` — jobs 可选，默认使用分析器中已有数据。

**CEO 方法二：优先级评分** — 综合重要性、满意度差距、置信度计算机会分，输出资源分配建议和验证时间线。

**API:** `skill.generate_priority_scoring(jobs)`

**CEO 方法三：商业化可行性** — 评估付费意愿(WTP)、投入产出比(ROI)、回收期，输出 Go/No-Go 决策建议。

**API:** `skill.generate_commercialization_feasibility(jobs)`

**一键生成**: `skill.analyze(include_ceo_analysis=True)` — 在标准分析报告后自动附加全部 CEO 决策模块。

**默认行为**: 当用户要求全面分析、深度分析，或涉及商业决策场景时，应自动设置 `include_ceo_analysis=True`。

## Python 工具包

位于 `jtbd/` 目录，纯标准库实现，无外部依赖。

| 模块 | 核心类/函数 | 用途 |
|---|---|---|
| `analyzer.py` | `JTBDAnalyzer` | 创建 JTBD 描述、管理四力、生成报告 |
| `interview.py` | `InterviewBuilder` | 按维度生成定制化访谈问题列表 |
| `forces.py` | `ForcesProfile` | 推力/拉力/焦虑/惯性结构化分析与诊断 |
| `innovation.py` | `InnovationFinder` | 创新信号识别、机会评估、检查清单 |
| `__init__.py` | `JTBDSkill` | CEO 市场规模 / 优先级评分 / 商业化可行性 / 一键分析 |
| `config.py` | `AnalysisConfig` | 运行时配置：分析维度、输出格式等 |
| `utils.py` | `load_knowledge`, `search_knowledge` | 知识库加载与关键词搜索 |
| `templates.py` | 模板常量 | 访谈问题、报告模板、分析框架、场景合并规则 |

### 快速使用

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 分析引擎
analyzer = JTBDAnalyzer("我的项目")
analyzer.add_statement("Help me", "快速找到合适的住处", "专注工作")
analyzer.add_force("push", "频繁出差找酒店耗时", intensity=4)
print(analyzer.generate_report())

# 访谈框架
builder = InterviewBuilder("用户访谈")
builder.include_dimensions(["competition", "push", "anxiety"])
print(InterviewBuilder.render_markdown(builder.build()))

# 四力分析
profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧", intensity=4)
profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
print(profile.diagnose())

# 创新发现
finder = InnovationFinder()
finder.add_signal("compensating_behavior", "用户用Excel手动追踪")
print(finder.render_markdown())

# 知识库搜索
from jtbd import search_knowledge
results = search_knowledge("焦虑")
```

### Facade 方法

`JTBDSkill` 提供一站式 `analyze()` 入口，自动编排分析 → 建议 → 市场估算 → 验证计划 → Go/No-Go 决策全流程：

```python
from jtbd import JTBDSkill
skill = JTBDSkill()
result = skill.analyze(
    product="在线旅行预订平台",
    target_user="商务出差人群",
    pain_points=["找酒店太耗时", "价格不透明"],
    competitors=["携程", "美团"],
    include_ceo_analysis=True  # 自动附加 CEO 决策分析
)
```

## 知识库索引

所有文档位于 `references/` 目录：

| 文件 | 主题 | 关键内容 |
|---|---|---|
| `01-theory-foundation.md` | 理论基础 | Klement JTBD 定义、与传统需求分析的区别 |
| `02-principles.md` | 核心原则 | 九大原则详解与实战应用 |
| `03-forces-of-progress.md` | 进步力量模型 | 四种力量详解、子类型、诊断方法 |
| `04-system-of-progress.md` | 进步系统 | System of Progress 完整框架 |
| `05-research-methods.md` | 信息采集方法 | 访谈设计、问卷设计、观察法 |
| `06-analysis-framework.md` | 信息整理框架 | 机会评分、优先级矩阵、场景分层 |
| `07-innovation-guide.md` | 创新指南 | 创新信号识别、补偿行为分析 |
| `08-business-decisions.md` | 业务决策 | 竞争分析、营销文案、增长策略 |
| `09-case-studies.md` | 案例精华 | 经典 JTBD 案例分析 |
| `10-two-models.md` | 两种模型对比 | Klement vs Moesta-Ulwick 流派差异 |
| `11-quick-reference.md` | 速查手册 | 全部概念速查与公式汇总 |

### AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 优先通过 `JTBDSkill` Facade 调用，亦可直接使用 JTBDAnalyzer 等子类 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示 |
| 3 | **触发映射** | 根据用户意图选择对应能力（参见触发条件表） |
| 4 | **四力优先** | 任何分析先进行四力（推力/拉力/焦虑/惯性）分析 |
| 5 | **知识优先** | 理论问题先调用 `search_knowledge()` 查询 |
| 6 | **CEO 决策默认附加** | 全面分析或涉及商业决策时，自动使用 `include_ceo_analysis=True` |
| 7 | **完整交付** | 每个任务产出完整可用的分析/报告/建议 |
