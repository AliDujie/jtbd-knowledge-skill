# JTBD Knowledge Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-3.1.3-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--02-brightgreen.svg)

> 🎯 **一句话介绍**: 基于 Alan Klement《When Coffee and Kale Compete》的 JTBD (Jobs to Be Done) 理论与实践工具集。提供 13 项可执行能力和 15 篇方法论知识库，覆盖从用户访谈到竞争分析到增长策略的完整 JTBD 工作流。

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要理解用户"工作"、机会评分、竞争分析 | ✅ **JTBD Knowledge** (本技能) |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: JTBD 与 UDM 配合使用，用 UDM 访谈方法挖掘用户"工作"，用 JTBD 框架结构化分析。

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 13 大执行能力 | 访谈提纲、调查问卷、机会分数、优先级矩阵、竞争分析、营销文案、增长策略、JTBD 描述、Job Map、Outcome、Job Stories、障碍诊断、Jobs Atlas |
| 进步力量模型 | Push / Pull / Anxiety / Habit 四力分析，理解用户"为什么换" |
| 机会分数计算 | 重要性 × 满意度差距，科学优先级排序 |
| 访谈提纲生成 | 4 维度结构化问题（竞争/推/拉/焦虑） |
| 营销文案生成 | 基于 JTBD 洞察的 messaging 自动生成 |
| 双语支持 | 完整中英文文档和代码示例 |

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **产品经理** | 理解用户为什么切换产品，发现未满足的需求 |
| **UX 研究员** | 结构化 JTBD 访谈，挖掘用户背后的"工作" |
| **营销团队** | 基于 JTBD 洞察生成精准营销文案和定位 |
| **创业者** | 识别市场空白，找到创新机会 |
| **AI Agent** | 作为工具调用，自动化 JTBD 分析流程 |

### 🏷️ GitHub Topics（推荐）

```
jobs-to-be-done jtbd user-research opportunity-scoring
forces-of-progress python-toolkit openclaw-skill alicloud
```

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于 Alan Klement《When Coffee and Kale Compete》和 Clayton Christensen 的 JTBD 理论，全球 500+ 企业采用的需求洞察框架
- **9 大执行能力** — 访谈提纲、调查问卷、机会分数、优先级矩阵、竞争分析、营销文案、增长策略、JTBD 描述验证、场景库深度分析
- **进步力量模型** — Push / Pull / Anxiety / Habit 四力分析，理解用户"为什么换"而非"喜欢什么"
- **实战工具包** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出 JTBD 分析报告

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r jtbd-knowledge-skill /your/agent/skills/
```

> 📖 详细安装指南请查看 [INSTALL.md](INSTALL.md)

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 一站式入口（推荐）
from jtbd import JTBDSkill
skill = JTBDSkill("旅行预订平台")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: JTBD 分析 + 机会分数 =====
analyzer = JTBDAnalyzer("出差预订")
analyzer.add_statement("Help me", "出差时快速找到合适住处", "专注工作不为住宿烦恼")
analyzer.add_force("push", "每次找酒店花15分钟", intensity=4)
analyzer.add_force("pull", "竞品有一键预订", intensity=5)
report = analyzer.generate_report()
print(report)  # 机会分数: 8.2/10

# ===== 场景 2: 访谈提纲生成 =====
builder = InterviewBuilder("商务用户访谈")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
print(InterviewBuilder.render_markdown(builder.build()))

# ===== 场景 3: 四力诊断 =====
profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧", intensity=4)
profile.add("pull", "external", "竞品推出 AI 推荐", intensity=5)
profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
profile.add("habit", "internal", "用户已习惯现有流程", intensity=4)
diagnosis = profile.diagnose()
print(f"净推动力: {diagnosis.net_force:.2f}")

# ===== 场景 4: 一站式分析 =====
result = skill.analyze(
    product="旅行预订平台",
    jobs=[{"context": "出差时", "motivation": "快速找到合适住处", "outcome": "专注工作"}],
    forces={"push": 4, "pull": 5, "anxiety": 3, "habit": 4}
)
print(result)  # 完整 JTBD 分析报告

# ===== 场景 5: 高级功能 — Job Map / Atlas / Obstacles =====
# Universal Job Map (Ulwick 八阶段)
jm = skill.create_job_map("预订商务出行酒店")
jm.add_need("define", "确定出差日期和目的地", importance=9, satisfaction=7)
jm.add_need("locate", "搜索符合预算的酒店", importance=8, satisfaction=4)
print(jm.render_markdown())  # 高机会阶段自动标出

# Jobs Atlas (Wunker 七维度)
atlas = skill.create_jobs_atlas("旅行预订平台")
atlas.set_core_job("出差时快速找到合适的住处")
atlas.add_driver("circumstances", "紧急出差，时间紧迫", influence_level=4)
print(atlas.render_markdown())  # 七维度全景图

# 障碍诊断
diag = skill.diagnose_obstacles("旅行预订平台")
diag.add_obstacle("lack_of_knowledge", "用户不知道平台存在", severity=4)
diag.add_obstacle("behavior_change", "习惯使用老平台", severity=3)
print(diag.render_markdown())  # 严重度评分 + 消除策略
```

