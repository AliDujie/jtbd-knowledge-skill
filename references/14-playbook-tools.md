# JTBD Playbook实践工具集

来源：Jim Kalbach《The Jobs to Be Done Playbook》

## 一、概述

本文档整合了Jim Kalbach在《The Jobs to Be Done Playbook》中介绍的实践工具、框架和配方。Kalbach的核心贡献在于他对多种JTBD方法论的整合——他不偏执于任何单一学派，而是根据不同场景推荐最适合的工具组合。他的整合观点是："我相信这两面并不互斥，两者都有其位置。有时从底层理解人们的目标和需求是有意义的（即ODI），例如在开发新产品或重新定义市场时。其他时候，从特定产品入手理解人们为何'雇用'该产品是合适的（即Switch）。"

## 二、Job Stories格式与四种变体

Job Stories是替代User Stories的一种需求描述格式，由Intercom产品团队首创。与User Stories关注角色不同，Job Stories关注情境；与User Stories预设解决方案不同，Job Stories保持解决方案无关性。

### 基本格式（Intercom版）

```
When [situation], I want to [motivation], so I can [expected outcome].
```

示例："When an important new customer signs up, I want to be notified so that I can start a conversation with that person."

### Kalbach结构化版

```
When I [circumstance + job stage/step], I want to [micro-job], so I can [need].
```

示例："When preparing for my commute and running late, I want to know the current weather along my journey so that I can minimize the chance of arriving wet."

### Andrea Hill版

```
When I [circumstance], I want to [solution capability], so I can [need].
```

显式从问题空间进入解决方案空间，适合已经明确解决方案方向的场景。

### Steph Troeth版

```
When I [circumstance], I want to [job], so that [benefit a solution offers].
```

将Job放在中间位置，结尾是解决方案提供的好处。

### Job Stories使用指南

每个项目或冲刺通常需要3到8个Job Stories。使用步骤：理解工作阶段和情境（基于之前的访谈和观察）；团队协作编写Job Stories；为Job Stories解题（可视化、头脑风暴、设计评审）。

Alan Klement的关键建议：避免模糊情境——不推荐"When I'm hungry..."，推荐"When I'm hungry, running late to get somewhere, not sure when I'm going to eat again, and worried that I'll soon be tired and irritable from hunger..."。情境越具体，Job Stories越有价值。

## 三、Value Proposition Canvas与JTBD的四步整合

Alexander Osterwalder的Value Proposition Canvas（VPC）与JTBD方法论可以结合使用，形成更完整的价值主张设计流程。

### Step 1 理解客户画像

列出主要工作及关键社会和情感方面（2到5个工作）。列出最重要的痛点（约12个）。列出收益（期望结果，独立于解决方案）。如果做过Switch访谈，用Four Forces分析来确定痛点和收益。

### Step 2 讨论解决方案画像

列出产品和服务。说明如何缓解痛点。说明如何创造收益。

### Step 3 确保契合

将痛点缓解者和收益创造者分别映射到痛点和收益。左侧匹配右侧即为问题-解决方案契合。

### Step 4 形成价值主张陈述

使用模板：

```
For [目标工作执行者]
who are dissatisfied with [当前替代方案],
our solution is a [产品或服务]
that provides [关键问题解决能力],
unlike [产品替代品].
```

## 四、消费链/消费旅程映射（12阶段）

消费旅程不同于Job Map。Job Map关注工作执行者独立于解决方案的工作流程，消费旅程关注客户与产品和品牌的互动关系。

### 消费旅程的12个阶段

Plan（计划）→ Discover（发现）→ Learn（学习）→ Decide（决定）→ Purchase（购买）→ Setup（设置）→ Use（使用）→ Modify（修改）→ Upgrade（升级）→ Renew（续约）→ Leave（离开）→ Return（返回）

### 创建消费旅程图的四个步骤

Step 1 启动项目——确定映射谁的旅程、映射哪些方面、旅程的边界。

Step 2 调查消费步骤——审查现有研究，直接与买家交谈（6人以上），发现消费工作序列、情绪、痛点和消费障碍。

Step 3 图解旅程——确定主要消费工作序列，添加体验细节（想法、情绪、痛点），先捕获as-is消费旅程。

Step 4 围绕消费旅程对齐——计划工作坊，参与创造性问题解决活动。

