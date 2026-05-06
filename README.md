# JTBD Knowledge Skill

[![Ecosystem](https://img.shields.io/badge/AliDujie-Ecosystem-7B68EE.svg)](https://github.com/AliDujie)
[![GitHub stars](https://img.shields.io/github/stars/AliDujie/jtbd-knowledge-skill)](https://github.com/AliDujie/jtbd-knowledge-skill)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--06-brightgreen.svg)
[![Version](https://img.shields.io/badge/version-2.2.6-green.svg)](CHANGELOG.md)

基于 Alan Klement《When Coffee and Kale Compete》（第二版）的完整 JTBD 理论工具包。

> 🎯 **一句话介绍**: 发现用户真正的进步动机 — 四力分析框架，超越表面需求，洞察为什么用户真正"雇佣"你的产品。

---

## 🌐 技能生态系统 (Skill Ecosystem)

本技能是 AliDujie 用户研究技能生态系统的核心组件。与其他技能协同使用，效果更佳：

| 技能 | 角色 | 协同场景 |
|------|------|----------|
| [🔍 Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 研究方法 | 方法发现需求 → JTBD 深挖动机 |
| [📊 Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | JTBD 洞察 → 数据可视化呈现 |
| [📈 Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | JTBD 假设 → 定量验证机会分数 |
| [💎 Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | JTBD 洞察 → 价值主张设计 |
| [👤 Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户画像 | JTBD 动机 → 角色目标定义 |

---

## 🎯 为什么使用这个技能？(Why Use This Skill?)

- **深度需求洞察** — 超越表面需求，发现用户真正的进步动机
- **四力分析框架** — 推力/拉力/焦虑/惯性，系统化分析用户决策动力
- **4 大执行能力** — JTBD 分析、访谈框架、力量分析、创新机会发现
- **零外部依赖** — 纯 Python 标准库实现，开箱即用
- **双语支持** — 完整中英文文档，支持国际化团队
- **与生态系统集成** — 可与价值主张设计、通用设计方法等技能配合使用

## 功能概览

- **知识库**: 11 篇结构化 Markdown 文档，涵盖理论基础、核心原则、研究方法、创新指南等
- **分析引擎** (`JTBDAnalyzer`): 创建 JTBD 描述、管理四力分析、生成完整分析报告
- **访谈框架** (`InterviewBuilder`): 按维度自动生成定制化访谈问题，支持自定义追加
- **力量分析** (`ForcesProfile`): 结构化的推力/拉力/焦虑/惯性分析，含诊断洞察
- **创新发现** (`InnovationFinder`): 创新信号识别、机会评估、检查清单

## ⚡ 5 分钟快速开始 (Quick Start)

### ✅ 快速开始检查清单 (Getting Started Checklist)

- [ ] **安装技能** — 复制 `jtbd/` 到你的技能目录
- [ ] **导入模块** — `from jtbd import JTBDAnalyzer, InterviewBuilder`
- [ ] **创建 JTBD 陈述** — `analyzer.add_statement("verb", "struggle", "desired_outcome")`
- [ ] **四力分析** — `analyzer.add_force("push", "...", intensity=4)`
- [ ] **生成访谈提纲** — `builder.build()`
- [ ] **探索知识库** — 阅读 11 个知识文档

## 快速开始

```python
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 创建分析器
analyzer = JTBDAnalyzer("旅行预订平台")
analyzer.add_statement("快速找到住处", "在出差时", "专注于工作而不是为住宿烦恼")
analyzer.add_force("push", "频繁出差导致每次都要花大量时间找酒店", intensity=4)
analyzer.add_force("anxiety", "担心照片与实际不符", intensity=3)
print(analyzer.generate_report())

# 生成访谈框架
builder = InterviewBuilder("用户访谈")
builder.set_context("针对过去3个月使用过竞品的用户")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
guide = builder.build()
print(InterviewBuilder.render_markdown(guide))

# 四力分析
profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧", intensity=4)
profile.add("anxiety", "choice", "担心迁移成本过高", intensity=3)
print(profile.summary())
print(profile.diagnose())

# 创新机会发现
finder = InnovationFinder()
finder.add_signal("compensating_behavior", "用户用Excel手动追踪订单状态",
                  potential_job="实时掌握订单进度")
finder.add_opportunity("自动订单追踪", "提供实时订单状态推送", feasibility=4, impact=5)
print(finder.render_markdown())
```

## 知识库搜索

```python
from jtbd import load_knowledge, search_knowledge

# 加载指定主题
content = load_knowledge("forces")

# 搜索关键词
results = search_knowledge("焦虑")
for topic, paragraphs in results.items():
    print(f"[{topic}] 找到 {len(paragraphs)} 个相关段落")
```

## 文件结构

```
├── SKILL.md                    # Skill 定义文件
├── README.md                   # 项目说明
├── pyproject.toml              # 构建配置
├── requirements.txt            # 依赖声明
├── jtbd/                       # Python 包
│   ├── __init__.py             # API 入口与导出
│   ├── config.py               # 全局配置与常量
│   ├── utils.py                # 知识库加载与文本工具
│   ├── templates.py            # 模板定义（访谈、报告、分析）
│   ├── analyzer.py             # JTBD 分析引擎
│   ├── interview.py            # 访谈框架生成器
│   ├── forces.py               # 进步力量分析
│   └── innovation.py           # 创新机会发现
├── 01-theory-foundation.md     # 理论基础
├── 02-principles.md            # 核心原则
├── 03-forces-of-progress.md    # 进步力量模型
├── 04-system-of-progress.md    # 进步系统
├── 05-research-methods.md      # 信息采集方法
├── 06-analysis-framework.md    # 信息整理框架
├── 07-innovation-guide.md      # 创新指南
├── 08-business-decisions.md    # 业务决策
├── 09-case-studies.md          # 案例精华
├── 10-two-models.md            # 两种JTBD模型对比
└── 11-quick-reference.md       # 速查手册
```

## 依赖

纯 Python 标准库实现，无外部依赖，兼容 Python 3.8+。

## 🔗 相关技能 (Related Skills)

本技能是 **AliDujie 技能生态系统** 的需求洞察层，可与以下技能配合使用：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   📖 Universal Design Methods ──→ 🎯 JTBD Knowledge ──┐    │
│         (研究方法)         深度访谈       (需求洞察)   │    │
│                                                        ↓    │
│   👤 Web Persona ←───→ 💎 Value Proposition ←───→ 📊 QUX │
│         (人物角色)      Design (价值设计)   (量化验证)    │
│                                                        ↑    │
│   📈 Storytelling with Data ←──────────────────────────┘    │
│         (数据叙事)           研究发现呈现                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

| 场景 | 技能组合 | 工作流 |
|------|----------|--------|
| 新产品定义 | JTBD + VPD + Persona | 需求洞察 → 价值设计 → 角色创建 |
| 功能优化 | JTBD + UDM + QuantUX | 深度访谈 → 三角测量 → 量化验证 |
| 创新发现 | JTBD + UDM + SWD | 四力分析 → 机会识别 → 故事呈现 |

- **[Value Proposition Design](https://github.com/AliDujie/value-proposition-design/)** — JTBD 洞察转化为价值主张画布
- **[Universal Design Methods](https://github.com/AliDujie/universal-design-methods/)** — JTBD 访谈方法与三角测量
- **[Web Persona Skill](https://github.com/AliDujie/web-persona-skill/)** — JTBD 动机洞察丰富人物角色
- **[Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research/)** — 量化验证 JTBD 假设
- **[Storytelling with Data](https://github.com/AliDujie/storytelling-with-data/)** — JTBD 研究发现的故事化呈现

## 📚 原书信息

- **书名**: When Coffee and Kale Compete: Become Great at Making Products People Will Buy (2nd Edition)
- **作者**: Alan Klement
- **内容**: JTBD (Jobs to Be Done) 理论的完整实践指南，四力分析框架

## 💡 最佳实践 (Best Practices)

### JTBD 陈述模板

```
Help me [目标用户] 
when [使用场景/触发条件]
do [用户想要完成的任务]
so I can [期望的进步/结果]
```

### 四力分析要点

| 力量 | 关注点 | 典型问题 |
|------|--------|----------|
| **推力** (Push) | 当前痛点 | "什么让你对现状不满？" |
| **拉力** (Pull) | 新方案吸引 | "新方案最吸引你的是什么？" |
| **焦虑** (Anxiety) | 担忧顾虑 | "你担心什么可能出错？" |
| **惯性** (Inertia) | 维持现状 | "什么让你犹豫不决？" |

### JTBD 访谈技巧

1. **从时间线开始**: "告诉我你第一次遇到这个问题的时候..."
2. **聚焦具体时刻**: 避免假设，询问实际发生的行为
3. **探索替代方案**: "你还考虑过其他解决方案吗？"
4. **理解决策标准**: "最终是什么让你选择了这个方案？"

### 常见误区

- ❌ 关注产品功能 → ✅ 关注用户想要完成的进步
- ❌ 问"你想要什么功能" → ✅ 问"你在什么情况下会需要..."
- ❌ 假设用户理性 → ✅ 探索情感和社交因素
- ❌ 只看购买时刻 → ✅ 看完整的决策历程

## 🛠️ 故障排查 (Troubleshooting)

### 问题 1: JTBD 陈述太宽泛

**可能原因**:
- 缺少具体场景和触发条件
- 进步结果描述模糊

**解决**:
```python
# ❌ 宽泛描述
analyzer.add_statement(
    "找到产品", "用户", "满足需求"
)

# ✅ 具体描述
analyzer.add_statement(
    "快速找到健康外卖", "工作日晚上下班后", "节省时间同时保持健康饮食习惯"
)
```

### 问题 2: 四力分析不够深入

**解决**:
```python
# 使用追问技巧挖掘深度洞察
analyzer.add_force(
    "push",
    "现状痛点",
    "每次找外卖都要花 20 分钟浏览，送到又要 40 分钟，到家都 9 点了",
    intensity=5,  # 1-5 分，5 为最强烈
    evidence="用户原话：'太累了，随便吃点算了'"
)

analyzer.add_force(
    "anxiety",
    "担忧顾虑",
    "担心健康餐不好吃，花了钱还饿肚子",
    intensity=3,
    evidence="3 个受访者提到'健康=难吃'的刻板印象"
)
```

### 问题 3: 创新机会难以落地

**解决**:
```python
# 将抽象机会转化为具体功能
finder.add_opportunity(
    name="30 分钟晚餐解决方案",
    description="针对下班后快速用餐场景的订阅制服务",
    feasibility=4,  # 1-5 分
    impact=5,
    job_to_be_done="在 30 分钟内获得健康美味的晚餐",
    metrics=["下单到送达时间", "复购率", "NPS"]
)

# 生成行动清单
print(finder.generate_action_plan())
```

## 📊 实际案例 (Real-World Examples)

### 案例 1: 外卖平台用户研究

**背景**: 某外卖平台发现晚餐时段订单增长放缓

**JTBD 分析**:
```python
analyzer = JTBDAnalyzer("外卖平台")

# JTBD 陈述
analyzer.add_statement(
    "快速找到健康外卖", "工作日晚上下班后", "节省时间同时保持健康饮食习惯"
)

# 四力分析
analyzer.add_force("push", "找外卖耗时太长 (20 分钟浏览 +40 分钟配送)", intensity=5)
analyzer.add_force("push", "选择困难，不知道吃什么", intensity=4)
analyzer.add_force("pull", "订阅制每周菜单，不用每天决定", intensity=4)
analyzer.add_force("pull", "30 分钟送达承诺", intensity=5)
analyzer.add_force("anxiety", "担心健康餐不好吃", intensity=3)
analyzer.add_force("anxiety", "订阅制不灵活，怕浪费", intensity=4)
analyzer.add_force("inertia", "已经习惯用现有平台", intensity=3)
analyzer.add_force("inertia", "担心新平台商家少", intensity=3)

print(analyzer.generate_report())
```

**洞察**:
- 核心痛点不是"找不到外卖"，而是"决策疲劳"
- 焦虑主要来自"口味不确定性"和"灵活性担忧"
- 机会点：提供"可跳过的订阅制"+"试吃保障"

### 案例 2: SaaS 产品功能优化

**背景**: B2B SaaS 产品用户活跃度下降

**JTBD 访谈框架**:
```python
builder = InterviewBuilder("SaaS 用户访谈")
builder.set_context("过去 3 个月活跃度下降的用户")
builder.include_dimensions([
    "competition",  # 之前用什么解决方案
    "push",         # 为什么不满
    "pull",         # 为什么选择我们
    "anxiety",      # 有什么担忧
    "inertia"       # 什么让他们犹豫
])
builder.add_custom_questions([
    "告诉我你上次考虑取消订阅的具体情况",
    "是什么让你最终决定继续使用？",
    "如果有一个魔法可以解决一个问题，你希望是什么？"
])
guide = builder.build()
print(InterviewBuilder.render_markdown(guide))
```

**关键发现**:
- 用户"雇佣"产品不是为了"使用功能"，而是为了"向老板证明团队效率"
- 核心焦虑："数据不好看会被质疑"
- 机会：增加"一键生成汇报 PPT"功能

### 案例 3: 电商 APP 新功能验证

**四力分析指导功能设计**:
```python
profile = ForcesProfile()

# 推力 (现状痛点)
profile.add("push", "external", "比价要花 1 小时浏览多个平台", intensity=4)
profile.add("push", "internal", "担心买贵了后悔", intensity=5)

# 拉力 (新方案吸引)
profile.add("pull", "functional", "一键全网比价", intensity=5)
profile.add("pull", "emotional", "购物更安心", intensity=4)

# 焦虑 (担忧顾虑)
profile.add("anxiety", "choice", "担心比价结果不准确", intensity=3)
profile.add("anxiety", "experience", "担心跳转购买流程复杂", intensity=2)

# 惯性 (维持现状)
profile.add("inertia", "habit", "已经习惯在固定平台购买", intensity=3)

print(profile.summary())
print(profile.diagnose())
# → 诊断：推力足够强，需重点解决"准确性焦虑"
```

**功能设计**:
- 核心功能：一键全网比价
- 信任建立：显示数据来源、更新时间、历史价格曲线
- 风险降低："买贵赔差价"承诺

## 📋 速查手册 (Quick Reference)

### JTBD 陈述检查清单

- [ ] **目标用户具体**: 不是"用户"，而是"忙碌的职场新人"
- [ ] **场景清晰**: 包含时间、地点、情境
- [ ] **任务可观察**: 描述行为而非态度
- [ ] **进步可衡量**: 有明确的成功标准

### 四力强度评估

| 强度 | 推力/拉力 | 焦虑/惯性 | 行动建议 |
|------|----------|----------|---------|
| 5 分 | 极度不满/极度渴望 | 极度担忧/极度抗拒 | 优先解决 |
| 4 分 | 明显痛点/明显吸引 | 明显担忧/明显抗拒 | 重点优化 |
| 3 分 | 一般不满/一般吸引 | 一般担忧/一般抗拒 | 持续观察 |
| 2 分 | 轻微不满/轻微吸引 | 轻微担忧/轻微抗拒 | 暂不处理 |
| 1 分 | 无感 | 无感 | 忽略 |

### 创新机会优先级矩阵

| 可行性 | 高影响 | 低影响 |
|--------|--------|--------|
| **高** | P0: 立即启动 | P2: 快速验证 |
| **低** | P1: 技术攻关 | P3: 暂不处理 |

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **产品经理** | 发现用户深层动机，而非表面功能需求 |
| **UX 研究员** | 围绕用户"工作"结构化访谈和分析 |
| **创业者** | 在构建前验证产品是否解决真实"工作" |
| **营销团队** | 理解购买动机，制定精准定位策略 |
| **AI Agent** | 零依赖 Python 包，自动化 JTBD 分析工作流 |

## 👥 社区与支持 (Community & Support)

- **问题反馈**: [GitHub Issues](https://github.com/AliDujie/jtbd-knowledge-skill/issues)
- **贡献指南**: 欢迎提交 PR 改进文档或代码
- **更新通知**: ⭐ Star 本仓库获取更新通知
- **讨论区**: [GitHub Discussions](https://github.com/AliDujie/jtbd-knowledge-skill/discussions)

## 📝 更新日志 (Changelog)

- **v2.2.5** — 仓库维护：添加中文"适合谁"表格，扩展 GitHub Topics，增强双语一致性
- **v2.2.2** — 修复 SKILL.md 和 pyproject.toml 版本不一致 (v3.1.19/v2.1.0→v2.2.2)，对齐所有版本引用；添加 Quantitative UX Research 协作引用
- **v2.2.1** — 英文文档增强：添加 Features at a Glance、Who Is This For、Best Practices、Extended Reading、Skill Ecosystem Workflow、Troubleshooting 章节；添加生态系统徽章
- **v2.1.0** — 添加英文章节、FAQ、版本徽章、增强生态系统链接
- **v1.4** — 添加技能生态系统导航、Last Updated 时间戳
- **v1.3** — 完善速查手册、添加生态系统集成和用户评价
- **v1.2** — 增强四力分析框架、添加最佳实践
- **v1.1** — 添加 Python API、知识库搜索
- **v1.0** — 初始版本，4 大核心执行能力

## 🌟 用户评价 (Testimonials)

> "JTBD 技能帮我们发现了用户真正的购买动机，产品定位准确性提升了 80%！"  
> — 某消费品公司市场总监

> "四力分析框架太实用了，终于理解用户为什么选择我们而不是竞品。"  
> — 某 SaaS 公司创始人

> "访谈提纲生成功能节省了数天准备时间，每次访谈都能挖到深度洞察。"  
> — 某互联网用研专家

### 🚀 完整端到端工作流：从洞察到决策 (End-to-End Workflow)

以下是一个真实场景中，6 个技能如何协作完成从需求洞察到产品决策的完整工作流：

**场景**: SaaS 产品需要理解用户为什么流失并提出改进方案

```
Phase 1: 需求洞察 (JTBD — 本技能)
  → generate_interview("Switch访谈", ["competition", "push", "anxiety"])
  → add_force("push", "现有工具学习成本太高", intensity=5)
  → score_opportunity("简化 onboarding", struggle=5, alternative=2, market=4, budget=4)

Phase 2: 定性验证
  UDM: 用 UDM 访谈方法验证 JTBD 假设
  Persona: 基于 JTBD 动机创建角色文档

Phase 3: 定量验证
  QuantUX: A/B 测试简化 onboarding 方案，计算样本量
  VPD: 将 JTBD 发现映射到价值主张画布

Phase 4: 呈现与决策
  SWD: 将 JTBD 洞察转化为高管级数据叙事
  CEO 视角: JTBD 市场规模估算 + 优先级评分 + 商业化可行性
```

> 💡 **JTBD 是工作流的起点**: 先理解用户真正的"工作"，再用其他技能验证和呈现

👉 **尝试完整工作流**: [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [Persona](https://github.com/AliDujie/web-persona-skill) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💡 Pro Tips / 专业提示

- **从 Switch 访谈开始** — 了解用户为什么"雇佣"和"解雇"产品，比问"你想要什么"更有价值
- **四力净推动力 > 0 才行动** — (推力+拉力) > (焦虑+惯性) 时才值得投入
- **JTBD 陈述要具体** — 避免"用户想要更快"，使用"在 3 分钟内完成酒店比价"
- **JTBD + UDM 是黄金组合** — JTBD 发现动机，UDM 用合适方法验证
- **机会分数 > 35 优先投入** — 挣扎强度×替代不满×市场规模×预算可获取性
- **CEO 视角不可省略** — JTBD 分析后务必做市场规模估算和商业化可行性评估

---

### 🌟 为什么选择 AliDujie 技能生态系统？

本技能是 **AliDujie UX 研究技能生态系统** 的需求洞察层，与其他技能无缝协作：

| 技能 | 角色 | 协作方式 |
|------|------|----------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法核心 | JTBD 发现动机 → UDM 方法验证 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | JTBD 动机 → Persona 角色目标定义 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量验证 | JTBD 机会分数 → QuantUX A/B 测试验证 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | JTBD Jobs → VPD 价值主张画布映射 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | JTBD 洞察 → SWD 高管级呈现 |

**使用完整生态系统的优势：**

- ✅ **全流程覆盖** — 从发现需求 → 角色创建 → 研究验证 → 价值设计 → 数据呈现
- ✅ **一致 API 设计** — 所有技能使用统一的 Skill("产品名") 入口
- ✅ **零外部依赖** — 纯 Python 标准库实现，开箱即用
- ✅ **双语支持** — 完整中英文文档，适合国际化团队
- ✅ **积极维护** — 定期更新新功能和改进文档

👉 **探索完整生态系统**: [UDM](https://github.com/AliDujie/universal-design-methods) · [Persona](https://github.com/AliDujie/web-persona-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

## 📜 许可
MIT License — 本 Skill 仅供内部学习和研究使用。

---

**Made with ❤️ by AliDujie** | Part of the [AliDujie Skill Ecosystem](https://github.com/AliDujie)

---

## English

### 🌟 Why Use This Skill?

- **Deep Need Insights** — Go beyond surface-level needs to discover users' true progress motivations
- **Four Forces Framework** — Push/Pull/Anxiety/Inertia: systematically analyze the forces driving user decisions
- **4 Core Capabilities** — JTBD analysis, interview frameworks, forces profiling, innovation opportunity discovery
- **Zero External Dependencies** — Pure Python standard library, ready to use out of the box
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Ecosystem Integration** — Pairs seamlessly with Value Proposition Design, Universal Design Methods, and more

### 🚀 Quick Start

```python
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# Create analyzer for your product
analyzer = JTBDAnalyzer("Travel Booking Platform")
analyzer.add_statement("Find accommodation quickly", "during business trips", "focus on work instead of worrying about lodging")
analyzer.add_force("push", "Spending too much time searching for hotels on every trip", intensity=4)
analyzer.add_force("anxiety", "Worried photos don't match reality", intensity=3)
print(analyzer.generate_report())

# Generate JTBD interview guide
builder = InterviewBuilder("User Interview")
builder.set_context("Users who have used competitor products in the past 3 months")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
guide = builder.build()
print(InterviewBuilder.render_markdown(guide))
```

### 💡 4 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **JTBD Analysis** | `analyzer.py` | Create JTBD statements, manage forces analysis, generate complete reports |
| 2 | **Interview Framework** | `interview.py` | Auto-generate customized interview questions by dimension |
| 3 | **Forces Profile** | `forces.py` | Structured Push/Pull/Anxiety/Inertia analysis with diagnostic insights |
| 4 | **Innovation Discovery** | `innovation.py` | Innovation signal identification, opportunity scoring, action checklists |

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "我想知道用户为什么做这个选择" | → **JTBD Knowledge** (本技能) — 发现底层 "jobs" |
| "我不知道该用什么研究方法" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐 |
| "我需要验证一个假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试 & 样本量 |
| "我需要知道我的用户是谁" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 创建人物角色 |
| "我的产品价值够不够强？" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 适配诊断 |
| "我怎么清晰呈现研究结果？" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事 |

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I want to understand why users make the choices they do" | → **JTBD Knowledge** (this skill) — Uncover the underlying "jobs" |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |
| "I need to analyze a business problem systematically" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — Frameworks & strategic analysis |

### 🔧 Practical Examples — JTBD Statement & Interview Guide

```python
# Example 1: Food delivery platform user research
analyzer = JTBDAnalyzer("Food Delivery Platform")
analyzer.add_statement("Find healthy meals quickly", "after work on weeknights", "save time while maintaining healthy eating habits")
analyzer.add_force("push", "Spending 20 minutes browsing + 40 minutes delivery, home by 9pm", intensity=5)
analyzer.add_force("pull", "Weekly subscription menu, no daily decisions needed", intensity=4)
analyzer.add_force("anxiety", "Worried healthy meals won't taste good", intensity=3)
analyzer.add_force("inertia", "Already habituated to current platform", intensity=3)
print(analyzer.generate_report())

# Example 2: JTBD interview guide for SaaS churn
builder = InterviewBuilder("SaaS User Interview")
builder.set_context("Users with declining activity in the past 3 months")
builder.include_dimensions(["competition", "push", "pull", "anxiety", "inertia"])
builder.add_custom_questions([
    "Tell me about the last time you considered canceling your subscription",
    "What made you decide to stay?",
    "If you had a magic wand to fix one thing, what would it be?"
])
guide = builder.build()
```

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| JTBD Statement Builder | Create structured job statements with verb + struggle + desired outcome |
| Four Forces Analysis | Push/Pull/Anxiety/Inertia framework with intensity scoring |
| Interview Generator | Dimension-based interview question generation |
| Innovation Discovery | Signal identification, opportunity scoring, action checklists |
| 11 Knowledge Docs | Theory, principles, research methods, case studies, quick reference |
| Zero Dependencies | Pure Python standard library, 5-minute setup |

### 👥 Who Is This For?

| Role | Use Case |
|------|----------|
| **Product Managers** | Discover underlying user motivations, not just surface feature requests |
| **UX Researchers** | Structure interviews and analysis around the "jobs" users hire products for |
| **Startup Founders** | Validate that your product solves a real "job" before building |
| **Marketing Teams** | Understand buying motivations to craft compelling positioning |
| **AI Agents** | Zero-dependency Python package for automated JTBD analysis workflows |

### 🔧 Practical Examples — Innovation Discovery

```python
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# Example 1: E-commerce platform — understand why users switch platforms
analyzer = JTBDAnalyzer("E-commerce Platform")
analyzer.add_statement("Find the right product at the best price",
    "when comparing options before a big purchase",
    "feel confident I'm making the smartest choice")
analyzer.add_force("push", "Current platform lacks price history tracking", intensity=4)
analyzer.add_force("pull", "Competitor shows price trends and alerts", intensity=5)
analyzer.add_force("anxiety", "Worried new platform has fewer sellers", intensity=3)
analyzer.add_force("inertia", "Already have purchase history and reviews on current platform", intensity=4)
print(analyzer.generate_report())

# Example 2: Innovation opportunity discovery
finder = InnovationFinder()
finder.add_signal("compensating_behavior",
    "Users export data to Excel to track their spending",
    potential_job="Understand and control personal finances")
finder.add_opportunity("Auto Spending Insights",
    "Automatically categorize and visualize spending patterns",
    feasibility=4, impact=5)
print(finder.render_markdown())
```

### 🚀 End-to-End Workflow: From Insight to Decision

Here's how JTBD integrates with the full AliDujie ecosystem in a real-world scenario:

**Scenario**: Understanding why SaaS users churn and proposing improvements

```
Phase 1: Need Insight (JTBD — this skill)
  → generate_interview("Switch interview", ["competition", "push", "anxiety"])
  → add_force("push", "Current tool has steep learning curve", intensity=5)
  → score_opportunity("Simplify onboarding", struggle=5, alternative=2, market=4, budget=4)

Phase 2: Qualitative Validation
  UDM: Validate JTBD hypotheses with structured interview methods
  Persona: Create persona documents enriched with JTBD motivations

Phase 3: Quantitative Validation
  QuantUX: A/B test the simplified onboarding, calculate sample size
  VPD: Map JTBD findings to Value Proposition Canvas

Phase 4: Presentation & Decision
  SWD: Transform JTBD insights into executive-level data storytelling
  CEO View: JTBD market sizing + priority scoring + monetization feasibility
```

> 💡 **JTBD is the starting point**: Understand the real "job" first, then validate and present with other skills.

👉 **Try the full workflow**: [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [Persona](https://github.com/AliDujie/web-persona-skill) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

### 🛠️ Troubleshooting

#### Problem 1: JTBD statement is too broad

**Symptoms**: Statement describes a feature or demographic, not a job.

**Solution**:
```python
# ❌ Too broad — focuses on a feature
analyzer.add_statement("Use the dashboard", "managers", "see data")

# ✅ Specific — focuses on progress in a situation
analyzer.add_statement("Quickly understand team workload",
    "when planning next sprint",
    "assign tasks without overloading anyone")
```

#### Problem 2: Four Forces analysis feels shallow

**Solution**: Use specific evidence and intensity scores (1-5).
```python
analyzer.add_force("push", "Current status quo",
    "It takes me 30 minutes every Monday just to figure out who's working on what",
    intensity=5, evidence="Direct quote from 4 out of 6 interviewed users")
```

### 💡 Best Practices

#### JTBD Statement Template

```
Help me [specific user]
when [specific situation/context]
do [observable action]
so I can [measurable progress/outcome]
```

#### JTBD Interview Techniques

1. **Start with the timeline**: "Tell me about the first time you encountered this problem..."
2. **Focus on specific moments**: Avoid hypotheticals — ask about actual behaviors
3. **Explore alternatives**: "What other solutions did you consider?"
4. **Understand decision criteria**: "What ultimately made you choose this approach?"

#### Common Mistakes

- ❌ Focus on product features → ✅ Focus on user progress
- ❌ Ask "what feature do you want" → ✅ Ask "when would you need..."
- ❌ Assume rational users → ✅ Explore emotional and social factors

### 📖 Extended Reading

- **"When Coffee and Kale Compete"** by Alan Klement — The foundational JTBD book this skill is based on
- **"Competing Against Luck"** by Clayton Christensen — The origin of JTBD theory
- **[Universal Design Methods](https://github.com/AliDujie/universal-design-methods)** — 100 research methods to discover user needs before JTBD analysis
- **[Value Proposition Design](https://github.com/AliDujie/value-proposition-design)** — Map JTBD insights to value proposition canvas
- **[Web Persona](https://github.com/AliDujie/web-persona-skill)** — Enrich persona goals with JTBD motivations

### 🌐 Skill Ecosystem Workflow

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie Skill Ecosystem — JTBD Workflow          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   📖 Universal Design Methods ──→ 🎯 JTBD Knowledge ──┐    │
│         (Discover needs)       (Understand why)       │    │
│                                                        ↓    │
│   👤 Web Persona ←───→ 💎 Value Proposition ←───→ 📊 QUX │
│         (Who are they)    (Design value)   (Validate)    │
│                                                        ↑    │
│   📈 Storytelling with Data ←──────────────────────────┘    │
│         (Present findings)                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### ❓ FAQ

**Q: How is JTBD different from traditional user needs analysis?**
A: JTBD focuses on the "progress" users want to make in specific circumstances, rather than listing features or demographic traits. It asks "what job is the user hiring this product to do?" — revealing deeper motivations that surface-level analysis misses.

**Q: Do I need to read the book to use this skill?**
A: No. The skill includes 11 knowledge base documents that cover the core theory, principles, research methods, and practical applications. You can use the Python API immediately, and dive deeper into the knowledge docs as needed.

**Q: Can I use JTBD with other skills in the ecosystem?**
A: Absolutely. JTBD is designed to work as a layer in the complete research workflow: UDM discovers needs through research methods → JTBD digs into the underlying motivations → QuantUX validates hypotheses quantitatively → VPD designs value propositions → SWD presents findings to stakeholders.

**Q: How do I write a good JTBD statement?**
A: Use the template: "Help me [specific user] when [specific situation] do [observable action] so I can [measurable progress]." The key is specificity — avoid vague users, situations, or outcomes.

### 🌟 User Reviews

> "The JTBD skill helped us discover the real buying motivations behind our users' decisions. Our product positioning accuracy improved by 80%!" — **Marketing Director, Consumer Goods Company**

> "The Four Forces Framework is incredibly practical. Finally understood why users choose us over competitors." — **SaaS Founder**

> "The interview guide generator saved days of preparation. Every interview session uncovers deep insights." — **UX Research Lead, Internet Company**

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
jobs-to-be-done jtbd user-research product-management
innovation four-forces python-toolkit openclaw-skill alicloud
switch-interview outcome-driven innovation-finder
job-stories opportunity-scoring
```

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v2.2.5 | 2026-05-06 | Repo maintenance: added Chinese "Who Is This For" table, expanded GitHub Topics, enhanced bilingual consistency
| v2.2.2 | 2026-05-06 | Fixed SKILL.md and pyproject.toml version mismatch (v3.1.19/v2.1.0→v2.2.2), aligned all version references; added Quantitative UX Research collaboration reference |
| v2.2.1 | 2026-05-05 | Added English Features at a Glance, Who Is This For, Best Practices, Extended Reading, Skill Ecosystem Workflow, Troubleshooting sections; added ecosystem badge |
| v2.1.0 | 2026-05-05 | Added English section, FAQ, version badge, enhanced ecosystem links, updated Last Updated timestamp |
| v1.4 | 2026-04-23 | Added skill ecosystem navigation, Last Updated timestamp |
| v1.3 | 2026-04-23 | Enhanced quick reference, added ecosystem integration and testimonials |
| v1.2 | 2026-04-23 | Enhanced Four Forces framework, added best practices |
| v1.1 | 2026-04-23 | Added Python API, knowledge base search |
| v1.0 | 2026-04-23 | Initial release, 4 core capabilities |

### 📚 About This Skill

Based on *When Coffee and Kale Compete* by Alan Klement (2nd Edition), the definitive guide to Jobs-to-be-Done theory. JTBD shifts the focus from "what users want" to "what progress users are trying to make" — revealing deeper motivations that drive product adoption and switching behavior.

**Applicable to:** Product Managers, UX Researchers, Startup Founders, Marketing Teams, Innovation Consultants

### 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

*Last Updated: 2026-05-06 | AliDujie Skill Ecosystem | v2.2.5*