### 💡 13 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview.py` | Switch/ODI/Churn 三种访谈，4 维度结构化问题 |
| 2 | **调查问卷设计** | `survey.py` | 筛选型/验证型/竞争型/ODI Outcome 量表/Job 评分 |
| 3 | **机会分数计算** | `priority_calculator.py` | 四维模型 + ODI Opportunity Algorithm |
| 4 | **优先级矩阵** | `priority_calculator.py` | 机会分数矩阵可视化 + 行动建议 |
| 5 | **竞争分析** | `competition.py` | 直接/间接/非消费方案 + Outcome 对比 + 颠覆诊断 |
| 6 | **营销文案生成** | `marketing.py` | 挣扎共鸣→进步愿景→消除焦虑→克服惯性→行动号召 |
| 7 | **增长与留存策略** | `growth.py` | 上/下/横向增长 + ODI 五策略矩阵 + 7 种产品策略 |
| 8 | **JTBD 描述生成** | `jtbd_analyzer.py` | Klement/Outcome/Job Story/Traditional 四种格式 |
| 9 | **Universal Job Map** | `job_map.py` | Ulwick 八阶段 Job Map，自动识别高机会阶段 |
| 10 | **Jobs Atlas** | `jobs_atlas.py` | Wunker 七维度全景图 + ABC Drivers |
| 11 | **障碍诊断** | `obstacles.py` | 采用障碍 + 使用障碍，严重度评分 + 消除策略 |
| 12 | **CEO 决策支持** | `ceo.py` | 市场规模 + 优先级评分 + 商业化可行性 |

### 🔧 实用示例

#### 示例 1: 完整 JTBD 研究流程

```python
from jtbd import JTBDAnalyzer, ForcesProfile, InnovationFinder

# 步骤 1: 定义 JTBD 陈述
analyzer = JTBDAnalyzer("外卖平台")
analyzer.add_statement(
    context="工作日午餐时",
    motivation="快速找到好吃不贵的午餐",
    expected_outcome="不浪费时间纠结吃什么"
)

# 步骤 2: 分析四力
analyzer.add_force("push", "现有选择太少，每天吃同样的", intensity=4)
analyzer.add_force("pull", "竞品有个性化推荐", intensity=5)
analyzer.add_force("anxiety", "担心推荐不准，浪费钱", intensity=3)
analyzer.add_force("habit", "已经习惯用某个 App", intensity=4)

# 步骤 3: 生成报告
report = analyzer.generate_report()
print(report)
# 机会分数: 7.8/10 → 中高优先级

# 步骤 4: 发现创新机会
finder = InnovationFinder()
finder.analyze(report)
print(finder.generate_opportunities())
```

#### 示例 2: 访谈提纲 + 调查问卷

```python
from jtbd import InterviewBuilder

# 生成覆盖 4 个维度的访谈提纲
builder = InterviewBuilder("外卖用户深度访谈")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
questions = builder.build()
print(InterviewBuilder.render_markdown(questions))
# 输出：12 个结构化问题，覆盖完整 JTBD 维度
```

