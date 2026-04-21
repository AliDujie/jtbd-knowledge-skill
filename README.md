# JTBD Knowledge Skill (Jobs to be Done 知识技能)

基于 Alan Klement《When Coffee and Kale Compete》(第二版) 的完整 JTBD 理论工具包。

## 🎯 为什么使用这个技能？(Why Use This Skill?)

- **深度需求洞察** — 超越表面功能，理解用户真正的进步动机
- **四力分析框架** — 推力/拉力/焦虑/惯性，系统化分析用户决策
- **实战工具齐全** — 访谈框架、分析引擎、创新发现，一站式解决
- **零外部依赖** — 纯 Python 标准库，开箱即用
- **双语支持** — 完整中英文文档，支持国际化团队
- **与生态系统集成** — 可与通用设计方法、价值主张设计等技能配合

## ⚡ 5 分钟快速开始 (Quick Start)

### ✅ 快速开始检查清单 (Getting Started Checklist)

- [ ] **安装技能** — 复制 `skills/jtbd-knowledge-skill` 到你的技能目录
- [ ] **导入模块** — `from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile`
- [ ] **创建 JTBD 描述** — 使用 `JTBDAnalyzer` 定义用户任务
- [ ] **生成访谈框架** — 使用 `InterviewBuilder` 创建访谈指南
- [ ] **四力分析** — 使用 `ForcesProfile` 分析用户决策力量
- [ ] **探索知识库** — 阅读 11 篇 JTBD 理论文档

### 步骤 1: 安装 (Installation)

```bash
# 复制为 AI Skill
cp -r ~/.agents/skills/jtbd-knowledge-skill/skills/jtbd-knowledge-skill ~/.aoneclaw/skills/

# 或作为 Python 包使用 (无需安装)
# 直接在代码中添加路径即可
```

### 步骤 2: 基础使用 (Basic Usage)

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 场景 1: 创建 JTBD 描述
analyzer = JTBDAnalyzer("旅行预订平台")
analyzer.add_statement("Help me", "在出差时快速找到合适的住处", "专注于工作而不是为住宿烦恼")
print(analyzer.generate_report())

# 场景 2: 生成访谈框架
builder = InterviewBuilder("用户访谈")
builder.set_context("针对过去 3 个月使用过竞品的用户")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
guide = builder.build()
print(InterviewBuilder.render_markdown(guide))

# 场景 3: 四力分析
profile = ForcesProfile()
profile.add("push", "external", "频繁出差导致每次都要花大量时间找酒店", intensity=4)
profile.add("pull", "external", "竞品有一键预订功能，5 秒完成", intensity=5)
profile.add("anxiety", "choice", "担心照片与实际不符", intensity=3)
profile.add("anxiety", "inertia", "懒得换平台，熟悉当前流程", intensity=2)
print(profile.summary())
print(profile.diagnose())
```

### 步骤 3: 进阶使用 (Advanced)

```python
# 创新机会发现
finder = InnovationFinder()
finder.add_signal("compensating_behavior", "用户用 Excel 手动追踪订单状态",
                  potential_job="实时掌握订单进度")
finder.add_opportunity("自动订单追踪", "提供实时订单状态推送", feasibility=4, impact=5)
print(finder.render_markdown())

# 知识库搜索
from jtbd import load_knowledge, search_knowledge

# 加载指定主题
content = load_knowledge("forces")

# 搜索关键词
results = search_knowledge("焦虑")
for topic, paragraphs in results.items():
    print(f"[{topic}] 找到 {len(paragraphs)} 个相关段落")
```

## 🔧 核心功能 (Core Features)

| 组件 | 类名 | 功能 | 使用场景 |
|------|------|------|----------|
| **分析引擎** | `JTBDAnalyzer` | 创建 JTBD 描述、管理四力分析、生成完整报告 | 深度需求分析 |
| **访谈框架** | `InterviewBuilder` | 按维度自动生成定制化访谈问题 | 用户研究准备 |
| **力量分析** | `ForcesProfile` | 结构化推力/拉力/焦虑/惯性分析，含诊断洞察 | 竞争分析、用户决策理解 |
| **创新发现** | `InnovationFinder` | 创新信号识别、机会评估、检查清单 | 产品创新、机会识别 |
| **知识库** | 11 篇 Markdown | 理论基础、核心原则、研究方法、创新指南 | 学习参考、快速查询 |

## 📚 实用示例 (Practical Examples)

### 示例 1: 完整 JTBD 分析流程

```python
# 初始化分析器
skill = JTBDAnalyzer("在线旅行预订平台")

# 步骤 1: 定义核心 JTBD
skill.add_statement(
    help_me="在出差时快速找到合适的住处",
    so_that="可以专注于工作而不是为住宿烦恼",
    context="商务出差，时间紧张，对价格不敏感"
)

# 步骤 2: 添加推力 (Push Forces)
skill.add_force("push", "当前平台搜索太慢，每次花 15+ 分钟", intensity=4)
skill.add_force("push", "筛选条件不够精准，经常找不到合适的", intensity=3)

