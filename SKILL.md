---
name: jtbd-knowledge-skill
description: >
  JTBD (Jobs to Be Done) v3.0 完整工具集。融合四大学派——Klement 进步力量、
  Ulwick ODI 机会算法、Wunker Jobs Atlas 七维度、Kalbach Job Stories 整合——
  提供 13 项可执行能力和 15 篇方法论知识库。附带完整 Python API（JTBDSkill 统一入口），
  覆盖访谈→问卷→评分→优先级→竞争→营销→增长→描述→Job Map→Outcome→Stories→障碍→Atlas
  全流程，以及 CEO 决策视角的市场规模估算、优先级评分与商业化可行性分析。
---

# JTBD (Jobs to Be Done) v3.0 执行技能

融合四大 JTBD 学派的完整工具集，不仅提供理论指导，更具备直接执行能力。

**四大学派融合**：Klement（进步力量、切换访谈、情感分析）→ Ulwick ODI（Opportunity Algorithm、Desired Outcome、Universal Job Map）→ Wunker Jobs Atlas（七维度分析、障碍诊断、ABC Job Drivers）→ Kalbach 整合（Job Stories、VPC 整合、多格式描述）。

**进步力量模型**：推力（Push）、拉力（Pull）、焦虑（Anxiety）、惯性（Inertia）。净推动力 = (推力+拉力) - (焦虑+惯性)。

## 触发条件

| 触发词 / 场景 | 激活能力 |
|---|---|
| **全面分析、完整分析、深度分析** | **能力九 + CEO 全流程** |
| 访谈提纲、用户访谈、Switch 访谈、ODI 访谈 | 能力一：访谈提纲生成 |
| 问卷、调查、量化、survey、ODI 量表 | 能力二：调查问卷设计 |
| 机会评估、机会分数、ODI 评分 | 能力三：机会评分 |
| 优先级、值不值得做、排序 | 能力四：优先级矩阵 |
| 竞争分析、竞品、替代方案、颠覆诊断 | 能力五：竞争分析 |
| 文案、营销、广告、落地页、VPC | 能力六：营销文案 |
| 增长、留存、流失、churn、ODI 策略 | 能力七：增长策略 |
| JTBD 描述、Job 描述、Outcome Statement | 能力八：JTBD 描述生成 |
| Job Map、Universal Job Map、八阶段 | 能力九：Job Map 构建 |
| Desired Outcome、成果管理 | 能力十：Outcome Statement 管理 |
| Job Stories、用户故事 | 能力十一：Job Stories 生成 |
| 采用障碍、使用障碍、obstacle | 能力十二：障碍诊断 |
| Jobs Atlas、七维度、全景图 | 能力十三：Jobs Atlas 构建 |
| 场景库、场景分析、JTBD 分析报告 | 综合运用全部能力 |
| 市场规模、TAM/SAM/SOM | CEO: 市场规模估算 |
| 优先级评分、资源分配 | CEO: 优先级评分 |
| 商业化、付费意愿、Go/No-Go | CEO: 商业化可行性 |
| 完整分析 + CEO 决策 | `analyze(include_ceo_analysis=True)` |

## 13 项执行能力

### 能力一：访谈提纲生成

支持 Switch（切换访谈）、ODI（成果驱动）、Churn（流失回溯）三种类型。从 6 个模块（挣扎时刻/竞争格局/推力拉力/焦虑惯性/进步验证/功能验证）组合生成结构化提纲。

```python
skill.generate_interview("用户访谈", ["competition", "push", "anxiety"])
skill.generate_interview("ODI访谈", interview_type="odi")
```

详见 `references/05-research-methods.md`。

### 能力二：调查问卷设计

支持筛选型/验证型/竞争型/ODI Outcome 配对量表/Job 评分五类问卷，输出完整问卷（题目+选项+跳转逻辑+预计时长）。

```python
skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])
skill.generate_survey("ODI量表", "odi_outcome", outcomes=["快速找到合适住处"])
```

详见 `references/05-research-methods.md`。