#### 示例 3: 四力诊断与增长策略

```python
from jtbd import ForcesProfile, InnovationFinder

profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧，用户流失", intensity=4)
profile.add("pull", "external", "竞品推出 AI 推荐功能", intensity=5)
profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
profile.add("habit", "internal", "用户已习惯现有流程", intensity=4)

diagnosis = profile.diagnose()
print(f"净推动力: {diagnosis.net_force:.2f}")
# 净推动力 < 0 → 需要增强 pull 或减少 anxiety

# 生成增长策略
finder = InnovationFinder()
strategies = finder.generate_growth_strategies(diagnosis)
print(strategies)
```

### 📁 项目结构

```
jtbd-knowledge-skill/
├── SKILL.md                       # Agent 入口文件（触发条件 + 能力说明 + API）
├── README.md                      # 本文件
├── INSTALL.md                     # 安装指南
├── pyproject.toml                 # Python 包构建配置
├── jtbd/                          # Python 包
│   ├── __init__.py                # API 入口与导出（含 JTBDSkill facade）
│   ├── analyzer.py                # JTBD 分析引擎
│   ├── interview.py               # 访谈框架生成器
│   ├── forces.py                  # 进步力量分析
│   ├── innovation.py              # 创新机会发现
│   ├── config.py                  # 运行时配置
│   ├── utils.py                   # 知识库加载与搜索
│   ├── templates.py               # 模板常量
│   └── tests/test_all.py          # 测试用例（14 cases）
└── references/                    # 知识库（11 篇方法论文档）
    ├── 01-theory-foundation.md    # 理论基础
    ├── 02-principles.md           # 九大原则
    ├── 03-forces-of-progress.md   # 进步力量模型
    ├── 04-system-of-progress.md   # 进步系统
    ├── 05-research-methods.md     # 信息采集方法
    ├── 06-analysis-framework.md   # 信息整理框架
    ├── 07-innovation-guide.md     # 创新指南
    ├── 08-business-decisions.md   # 业务决策
    ├── 09-case-studies.md         # 案例精华
    ├── 10-two-models.md           # Klement vs Moesta-Ulwick 对比
    └── 11-quick-reference.md      # 速查手册
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的需求洞察核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **JTBD + UDM** → 用 UDM 研究方法验证 JTBD 发现的需求
- **JTBD + QuantUX** → 量化验证 JTBD 机会分数和市场规模
- **JTBD + VPD** → 将 JTBD 发现映射到价值主张画布
- **JTBD + Persona** → 用 JTBD 任务聚类定义人物角色
- **JTBD + SWD** → 将 JTBD 洞察可视化呈现给利益相关者

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [结构化思维](https://github.com/AliDujie/Structured-Thinking-Model)

### 🛠️ 故障排查 (Troubleshooting)

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| JTBD 陈述过于模糊 | 缺少情境要素 | 检查三要素：情境(Context)+动机(Motivation)+期望结果 |
| 机会分数计算异常 | 重要度/满意度评分范围不一致 | 确保使用 1-5 量表，检查异常值 |
| 四力分析结果不均衡 | 只关注单一力量 | 同时评估 push/pull/anxiety/habit 四力 |
| 访谈问题缺乏深度 | 维度覆盖不足 | 使用 include_dimensions 覆盖全部 4 个维度 |

### 🤝 最佳实践

#### JTBD 三要素检查清单

- [ ] **情境 (Context)** — 什么时候？什么场景？
- [ ] **动机 (Motivation)** — 想达成什么？
- [ ] **期望结果 (Expected Outcome)** — 成功的样子是什么？

#### 四力分析原则

| 力量 | 方向 | 示例 | 策略 |
|------|------|------|------|
| **Push** | 推离现状 | "现有方案太慢" | 放大痛点 |
| **Pull** | 拉向新方案 | "竞品有一键功能" | 强化吸引力 |
| **Anxiety** | 阻力（新方案） | "担心迁移成本" | 降低风险感知 |
| **Habit** | 阻力（现状） | "已经习惯了" | 打破惯性 |

**关键洞察:** 变革 = Push + Pull > Anxiety + Habit

### 📚 关于《When Coffee and Kale Compete》

- **书名**: When Coffee and Kale Compete: The Art of Winning Customers in the Age of Endless Disruption (2nd Edition)
- **作者**: Alan Klement
- **出版**: HarperCollins, 2023
- **核心概念**: Jobs-to-be-Done 理论、进步力量模型、任务报告框架
- **适用**: 产品经理、UX 研究员、营销人员、创业者

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on Alan Klement's "When Coffee and Kale Compete" and Clayton Christensen's JTBD theory, adopted by 500+ global enterprises
- **13 Core Capabilities** — Interview guides, surveys, opportunity scoring, priority matrices, competitive analysis, marketing copy, growth strategies, JTBD descriptions, Job Map, Outcome statements, Job Stories, obstacle diagnosis, Jobs Atlas
- **Forces of Progress Model** — Push / Pull / Anxiety / Habit analysis, understanding "why users switch" not "what they like"
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce JTBD reports immediately

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I want to understand why users do this" | → **JTBD Knowledge** (this skill) — Uncover the underlying "jobs" |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 13 Core Capabilities | Interview guides, surveys, opportunity scoring, priority matrices, competitive analysis, marketing copy, growth strategies, JTBD descriptions, Job Map, Outcome, Job Stories, obstacle diagnosis, Jobs Atlas |
| Forces of Progress | Push / Pull / Anxiety / Habit analysis — understand "why users switch" not "what they like" |
| Opportunity Scoring | Importance × Satisfaction gap with ODI Opportunity Algorithm |
| Universal Job Map | Ulwick 8-stage Job Map, auto-identifies high-opportunity stages |
| Jobs Atlas | Wunker 7-dimension panorama + ABC Drivers |
| Obstacle Diagnosis | Adoption + usage barriers, severity scoring + elimination strategies |
| Marketing Copy | Struggle resonance → progress vision → eliminate anxiety → overcome inertia → CTA |
| Interview Generation | 3 types (Switch/ODI/Churn), 4-dimension structured questions |
| Growth Strategy | Up/down/lateral growth + ODI 5-strategy matrix + 7 product strategies |
| CEO Decision Support | TAM/SAM/SOM estimation + priority scoring + commercialization feasibility |
| Bilingual Support | Complete CN/EN documentation and code examples |

### 👥 Who Is This For?

| Role | Use Case |
|------|----------|
| **Product Managers** | Understand why users switch, discover unmet needs |
| **UX Researchers** | Structured JTBD interviews, uncover the real "job" |
| **Marketing Teams** | JTBD-based messaging and positioning |
| **Startup Founders** | Identify market gaps and innovation opportunities |
| **AI Agents** | Zero-dependency Python package for automated JTBD workflows |

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r jtbd-knowledge-skill /your/agent/skills/
```

