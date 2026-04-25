# JTBD Knowledge Skill v3.0

> 融合 Klement · Ulwick ODI · Wunker Jobs Atlas · Kalbach 四大学派的 JTBD 理论与执行工具包。
> 15 篇结构化知识库 + 18 个 Python 模块 + 13 项可执行能力，覆盖从用户研究到商业决策的完整 JTBD 工作流。

## 四大理论来源

| 学派 | 代表著作 | 核心贡献 |
|------|---------|---------|
| **Klement** | *When Coffee and Kale Compete* | 进步力量模型、切换访谈、情感分析、补偿行为识别 |
| **Ulwick ODI** | *Jobs to Be Done: Theory to Practice* | Opportunity Algorithm、Desired Outcome Statement、Universal Job Map |
| **Wunker Atlas** | *Jobs to Be Done: A Roadmap* | 七维度 Jobs Atlas、ABC Job Drivers、采用/使用障碍诊断 |
| **Kalbach** | *The Jobs to Be Done Playbook* | Job Stories 四变体、VPC 价值主张整合、多工具协同 |

## 13 项执行能力

| # | 能力 | 模块 | 说明 |
|---|------|------|------|
| 1 | 访谈提纲 | `InterviewBuilder` | Switch / ODI / Churn 三种类型，10 个维度 |
| 2 | 调查问卷 | `SurveyBuilder` | 筛选 / 验证 / 满意度 / ODI 配对量表 / Job 评分 |
| 3 | 机会评分 | `PriorityAnalyzer` | 四维模型 + ODI Opportunity Algorithm 双轨 |
| 4 | 优先级矩阵 | `PriorityMatrix` | 多 Job 排序、力量叠加、策略建议 |
| 5 | 竞争分析 | `CompetitionAnalyzer` | Outcome 对比、颠覆诊断、Right to Win |
| 6 | 营销文案 | `MarketingCopywriter` | 四力驱动文案 + VPC 价值主张陈述 |
| 7 | 增长策略 | `GrowthStrategyBuilder` | ODI 五策略矩阵、七种产品策略行动 |
| 8 | JTBD 描述 | `JTBDAnalyzer` | Klement / Outcome / Job Story / Traditional 四格式 |
| 9 | Job Map | `JobMapBuilder` | Universal Job Map 8 阶段分解 |
| 10 | Outcome 管理 | `OutcomeBuilder` | Desired Outcome Statement 四元素格式 |
| 11 | Job Stories | `JobStoryBuilder` | Intercom / Kalbach / Hill / Troeth 四变体 |
| 12 | 障碍诊断 | `ObstacleAnalyzer` | 6 种采用障碍 + 4 种使用障碍 + 对策 |
| 13 | Jobs Atlas | `JobsAtlasBuilder` | 七维度引导式构建，ABC Drivers，完成度检查 |

## 快速开始

```python
from jtbd import JTBDSkill

skill = JTBDSkill("旅行预订平台")
```

### 访谈与问卷

```python
guide = skill.generate_interview("用户访谈", ["competition", "push", "anxiety"])

odi_guide = skill.generate_interview("ODI访谈", interview_type="odi")

survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])
```

### 机会评分

```python
score = skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)
# {'score': 3.75, 'level': '中等机会', 'action': '值得验证...'}

odi = skill.score_odi("快速找住处", importance=8, satisfaction=3)
# {'odi_score': 13.0, 'odi_level': '未被充分满足', 'suggested_strategy': 'differentiated'}
```

### Universal Job Map

```python
jm = skill.create_job_map("预订商务出行酒店", executor="商务旅客")
jm.add_need("define", "确定出差日期和目的地", importance=9, satisfaction=7)
jm.add_need("locate", "搜索符合差旅标准的酒店", importance=8, satisfaction=3)
jm.add_pain_point("locate", "需要在多个平台反复比较")
job_map = jm.build()
print(JobMapBuilder.render_markdown(job_map))
```

### Desired Outcome Statement

```python
ob = skill.create_outcome_statements("预订商务出行酒店")
ob.add_outcome(
    direction="minimize", metric="the time it takes to",
    object_of_control="find a hotel that meets company travel standards",
    clarifier="when booking for business trips",
    importance=9, satisfaction=3,
    job_map_stage="locate",
)
outcome_set = ob.build()
print(OutcomeBuilder.render_markdown(outcome_set))
```

### Job Stories

```python
js = skill.create_job_stories("预订商务出行酒店")
js.add_story(
    story_format="intercom",
    situation="出差需要住酒店",
    motivation="快速找到合适的住处",
    outcome="专注工作而不是为住宿烦恼",
)
js.add_story(
    story_format="kalbach",
    situation="临时接到出差通知",
    motivation="快速预订符合差旅标准的酒店",
    outcome="不用担心报销问题",
    emotional_trigger="时间紧迫带来的焦虑",
    emotional_reward="一切搞定的安心感",
)
stories = js.build()
print(JobStoryBuilder.render_markdown(stories))
```

### 障碍诊断

```python
diag = skill.diagnose_obstacles()
diag.set_target_job("快速找到合适的商务酒店")
diag.add_obstacle("lack_of_knowledge", "用户不知道平台有商旅专属功能", severity=4)
diag.add_obstacle("behavior_change", "已习惯使用携程", severity=3)
diag.add_inertia_strategy("lower_trial_barriers")
diag.add_inertia_strategy("social_proof")
diagnosis = diag.build()
print(ObstacleAnalyzer.render_markdown(diagnosis))
```