### 能力三：机会评分

**四维模型**：挣扎强度(30%)、替代方案满意度(25%)、市场规模(25%)、预算可获取性(20%)。
**ODI 双轨评分**：Opportunity = Importance + max(Importance - Satisfaction, 0)。

```python
skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)
skill.score_odi("快速找住处", importance=8, satisfaction=3)
```

详见 `references/06-analysis-framework.md` + `references/12-odi-methodology.md`。

### 能力四：优先级矩阵

对多个 Job 标准化描述、四力分析、机会评分（含 ODI），输出排序矩阵和行动建议。

```python
skill.add_job_to_matrix("快速找住处", struggle=4, alternative=3, market=4, budget=4,
                        importance=8, satisfaction=3)
matrix = skill.render_priority_matrix()
```

详见 `references/06-analysis-framework.md`。

### 能力五：竞争分析

识别直接竞品/间接竞品/非消费方案，支持 Outcome 对比和颠覆诊断（新进入者威胁评估）。

```python
skill.add_competitor("携程", "direct", strengths=["酒店多"], weaknesses=["界面复杂"])
skill.add_outcome_comparison("快速找到合适住处", 7, "携程", 5)
skill.add_disruption("新兴平台", disruptor_advantages=["AI推荐"], threat_level="high")
report = skill.render_competition()
```

详见 `references/08-business-decisions.md`。

### 能力六：营销文案生成

按挣扎共鸣→进步愿景→消除焦虑→克服惯性→行动号召结构生成，支持 VPC（Value Proposition Canvas）价值主张整合。

```python
skill.generate_marketing_copy(
    struggle="花30分钟比价", desired_outcome="专注工作",
    value_proposition="AI 一键推荐最优方案"
)
```

详见 `references/08-business-decisions.md`。

### 能力七：增长与留存策略

识别上游/下游/横向增长机会，按三种流失原因生成针对性策略。支持 ODI 五策略矩阵（Differentiated/Dominant/Discrete/Sustaining/Disruptive）和 7 种产品策略行动。

```python
skill.generate_growth_strategy(
    target_job="预订商务出行酒店",
    churn_segments=[("no_progress", "首周未预订", 200)],
    odi_strategy="differentiated", odi_rationale="高重要性低满意度"
)
```

详见 `references/08-business-decisions.md`。

### 能力八：JTBD 描述生成

支持四种描述格式：Klement（`[动作]+[挣扎]，这样我就能+[进步]`）、Outcome Statement（`[方向]+[指标]+[对象]+[条件]`）、Job Story（`When...I want to...So I can...`）、Traditional（`As a...I want to...So that...`）。

```python
skill.create_jtbd_statement("Help me", "快速找住处", "专注工作", statement_format="klement")
skill.create_outcome_statement(direction="minimize", metric="the time",
    obj="finding a suitable hotel", clarifier="when traveling for business")
```

详见 `references/06-analysis-framework.md`。

### 能力九：Universal Job Map 构建

Ulwick 八阶段 Job Map（Define → Locate → Prepare → Confirm → Execute → Monitor → Modify → Conclude），每阶段记录需求、重要性、满意度，自动识别高机会阶段。

```python
jm = skill.create_job_map("预订商务出行酒店")
jm.add_need("define", "确定出差日期和目的地", importance=9, satisfaction=7)
jm.add_need("locate", "搜索符合预算的酒店", importance=8, satisfaction=4)
result = jm.build()
```

详见 `references/12-odi-methodology.md`。

### 能力十：Desired Outcome Statement 管理

按 Ulwick 标准格式管理成果声明，支持 minimize/increase 方向、过程需求/情感需求/社会需求分类，自动生成优先级排序。

```python
ob = skill.create_outcome_statements("预订商务出行酒店")
ob.add_outcome("minimize", "the time it takes to", "find a suitable hotel",
               "when traveling for business", importance=9, satisfaction=3)
ob.add_outcome("minimize", "the likelihood of", "booking a hotel that doesn't match its photos",
               importance=8, satisfaction=4, need_type="emotional")
result = ob.build()
```