# 步骤 3: 添加拉力 (Pull Forces)
skill.add_force("pull", "竞品有一键预订功能，5 秒完成", intensity=5)
skill.add_force("pull", "朋友推荐的新平台有 AI 推荐", intensity=3)

# 步骤 4: 添加焦虑 (Anxiety)
skill.add_force("anxiety", "担心照片与实际不符", intensity=3)
skill.add_force("anxiety", "担心取消政策太严格", intensity=2)

# 步骤 5: 添加惯性 (Inertia)
skill.add_force("inertia", "懒得换平台，熟悉当前流程", intensity=2)
skill.add_force("inertia", "积分和会员等级不想放弃", intensity=3)

# 生成完整报告
report = skill.generate_report()
print(report)
```

### 示例 2: JTBD 访谈框架生成

```python
# 创建访谈构建器
builder = InterviewBuilder("商务用户深度访谈")

# 设置背景
builder.set_context(
    target="过去 3 个月有至少 2 次商务出差预订的用户",
    goal="理解用户选择和使用预订平台的决策过程",
    duration="45-60 分钟"
)

# 选择访谈维度
builder.include_dimensions([
    "competition",    # 竞品对比
    "push",          # 推力因素
    "pull",          # 拉力因素
    "anxiety",       # 焦虑因素
    "inertia",       # 惯性因素
    "timeline"       # 时间线
])

# 自定义追加问题
builder.add_custom_questions([
    "能描述一下上次出差预订酒店的完整过程吗？",
    "当时有没有考虑过其他方案？为什么没选？",
    "什么因素让你最终决定用这个平台？"
])

# 生成访谈指南
guide = builder.build()
print(InterviewBuilder.render_markdown(guide))

# 输出包含：
# - 开场介绍和暖场问题
# - 竞品对比探索
# - 四力深度挖掘
# - 决策时间线重建
# - 结束总结
```

### 示例 3: 四力诊断与策略建议

```python
# 创建四力分析
profile = ForcesProfile()

# 添加力量
profile.add("push", "external", "市场竞争加剧，用户流失加速", intensity=4)
profile.add("push", "internal", "产品迭代慢，用户抱怨增多", intensity=3)

profile.add("pull", "external", "竞品推出 AI 智能推荐功能", intensity=5)
profile.add("pull", "external", "新进入者价格战激烈", intensity=4)

profile.add("anxiety", "choice", "担心功能变更影响用户体验", intensity=3)
profile.add("anxiety", "inertia", "团队对新技术有抵触", intensity=2)

profile.add("inertia", "internal", "现有技术债务重", intensity=4)
profile.add("inertia", "internal", "组织流程复杂，决策慢", intensity=3)

# 生成诊断
print(profile.summary())
print(profile.diagnose())

# 输出诊断：
# - 推力分析：外部竞争压力 > 内部问题
# - 拉力分析：竞品创新是最大威胁
# - 焦虑分析：变革风险可控
# - 惯性分析：技术债务是主要阻力
# - 策略建议：优先解决技术债务，快速跟进 AI 功能
```

### 示例 4: 创新机会发现

```python
# 创建创新发现器
finder = InnovationFinder()

# 添加补偿行为信号
finder.add_signal(
    signal_type="compensating_behavior",
    observation="用户用 Excel 手动追踪订单状态",
    potential_job="实时掌握订单进度"
)

finder.add_signal(
    signal_type="workaround",
    observation="用户截图保存订单信息",
    potential_job="方便分享和报销"
)

# 添加创新机会
finder.add_opportunity(
    name="自动订单追踪",
    description="提供实时订单状态推送和可视化时间线",
    feasibility=4,  # 1-5 分
    impact=5,
    linked_job="实时掌握订单进度"
)

finder.add_opportunity(
    name="一键报销单生成",
    description="自动生成符合公司要求的报销单据",
    feasibility=3,
    impact=4,
    linked_job="方便分享和报销"
)

# 生成创新报告
print(finder.render_markdown())