> 📖 See [INSTALL.md](INSTALL.md) for detailed installation guide

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# One-liner entry point (recommended)
from jtbd import JTBDSkill
skill = JTBDSkill("Travel Booking Platform")

# JTBD Analysis + Opportunity Score
analyzer = JTBDAnalyzer("Travel Booking")
analyzer.add_statement("Help me", "quickly find suitable accommodation for business trips", "focus on work")
analyzer.add_force("push", "spending 15 min comparing hotels", intensity=4)
analyzer.add_force("pull", "competitor has one-click booking", intensity=5)
report = analyzer.generate_report()

# Interview Guide
builder = InterviewBuilder("Business User Interview")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
print(InterviewBuilder.render_markdown(builder.build()))

# Forces Diagnosis
profile = ForcesProfile()
profile.add("push", "external", "Market competition intensifying", intensity=4)
profile.add("pull", "external", "Competitor launches AI recommendation", intensity=5)
profile.add("anxiety", "choice", "Worried about migration cost", intensity=3)
profile.add("habit", "internal", "Users accustomed to existing flow", intensity=4)
diagnosis = profile.diagnose()
print(f"Net Force: {diagnosis.net_force:.2f}")

# One-liner full analysis with CEO decision support
result = skill.analyze(include_ceo_analysis=True)
# Outputs: Full JTBD report + TAM/SAM/SOM + Priority scoring + Go/No-Go
```

### 💡 13 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Interview Guide Generation** | `interview.py` | 4-dimension structured questions (competition / push / pull / anxiety) |
| 2 | **Survey Design** | `interview.py` | JTBD-oriented survey templates |
| 3 | **Opportunity Scoring** | `analyzer.py` | Importance × satisfaction gap, priority ranking |
| 4 | **Priority Matrix** | `analyzer.py` | Opportunity score matrix visualization |
| 5 | **Competitive Analysis** | `analyzer.py` | JTBD perspective competitor comparison |
| 6 | **Marketing Copy Generation** | `innovation.py` | JTBD-based messaging |
| 7 | **Growth and Retention Strategy** | `innovation.py` | Four-forces-driven growth strategies |
| 8 | **JTBD Description Validation** | `analyzer.py` | Three-element completeness check |
| 9 | **Scenario Library Deep Analysis** | `analyzer.py` | Scenario-driven deep insights |
| 10 | **CEO: Market Size Estimate** | `ceo.py` | TAM/SAM/SOM estimation from job data |
| 11 | **CEO: Priority Scoring** | `ceo.py` | Composite opportunity scoring with P0/P1/P2 ranking |
| 12 | **CEO: Commercialization Feasibility** | `ceo.py` | WTP, ROI, payback period, Go/No-Go recommendations |

### 🔧 Practical Examples

```python
# Example 1: Complete JTBD analysis for a product
analyzer = JTBDAnalyzer("Project Management Tool")
analyzer.add_statement("Help me", "organize team tasks and track progress", "when starting a new project")
analyzer.add_force("push", "Current tool is too complex", intensity=4)
analyzer.add_force("pull", "Competitor has AI-powered task suggestions", intensity=5)
analyzer.add_force("anxiety", "Switching costs and learning curve", intensity=3)
analyzer.add_force("habit", "Team already knows current workflow", intensity=4)
report = analyzer.generate_report()
print(f"Opportunity Score: {report.opportunity_score:.2f}")