## 五、Hypothesis Progression Framework（假设递进框架）

由Lowdermilk和Rich开发的HPF提供了一种从宽泛到具体逐步验证假设的方法。四个阶段的假设递进：

### Customer假设

```
We believe [type of customers] are motivated to [motivation]
when doing [job to be done].
```

这是最宽泛的假设，用于验证目标客户和工作的基本假定。

### Problem假设

```
We believe [type of customers] are frustrated by [job to be done]
because of [problem].
```

在确认了客户和工作后，进一步验证具体的问题。

### Concept假设

```
We believe that [concept] will solve [problem]
and be valuable to [customers] while doing [job to be done].
```

验证解决方案概念是否能解决已确认的问题。

### Feature假设

```
We believe that [type of customers] will be successful solving [problem]
using [feature] while doing [job to be done].
```

验证具体的产品特性是否有效。

## 六、五种JTBD Recipes（配方）

Kalbach提供了五种针对不同场景的JTBD应用配方，每种配方是一个端到端的方法组合。

### Recipe 1：推出新产品

目标：发现未满足的需求并创建新产品。

流程：访谈（发现工作）→ Job Map（映射工作流程）→ 找未满足需求（ODI机会分数或定性判断）→ 创建价值主张（VPC四步法）→ 测试假设（HPF四阶段）。

### Recipe 2：优化现有产品

目标：改进现有产品以更好地满足客户工作。

流程：访谈（理解当前使用情况）→ 比较竞品（竞争分析）→ 创建消费旅程图（12阶段映射）→ 写Job Stories（3-8个）→ 创建路线图。

### Recipe 3：增加现有产品需求

目标：理解购买动机以增加市场需求。

流程：Switch访谈（理解购买时间线）→ Four Forces分析（推力、拉力、焦虑、惯性）→ 写Job Stories（基于力量分析）→ 建立路线图（针对性解决焦虑和惯性）。

### Recipe 4：让客户长期成功

目标：提高客户留存和成功率。

流程：访谈（理解客户的Job）→ Job Map（映射成功路径）→ 入职设计（Onboarding Matrix）→ 最大化留存（关键习惯识别）→ 提供支持（持续帮助客户实现进步）。

### Recipe 5：构建企业创新战略

目标：建立系统性的创新能力。

流程：访谈（多个目标市场）→ Job Map（跨市场映射）→ 找未满足需求（识别最大机会）→ 创建战略（增长策略矩阵）→ 围绕工作组织（团队重组）。

## 七、组织围绕JTBD重组

### 三步重组方法

**Step 1 将工作聚类为本地分组** 使用Job Map找到工作中的自然分界。可以看工作前、工作中、工作后的步骤。考虑相关工作如何相互影响。

**Step 2 围绕工作组织** 不必以JTBD作为主要组织向量。最简单的方式是将跨职能团队或工作组对齐到JTBD（二级或三级层面），类似Spotify模型中的guilds或chapters。

**Step 3 设定成功指标和测量标准** 赋予新团队"拥有"客户成功的使命。授权他们理解工作并想办法解决。

### 案例——Intercom

围绕4个核心工作组织产品：Acquire new customers（获取新客户）、Engage with existing customers（与现有客户互动）、Learn about customers（了解客户）、Support customers（支持客户）。JTBD渗透到产品、营销、研究、销售和支持。

### 案例——USAA Bank

消除了传统的产品P&L中心（支票账户、信用卡等）。围绕客户"体验"重组。没有产品负责人，而是"体验负责人"直接向总裁汇报。例如"日常消费体验负责人"同时负责支票账户和信用卡消费。

## 八、Onboarding Matrix（入职矩阵）

Alan Klement的2×2框架，用于设计新用户引导流程。

横轴：Solution Experience（解决方案经验）——高或低。

纵轴：Job Comprehension（工作理解）——高或低。

### 四种组合的入职策略

**高理解+高经验** 客户知道自己要什么也知道怎么用。策略：快速通道，减少引导步骤，让用户直接开始。

**高理解+低经验** 客户知道目标但不熟悉工具。策略：功能教程，帮助用户学会使用工具来完成已知的工作。

**低理解+高经验** 客户熟悉工具但不确定用它做什么。策略：价值展示，帮助用户发现工具能帮他们完成什么工作。