详见 `references/12-odi-methodology.md`。

### 能力十一：Job Stories 生成

支持四种变体：Classic（标准三段式）、Anxious（焦虑导向）、Force（四力聚焦）、Context-Rich（场景丰富），从不同视角捕捉同一 Job。

```python
js = skill.create_job_stories("预订商务出行酒店")
js.add_story("intercom", situation="出差需要住酒店",
             motivation="快速找到合适的住处", outcome="专注工作而不是为住宿烦恼")
js.add_story("kalbach", situation="到达酒店后很疲惫",
             motivation="快速办理入住", outcome="尽快休息",
             emotional_trigger="疲惫焦虑", emotional_reward="如释重负")
stories = js.build()
```

详见 `references/14-playbook-tools.md`。

### 能力十二：采用障碍诊断

从 Adoption（认知不足/价值不清/信任缺失/切换成本/复杂度）和 Usage（学习曲线/功能过载/性能/整合/支持）两大类诊断障碍，输出严重度评分和消除策略。

```python
diag = skill.diagnose_obstacles("旅行预订平台")
diag.add_obstacle("lack_of_knowledge", "用户不知道平台存在", severity=4)
diag.add_obstacle("behavior_change", "习惯使用老平台", severity=3)
diagnosis = diag.build()
```

详见 `references/14-playbook-tools.md`。

### 能力十三：Jobs Atlas 七维度构建

基于 Wunker 方法论的七维度 Job 全景图：Core Functional、Related、Emotional、Social、Financial、Consumption Chain、Context。包含 ABC Job Drivers（Attitude、Background、Circumstance）分析。

```python
atlas = skill.create_jobs_atlas("旅行预订平台")
atlas.set_core_job("出差时快速找到合适的住处")
atlas.add_related_job("管理差旅预算")
atlas.add_driver("circumstances", "紧急出差，时间紧迫", influence_level=4)
atlas.add_success_criterion("预订耗时", measurement="分钟", current_score=3, target_score=9)
result = atlas.build()
```

详见 `references/13-jobs-atlas.md`。

## CEO 决策视角

在 JTBD 分析完成后，可自动附加商业决策支持分析。当用户要求全面分析、深度分析，或涉及商业决策场景时，应自动设置 `include_ceo_analysis=True`。

### CEO 方法一：市场规模估算

基于 Job 数据推导 TAM/SAM/SOM，输出关键假设和分阶段验证计划（定性→定量→MVP→试点）。

**API:** `skill.generate_market_size_estimate(jobs)`

### CEO 方法二：优先级评分

综合重要性、满意度差距、置信度计算机会分，输出资源分配建议（P0/P1/P2 分层）和验证时间线。

**API:** `skill.generate_priority_scoring(jobs)`

### CEO 方法三：商业化可行性

评估付费意愿(WTP)、投入产出比(ROI)、回收期，输出 Go/No-Go 决策建议。

**API:** `skill.generate_commercialization_feasibility(jobs)`

### 一键生成

```python
result = skill.analyze(include_ceo_analysis=True)
# 标准分析报告 + 市场规模 + 优先级评分 + 商业化可行性
```

## Python 工具包

位于 `jtbd/` 目录，纯标准库实现，无外部依赖。版本 3.0.0。