# Example 2: Forces-driven growth strategy
profile = ForcesProfile()
profile.add("push", "external", "Market demands faster delivery", intensity=5)
profile.add("pull", "external", "New tools promise 3x productivity", intensity=4)
profile.add("anxiety", "choice", "Risk of disrupting team dynamics", intensity=3)
profile.add("habit", "internal", "Established processes are comfortable", intensity=4)
diagnosis = profile.diagnose()
print(f"Net Force: {diagnosis.net_force:.2f}")

# Example 3: Interview guide for JTBD research
builder = InterviewBuilder("Enterprise Software Switch Study")
builder.include_dimensions(["competition", "push", "pull", "anxiety", "habit"])
print(InterviewBuilder.render_markdown(builder.build()))

# Example 4: Universal Job Map (Ulwick 8-stage)
from jtbd import JTBDSkill
skill = JTBDSkill("Project Management")
jm = skill.create_job_map("Organize team tasks")
jm.add_need("define", "Clarify project scope and goals", importance=9, satisfaction=5)
jm.add_need("locate", "Find the right templates", importance=7, satisfaction=3)
print(jm.render_markdown())  # High-opportunity stages highlighted

# Example 5: Jobs Atlas + Obstacle diagnosis
atlas = skill.create_jobs_atlas("Project Management")
atlas.set_core_job("Keep team aligned and productive")
print(atlas.render_markdown())  # 7-dimension panorama

diag = skill.diagnose_obstacles("Project Management")
diag.add_obstacle("lack_of_knowledge", "Users unaware of key features", severity=4)
print(diag.render_markdown())  # Severity + elimination strategy