**低理解+低经验** 客户既不知道目标也不知道工具。策略：全面引导，从Job教育开始，再引入解决方案。

## 九、Fogg Behavior Model在JTBD中的应用

B.J. Fogg的行为模型认为行为发生需要三个要素同时满足：

**Motivation（动机）** 对应JTBD中的工作完成愿望——推力和拉力的总和。

**Ability（能力）** 对应执行工作的技能和资源——焦虑和惯性的反面。

**Prompts（触发器）** 对应触发目标行为的信号——时机、提醒、情境变化。

这个模型解释了"为什么客户知道有更好的方案但不行动"——可能是动机足够但能力不足（太复杂），也可能是动机和能力都够但缺少触发器（没有合适的时机）。

在JTBD实践中的应用：增强推力和拉力以提高动机；降低焦虑和惯性以提高能力；设计合适的触发器（入职流程、通知、情境提醒）。

## 十、Disruption Diagnostic（颠覆诊断）

Wessel和Christensen的颠覆诊断三步法，用于评估颠覆性威胁。

### Step 1 确定颠覆者的优势

颠覆者通常在价格、便利性或某个特定维度上有显著优势。他们的产品可能在大多数维度上"更差"，但在关键维度上"足够好"。

### Step 2 识别自身公司的相对优势

你有哪些颠覆者难以复制的优势？品牌、客户关系、专有技术、分销渠道、规模经济？

### Step 3 评估障碍

评估颠覆者面临的采用障碍有多大。如果障碍很低（如切换成本低、学习曲线平缓），威胁更紧迫。如果障碍很高（如需要行为改变、多决策者），你有更多时间应对。

### 案例——Skype vs 传统视频会议

2003年推出时功能有限、质量差，但免费。老牌公司（WebEx、GoToMeeting）忽视了这个威胁。到2011年，Microsoft以85亿美元收购Skype。经典颠覆路径：从低端市场进入，逐步改善质量，最终占领主流市场。

## 十一、增长策略矩阵

基于Tony Ulwick提出的两个维度（完成工作的能力和解决方案成本）：

**Differentiated（差异化）** 更好更贵。目标服务不足的客户。案例：Nest恒温器、Nespresso、Whole Foods。

**Dominant（主导）** 更好更便宜。目标所有客户。案例：UberX、Netflix。最难实现但回报最高。

**Disruptive（颠覆性）** 更差更便宜。目标被过度服务的客户和非消费者。案例：Google Docs、TurboTax、eTrade。

**Discrete（离散）** 特定场景解决方案。目标选择有限的客户。案例：高速公路休息站、体育场小卖部。

**Sustaining（维持）** 中间区域改进。目标现有客户。大多数公司的默认策略。

策略动态性：产品位置随时间变化。Uber从差异化（Uber Black）到主导（UberX）到颠覆（Uber Pool）。

## 十二、实践案例集

### GoToWebinar

4阶段JTBD流程：发现工作（8次深度访谈）→ 验证需求陈述（6次验证访谈，约50条）→ 优先排序需求（ODI调查）→ 转化为行动（定价、营销、路线图）。领导层只有1人正确猜中了前5大未满足需求中的2个。

### MURAL

5步产品路线图流程：创建Job Map（8阶段加多步骤）→ 基于机会决定构建内容（每季度）→ 研究具体工作（定性加定量）→ 创建Job Stories → 设计和开发功能（分阶段发布）。

### Trulia

从30多个概念出发，提取工作陈述，用重要性-满意度矩阵调查。首要未满足需求：理解从住在那里的人的角度了解社区。开发UGC策略，每天收集10万条以上社区反馈。

### CarMax

从"改善照片质量"转向"理解人们雇用照片做什么工作"。发现用户在方向盘照片上停留很久——想确认是否有蓝牙。将功能展示从文字列表改为缩略图照片，A/B测试显示业务指标提升。

### Bidsketch

使用反向Switch访谈进行取消研究。发现主要情感工作是给客户信心。行动：在每个产品步骤提供设计信心，识别早期取消信号。

### Airbnb

从"预订住宿"扩展到"旅行"。Rebecca Sinclair说"We started to say the product is the trip"。推出Airbnb Experiences（城市旅游、烹饪课、博物馆参观等）。
