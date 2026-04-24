# JTBD Knowledge Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--04--23-brightgreen.svg)

> 🎯 **一句话介绍**: 基于 Alan Klement《When Coffee and Kale Compete》的 JTBD (Jobs to Be Done) 理论与实践工具集。提供 9 项可执行能力和 11 篇方法论知识库，覆盖从用户访谈到竞争分析到增长策略的完整 JTBD 工作流。

[English](#english) | [中文](#中文说明)

---

## 中文说明

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
```

### 💡 9 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview.py` | 4 维度（竞争/推/拉/焦虑）结构化问题 |
| 2 | **调查问卷设计** | `interview.py` | JTBD 导向的问卷模板 |
| 3 | **机会分数计算** | `analyzer.py` | 重要性×满意度差距，优先级排序 |
| 4 | **优先级矩阵** | `analyzer.py` | 机会分数矩阵可视化 |
| 5 | **竞争分析** | `analyzer.py` | JTBD 视角的竞品对比 |
| 6 | **营销文案生成** | `innovation.py` | 基于 JTBD 的 messaging |
| 7 | **增长与留存策略** | `innovation.py` | 四力驱动的增长策略 |
| 8 | **JTBD 描述验证** | `analyzer.py` | 三要素完整性检查 |
| 9 | **场景库深度分析** | `analyzer.py` | 场景驱动的深度洞察 |

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

👉 **探索完整生态系统**: [通用设计方法](../universal-design-methods/) | [人物角色](../web-persona-skill/) | [量化 UX 研究](../quantitative-ux-research/) | [价值主张设计](../value-proposition-design/) | [数据叙事](../storytelling-with-data/)

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
- **9 Core Capabilities** — Interview guides, surveys, opportunity scoring, priority matrices, competitive analysis, marketing copy, growth strategies, JTBD validation, scenario analysis
- **Forces of Progress Model** — Push / Pull / Anxiety / Habit analysis, understanding "why users switch" not "what they like"
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce JTBD reports immediately

### 🚀 Quick Start

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile

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
```

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](../universal-design-methods/)** — 100 design research methods
- **[Web-Persona-Skill](../web-persona-skill/)** — Persona creation
- **[Quantitative-UX-Research](../quantitative-ux-research/)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](../value-proposition-design/)** — Value proposition canvas
- **[Storytelling-with-Data](../storytelling-with-data/)** — Data storytelling

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](../universal-design-methods/) | [Web Persona](../web-persona-skill/) | [Quantitative UX Research](../quantitative-ux-research/) | [Value Proposition Design](../value-proposition-design/) | [Storytelling with Data](../storytelling-with-data/)

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

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
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-04-25 | AliDujie Skill Ecosystem*