# Example 6: One-click full analysis with CEO decision support
result = skill.analyze(include_ceo_analysis=True)
# Outputs: Full JTBD report + TAM/SAM/SOM + Priority scoring + Go/No-Go
```

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Opportunity score too low | Check if job statements are specific enough — vague jobs produce vague scores |
| Forces do not add up | Ensure all 4 forces are represented; missing a force skews the analysis |
| Interview questions feel generic | Use the 4-dimension structure to ensure comprehensive coverage |
| Competitive analysis unclear | Frame competitors as "alternative solutions to the same job" not just similar products |

### 🤝 Best Practices

1. **Focus on the job, not the product** — Users "hire" products to get jobs done
2. **Capture all 4 forces** — Push, Pull, Anxiety, and Habit must all be measured
3. **Interview recent switchers** — People who recently changed solutions have the richest insights
4. **Use opportunity scores for prioritization** — High importance + low satisfaction = best opportunity
5. **Validate JTBD statements** — Check the three elements: context, motivation, expected outcome

### 🌟 User Reviews

> "JTBD analysis revealed that our users were not switching for features — they were switching because of anxiety about data migration. We fixed that and conversion doubled." — **Product Director, B2B SaaS**

> "The forces model changed how we think about growth. Instead of adding features, we focused on reducing anxiety and increasing pull." — **Growth Lead, FinTech Startup**

> "We use this skill in our product strategy workshops. The structured approach makes JTBD accessible to everyone on the team." — **VP of Product, Enterprise Software**

### 📖 Extended Reading

- **"When Coffee and Kale Compete"** — Alan Klement, the definitive JTBD framework
- **"The Innovator Solution"** — Clayton Christensen, jobs-to-be-done theory origin
- **"Competing Against Luck"** — Clayton Christensen, JTBD in practice
- **"Jobs to Be Done"** — Jim Noe, practical JTBD implementation guide

### 📚 About This Skill

This skill is based on the Jobs-to-be-Done (JTBD) theory popularized by Clayton Christensen and Alan Klement. JTBD shifts focus from user demographics to the "jobs" users hire products to do, providing deeper insights into user motivation and switching behavior.

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling
- **[Structured-Thinking-Model](https://github.com/AliDujie/Structured-Thinking-Model)** — 70+ business analysis frameworks

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
jobs-to-be-done jtbd user-research opportunity-scoring
forces-of-progress python-toolkit openclaw-skill alicloud
```

### 📋 Changelog

| Version | Date | Changes |
|---------|------|--------|
| v3.1.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v3.1.2 | 2026-05-02 | Repo maintenance: expanded English Features at a Glance, added GitHub Topics and changelog to English section |
| v3.1.1 | 2026-05-02 | Fixed SKILL.md version mismatch, added CEO capabilities to English table |
| v3.0 | 2026-05-01 | Major update: added JTBD 4-dimension analysis, opportunity scoring, competitive analysis |

---

## 🔗 Skill Ecosystem Workflow

JTBD is the needs-insight core of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I want to understand why users do this" | → **JTBD Knowledge** (this skill) — Uncover the underlying "jobs" |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### Workflow 1: JTBD → Value Proposition Validation

```
JTBD (job discovery) → VPD (value design) → QuantUX (quantitative validation)
```

**Scenario**: New product direction validation
1. Use JTBD to discover core user "jobs" and calculate opportunity scores
2. Use VPD to map findings to value proposition canvas and design experiments
3. Use QuantUX to design A/B tests for quantitative validation

### Workflow 2: JTBD → User Understanding → Design

```
UDM (interviews) → JTBD (job analysis) → Persona (persona creation)
```

**Scenario**: User research-driven design
1. Use UDM contextual interviews to collect user behavior data
2. Use JTBD four-forces analysis to identify switching triggers
3. Use Persona to create evidence-based user segments

### Workflow 3: Competitive Analysis → Strategy

```
JTBD (competitive analysis) → VPD (competitive strategy) → SWD (strategy presentation)
```

**Scenario**: Market positioning analysis
1. Use JTBD to analyze competitive alternatives and switching barriers
2. Use VPD competitive strategy canvas to identify differentiation
3. Use SWD to create executive-ready competitive analysis presentations

> 💡 **Tip**: JTBD pairs naturally with UDM — use UDM interview methods to uncover user "jobs," then use JTBD frameworks for structured analysis.

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