### Jobs Atlas

```python
atlas = skill.create_jobs_atlas("旅行预订平台")
atlas.set_core_job("快速找到合适的商务酒店")
atlas.add_driver("circumstances", "临时出差通知，时间紧迫", influence_level=5)
atlas.add_driver("background", "每月出差2-3次的商务人士", influence_level=4)
atlas.add_current_approach("携程", pain_points=["界面复杂", "价格不透明"])
atlas.add_success_criterion("5分钟内完成预订", priority=5)
atlas.add_obstacle("不知道平台有商旅功能")
atlas.add_value("functional", "一站式比价节省时间", magnitude=4)
atlas.add_competitor("携程", job_overlap="商务酒店预订", threat_level=4)
atlas_result = atlas.build()
print(JobsAtlasBuilder.render_markdown(atlas_result))
```

### 竞争分析

```python
skill.add_competitor("携程", "direct", strengths=["酒店多"], weaknesses=["界面复杂"])
skill.add_outcome_comparison("最小化找酒店时间", 7, "携程", 5)
skill.add_disruption("AI旅行助手", disruptor_advantages=["智能推荐"], threat_level="medium")
print(skill.render_competition())
```

### 营销文案

```python
copy = skill.generate_marketing_copy(
    struggle="每次出差花30分钟比价",
    desired_outcome="专注工作不为住宿烦恼",
    executor="商务出差人群",
    current_approach="手动在多个平台比价",
    value_proposition="一站式智能比价推荐",
)
```

### 增长策略

```python
growth = skill.generate_growth_strategy(
    target_job="帮我快速找到合适的住处",
    odi_strategy="differentiated",
    odi_rationale="多个Outcome未满足，聚焦差异化",
    churn_segments=[("no_progress", "首周未完成预订的用户", 200)],
    key_habits=[("完成首次预订", 85, 20, "首周")],
)
```

### 知识库

```python
from jtbd import load_knowledge, search_knowledge

content = load_knowledge("odi")       # ODI 方法论
content = load_knowledge("atlas")     # Jobs Atlas 框架
content = load_knowledge("glossary")  # 50+ JTBD 术语

results = search_knowledge("焦虑")    # 跨知识库关键词搜索
```

## 文件结构

```
jtbd-knowledge-skill/
├── SKILL.md                         # Skill 定义（13 项执行能力）
├── README.md
├── pyproject.toml
│
├── jtbd/                            # Python 包（零外部依赖）
│   ├── __init__.py                  # v3.0 统一入口，JTBDSkill 类
│   ├── config.py                    # 全局配置与常量
│   ├── utils.py                     # 知识库加载与文本工具
│   ├── templates.py                 # 模板定义
│   │
│   ├── jtbd_analyzer.py             # JTBD 分析引擎（四格式描述）
│   ├── interview_generator.py       # 访谈提纲（Switch/ODI/Churn）
│   ├── survey_generator.py          # 问卷生成（5 种类型）
│   ├── priority_calculator.py       # 机会评分（四维 + ODI 双轨）
│   ├── forces.py                    # 进步力量分析
│   ├── innovation.py                # 创新信号识别
│   ├── competition.py               # 竞争分析（Outcome 对比）
│   ├── marketing.py                 # 营销文案（VPC 价值主张）
│   ├── growth.py                    # 增长策略（ODI 五策略）
│   │
│   ├── job_map.py                   # Universal Job Map（8 阶段）
│   ├── outcome_statement.py         # Desired Outcome Statement
│   ├── job_stories.py               # Job Stories（4 种变体）
│   ├── obstacles.py                 # 采用障碍诊断（10 种障碍）
│   ├── jobs_atlas.py                # Jobs Atlas（七维度）
│   │
│   └── tests/
│       └── test_all.py              # 26 个测试函数
│
└── references/                      # 15 篇知识库
    ├── 01-theory-foundation.md
    ├── 02-principles.md
    ├── 03-forces-of-progress.md
    ├── 04-system-of-progress.md
    ├── 05-research-methods.md
    ├── 06-analysis-framework.md
    ├── 07-innovation-guide.md
    ├── 08-business-decisions.md
    ├── 09-case-studies.md
    ├── 10-two-models.md
    ├── 11-quick-reference.md
    ├── 12-odi-methodology.md        # v3.0 新增
    ├── 13-jobs-atlas.md             # v3.0 新增
    ├── 14-playbook-tools.md         # v3.0 新增
    └── 15-glossary.md               # v3.0 新增
```

## 技术规格

纯 Python 标准库，零外部依赖，兼容 Python 3.8+。所有模块支持 Markdown 和 JSON 双格式输出，采用 Builder 模式 API 和 `@dataclass` 数据结构。

## 版本

| 版本 | 变更 |
|------|------|
| **v3.0.0** | 融合四大学派，新增 Job Map / Outcome / Job Stories / 障碍诊断 / Jobs Atlas 五模块，增强全部现有模块，新增 4 篇知识库 |
| **v2.0.0** | Python 工具包：8 大执行能力，统一入口 JTBDSkill 类 |
| **v1.0.0** | 基础版：知识库 + 分析引擎 |