# 输出包含：
# - 创新信号汇总
# - 机会评估矩阵
# - 优先级排序
# - 实施检查清单
```

## 🔗 相关技能 (Related Skills)

本技能是 **AliDujie 技能生态系统** 的需求洞察核心，可与以下技能配合使用：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
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
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **JTBD + UDM** → 用 UDM 的访谈方法收集 JTBD 分析所需的用户故事和数据
- **JTBD + VPD** → 将 JTBD 洞察直接输入到价值主张画布的客户概况
- **JTBD + Persona** → 基于 JTBD 任务和目标创建更精准的人物角色
- **JTBD + QuantUX** → 量化验证 JTBD 假设和机会市场规模
- **JTBD + SWD** → 将 JTBD 研究发现用故事方式呈现，提升共情

👉 **探索完整生态系统**: [通用设计方法](../universal-design-methods/) | [价值主张设计](../value-proposition-design/) | [量化 UX 研究](../quantitative-ux-research/) | [人物角色](../web-persona-skill/) | [数据叙事](../storytelling-with-data/)

## 🌟 为什么选择 AliDujie 技能生态系统？(Why Choose AliDujie Skill Ecosystem?)

本技能是 **AliDujie 技能生态系统** 的重要组成部分。使用完整生态系统可获得：

- ✅ **完整覆盖** — 从用户研究到产品设计到数据呈现，全流程工具支持
- ✅ **无缝集成** — 所有技能使用一致的 API 设计和数据格式
- ✅ **最佳实践** — 基于经典理论和实战经验，避免常见陷阱
- ✅ **持续更新** — 活跃维护，定期添加新功能和改进
- ✅ **零依赖** — 纯 Python 标准库，开箱即用，无需复杂安装
- ✅ **双语支持** — 完整中英文文档，支持国际化团队协作

👉 **探索更多技能**: [通用设计方法](../universal-design-methods/) | [价值主张设计](../value-proposition-design/) | [量化 UX 研究](../quantitative-ux-research/) | [人物角色](../web-persona-skill/) | [数据叙事](../storytelling-with-data/)

## 📁 文件结构 (File Structure)

```
jtbd-knowledge-skill/
├── SKILL.md                    # Skill 定义文件
├── README.md                   # 本文件
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
├── 10-two-models.md            # 两种 JTBD 模型对比
└── 11-quick-reference.md       # 速查手册
```

## 🤝 最佳实践 (Best Practices)

### 1. JTBD 陈述格式

使用标准格式确保清晰和可执行：

```
Help me [做什么]
So that [达到什么目的/进步]
Context: [使用场景和约束]
```

**好的例子：**
> Help me 在出差时快速找到合适的住处  
> So that 可以专注于工作而不是为住宿烦恼  
> Context: 商务出差，时间紧张，对价格不敏感

**避免：**
> Help me 预订酒店 (太表面，未揭示真正目的)

### 2. 四力访谈技巧

- **推力** — "之前用什么？有什么不满？"
- **拉力** — "什么吸引你尝试新方案？"
- **焦虑** — "担心什么？什么让你犹豫？"
- **惯性** — "为什么没早点换？什么让你留下？"

### 3. 创新信号识别

| 信号类型 | 说明 | 示例 |
|----------|------|------|
| Compensating Behavior | 用户自己拼凑解决方案 | 用 Excel 追踪订单 |
| Workaround | 绕过产品限制的变通方法 | 截图保存信息 |
| Unmet Need | 明确表达但未满足的需求 | "要是有 X 功能就好了" |
| Emotional Trigger | 强烈情绪反应的点 | "这个太让人沮丧了" |

### 4. 机会评估维度

- **可行性 (Feasibility)** — 技术可实现性 (1-5 分)
- **影响力 (Impact)** — 对用户进步的帮助 (1-5 分)
- **差异化 (Differentiation)** — 与竞品的区别程度
- **战略契合 (Strategic Fit)** — 与公司战略的一致性

## 🛠️ 故障排查 (Troubleshooting)

### 问题 1: JTBD 陈述过于表面

**原因**: 描述的是功能而非进步

**解决**:
- 追问"so that"部分，挖掘真正目的
- 使用"当...我想...以便..."句式
- 避免功能描述，聚焦用户进步

```python
# 表面描述 (避免)
analyzer.add_statement("Help me", "预订酒店", "...")

# 深度描述 (推荐)
analyzer.add_statement(
    "Help me", "在出差时快速找到合适的住处",
    "So that", "可以专注于工作而不是为住宿烦恼"
)
```

### 问题 2: 四力分析不平衡

**检查**:
- 是否遗漏了某些力量类型
- 强度评分是否合理 (1-5 分)
- 是否有具体证据支持

### 问题 3: 创新机会可行性评估困难

**解决**:
- 与技术团队讨论实现难度
- 参考类似功能的实现成本
- 使用 MVP 方式验证可行性

## 📚 相关资源 (Additional Resources)

- **[INSTALL.md](./INSTALL.md)** — 详细安装指南和配置说明
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** — 贡献指南
- **[CHANGELOG.md](./CHANGELOG.md)** — 版本更新日志
- **[Knowledge Base](./)** — 11 篇完整 JTBD 知识库文档
- **[SKILL.md](./SKILL.md)** — 完整技能定义和 API 文档

## 👥 社区与支持 (Community & Support)

- **问题反馈**: 在 GitHub Issues 中报告问题或提出建议
- **贡献代码**: 阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解如何贡献
- **更新通知**: Star 仓库获取最新更新通知

## 📝 更新日志 (Changelog)

- **v1.0** — 初始版本，4 大核心组件
- **v1.1** — 添加创新发现引擎、知识库搜索
- **v1.2** — 增强四力诊断、添加最佳实践和故障排查

## 📄 许可 (License)

本技能仅供内部学习和研究使用。

## 👥 作者 (Credits)

- 基于《When Coffee and Kale Compete》(2nd Edition) by Alan Klement
- 技能开发：AliDujie 团队