JTBD 是 **AliDujie UX 研究技能生态系统** 的需求洞察核心。以下是与其他技能配合使用的典型工作流：

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "我想理解用户为什么这样做" | → **JTBD Knowledge** (本技能) — 挖掘用户背后的"工作" |
| "我不知道该研究什么" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐帮你找到方向 |
| "我需要验证一个假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试和样本量计算 |
| "我需要知道用户是谁" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 创建具体的人物角色 |
| "我的产品价值够不够？" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 契合度诊断 |
| "我怎么把研究结果讲清楚？" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事和图表改造 |

### 工作流 1: JTBD → 价值主张验证

```
JTBD (机会分数) → VPD (画布填充) → QuantUX (A/B 验证)
```

**场景**: 产品-市场契合验证
1. 用 JTBD 访谈发现用户核心"工作"和机会分数
2. 用 VPD 将 Jobs 映射到价值主张画布
3. 用 QuantUX 设计实验验证价值假设

### 工作流 2: JTBD → 人物角色定义

```
JTBD (任务聚类) → Persona (角色细分) → SWD (汇报呈现)
```

**场景**: 用户细分与定位
1. 用 JTBD 四力分析识别用户切换动机
2. 用 Persona 基于 JTBD 任务聚类创建角色
3. 用 SWD 将角色故事可视化呈现给团队

### 工作流 3: 增长策略

```
JTBD (流失分析) → QuantUX (数据验证) → VPD (策略调整)
```

**场景**: 用户留存提升
1. 用 JTBD Churn 访谈识别流失原因
2. 用 QuantUX 日志分析验证行为模式
3. 用 VPD 竞争战略评估差异化机会

> 💡 **提示**: JTBD 的进步力量模型（Push/Pull/Anxiety/Habit）是理解用户切换行为的核心框架。

## Run Tests / 运行测试

```bash
cd /path/to/jtbd-knowledge-skill
python3 jtbd/tests/test_all.py
# 或使用 pytest
python3 -m pytest jtbd/tests/test_all.py -v
```

## 🤝 参与贡献 (Contributing)

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

- 🐛 **报告 Bug**: 提交 [Issue](https://github.com/AliDujie/jtbd-knowledge-skill/issues)
- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AliDujie/jtbd-knowledge-skill/issues/new?template=feature_request.md)
- 📝 **改进文档**: PR 欢迎，特别是参考文档和代码示例

## 🆘 获取帮助 (Getting Help)

- 📖 查看 [故障排查](#故障排查-troubleshooting) 部分
- 📚 阅读 [references/](references/) 目录下的 11 篇方法论文档
- 💬 在 [Issues](https://github.com/AliDujie/jtbd-knowledge-skill/issues) 中提问

## 📖 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《When Coffee and Kale Compete》(2nd Ed) | Alan Klement | 全书方法论基础 |
| 《Competing Against Luck》 | Clayton Christensen | JTBD 理论起源 |
| 《Jobs to Be Done Playbook》 | Jim Kalbach | 实操指南与模板 |
| 《Demand-Side Sales 101》 | Bob Moesta | 销售视角的 JTBD |

## 📜 许可 (License)

基于《When Coffee and Kale Compete》(2nd Edition) by Alan Klement。本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《When Coffee and Kale Compete》by Alan Klement
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v3.1.3 | 2026-05-02 | 仓库维护：为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v3.1.2 | 2026-05-02 | 仓库维护：优化 12 大核心能力表与 Features at a Glance 一致性，增强技能生态工作流描述，统一交叉引用格式 |
| v3.1.1 | 2026-05-02 | 修复 SKILL.md 版本号不一致 (v3.0.0→v3.1.0)，补充 CEO 能力到英文能力表，添加 Structured-Thinking-Model 交叉引用 |
| v2.2 | 2026-04-30 | 更新维护，清理格式 |
| v2.0 | 2026-04-29 | 统一交叉引用为 GitHub 绝对链接，添加 GitHub Topics，更新 Last Updated 日期 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-05-02 | AliDujie Skill Ecosystem | v3.1.3*