| 模块 | 核心类/函数 | 用途 | 学派来源 |
|---|---|---|---|
| `__init__.py` | `JTBDSkill` | 统一 Facade 入口，封装全部 13 项能力 + CEO 方法 | 融合 |
| `jtbd_analyzer.py` | `JTBDAnalyzer` | JTBD 描述管理（四种格式）、四力分析、报告生成 | Klement |
| `interview_generator.py` | `InterviewBuilder` | Switch/ODI/Churn 三种访谈提纲生成 | Klement+Ulwick |
| `survey_generator.py` | `SurveyBuilder` | 五类问卷设计（含 ODI 配对量表） | Ulwick |
| `priority_calculator.py` | `PriorityAnalyzer` | 四维评分 + ODI Opportunity Algorithm | Klement+Ulwick |
| `competition.py` | `CompetitionAnalyzer` | 竞品分析 + Outcome 对比 + 颠覆诊断 | 融合 |
| `marketing.py` | `MarketingCopywriter` | 营销文案 + VPC 价值主张整合 | Kalbach |
| `growth.py` | `GrowthStrategyBuilder` | 增长策略 + ODI 五策略矩阵 + 7 产品策略 | Ulwick |
| `forces.py` | `ForcesProfile` | 推力/拉力/焦虑/惯性结构化分析 | Klement |
| `innovation.py` | `InnovationFinder` | 创新信号识别、补偿行为分析 | Klement |
| `job_map.py` | `JobMapBuilder` | Universal Job Map 八阶段构建 | Ulwick |
| `outcome_statement.py` | `OutcomeBuilder` | Desired Outcome Statement 管理 | Ulwick |
| `job_stories.py` | `JobStoryBuilder` | Job Stories 四种变体生成 | Kalbach |
| `obstacles.py` | `ObstacleAnalyzer` | 采用/使用障碍诊断与消除策略 | Wunker |
| `jobs_atlas.py` | `JobsAtlasBuilder` | Jobs Atlas 七维度全景图 + ABC Drivers | Wunker |
| `config.py` | `AnalysisConfig` | 运行时配置：分析维度、输出格式 | — |
| `templates.py` | 模板常量 | 访谈问题、报告模板、分析框架 | — |
| `utils.py` | `load_knowledge`, `search_knowledge` | 知识库加载与搜索 | — |

### 快速使用

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDSkill

skill = JTBDSkill("在线旅行预订平台")

# 基础分析
guide = skill.generate_interview("用户访谈", ["competition", "push"])
survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])

# ODI 分析
odi = skill.score_odi("快速找住处", importance=8, satisfaction=3)
jm = skill.create_job_map("预订商务出行酒店")

# Atlas 分析
atlas = skill.create_jobs_atlas("预订商务出行酒店")
obstacles = skill.diagnose_obstacles("旅行预订平台")

# 完整报告（含 CEO 决策）
report = skill.analyze(include_ceo_analysis=True)

# 知识库搜索
from jtbd import search_knowledge
results = search_knowledge("焦虑")
```

## 知识库索引

所有文档位于 `references/` 目录（共 15 篇）：

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
| `12-odi-methodology.md` | ODI 方法论 | Ulwick Opportunity Algorithm、Job Map、Outcome Statement |
| `13-jobs-atlas.md` | Jobs Atlas | Wunker 七维度分析、ABC Drivers、全景图构建 |
| `14-playbook-tools.md` | 实战工具箱 | Job Stories 模板、障碍检查清单、研讨会引导 |
| `15-glossary.md` | 术语表 | 四大学派核心术语中英对照 |

## AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 优先通过 `JTBDSkill` Facade 调用，亦可直接使用子类（JTBDAnalyzer / InterviewBuilder 等） |
| 2 | **返回值** | 所有方法返回 Markdown 字符串（Builder 类需先 `.build()` 再 `.render_markdown()`） |
| 3 | **触发映射** | 根据用户意图选择对应能力（参见触发条件表），模糊意图时优先执行能力九全流程 |
| 4 | **四力优先** | 任何分析先进行四力（推力/拉力/焦虑/惯性）分析，这是 JTBD 的基石 |
| 5 | **学派匹配** | 用户提及 ODI/Outcome/Job Map 时使用 Ulwick 工具，提及 Atlas/障碍时使用 Wunker 工具 |
| 6 | **知识优先** | 理论问题先调用 `search_knowledge()` 查询知识库 |
| 7 | **CEO 决策默认附加** | 全面分析或涉及商业决策时，自动使用 `include_ceo_analysis=True` |
| 8 | **完整交付** | 每个任务产出完整可用的分析/报告/建议，不留半成品 |
| 9 | **格式灵活** | 能力八支持四种描述格式，根据上下文选择最合适的格式 |
