# JTBD (Jobs to Be Done) Knowledge Skill — Usage Guide

> JTBD 需求洞察 · 使用指南

## 📐 Where JTBD Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
                  ↑
            JTBD sits here
```

- **After** Persona defines who the users are
- **Before** UDM recommends research methods and VPD maps value propositions
- **JTBD** discovers what users are really trying to accomplish (Jobs)

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
cp -r jtbd-knowledge-skill /your/agent/skills/
python -c "from jtbd import JTBDSkill; print(JTBDSkill('My Product').score_opportunity('Core Job', struggle=4, alternative=3, market=4, budget=4))"
```

## 🔑 Core Workflows / 核心工作流

### 1. Opportunity Scoring / 机会评分

```python
from jtbd import JTBDSkill

jtbd = JTBDSkill("Travel Booking Platform")

# 4-dimension model (0-10 scale)
score = jtbd.score_opportunity(
    "Find suitable accommodation quickly",
    struggle=4, alternative=3, market=4, budget=4
)
# → Score: 7.6 / 10

# ODI dual-track scoring
odi = jtbd.score_odi("Find suitable accommodation quickly", importance=8, satisfaction=3)
# → Opportunity Score: 13 (high opportunity area)
```

### 2. Four Forces Analysis / 四力分析

```python
# Understand why users switch
forces = jtbd.analyze_forces("Users switching from competitor to our product")
# Push: What's wrong with current solution
# Pull: What's attractive about new solution
# Anxiety: What worries them about switching
# Habit: What keeps them anchored
```

### 3. Switch Interview / 转换访谈

```python
# Generate structured interview guide
guide = jtbd.generate_interview("Switch Interview", ["competition", "push", "anxiety"])
print(guide)
```

### 4. Jobs Atlas / Jobs Atlas 七维全景

```python
atlas = jtbd.create_jobs_atlas("Travel Booking Platform")
atlas.set_core_job("Quickly find suitable accommodation during business trips")
atlas.add_related_job("Manage travel budget")
atlas.add_driver("circumstances", "Urgent business trip, tight schedule", influence_level=4)
print(atlas.build())
```

### 5. Priority Matrix / 优先级矩阵

```python
jtbd.add_job_to_matrix("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4, importance=8, satisfaction=3)
jtbd.add_job_to_matrix("Compare prices easily", struggle=3, alternative=2, market=5, budget=3, importance=7, satisfaction=5)
print(jtbd.render_priority_matrix())
```

### 6. CEO Extensions / CEO 决策支持

```python
# Full analysis with market sizing + prioritization + commercialization
report = jtbd.analyze(include_ceo_analysis=True)
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| Identify underserved jobs | Score → Priority matrix | `score_opportunity()` → `render_priority_matrix()` |
| Competitive switching | Four forces → Switch interview | `analyze_forces()` → `generate_interview()` |
| Feature roadmap | ODI scoring → Priority | `score_odi()` → `add_job_to_matrix()` |
| Market sizing for investors | Jobs Atlas → Market estimate | `create_jobs_atlas()` → `generate_market_size_estimate()` |

## 🔗 Ecosystem Integration / 生态协作

```python
# Persona (who) → JTBD (what) → VPD (value) → SWD (present)
from persona import PersonaSkill
from jtbd import JTBDSkill
from vpd import VPDSkill
from swd import SWDSkill

persona = PersonaSkill("Travel Booking")
persona.add_persona(name="Alex", archetype="Business Traveler", priority="primary",
    goals=["Book hotel in under 30 seconds"], behaviors=["Last-minute bookings"])

jtbd = JTBDSkill("Travel Booking")
score = jtbd.score_opportunity("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4)

vpd = VPDSkill("Travel Booking", "Business Travelers")
canvas = vpd.analyze_canvas(product_name="Travel Booking",
    jobs=[{"description": "Find hotel quickly"}])

swd = SWDSkill("Q2 Review")
story = swd.build_story(protagonist="Product Committee",
    imbalance="Business travelers struggle with hotel booking",
    call_to_action="Prioritize one-click rebook in Q3")
```

## 🧪 Testing / 测试

```bash
cd jtbd-knowledge-skill
python jtbd/tests/test_all.py
```

## 🎯 When to Use Each JTBD School / 何时使用各学派

| School | When to Use | Key Method | Use It For |
|--------|------------|------------|------------|
| **Klement** — Forces of Progress | Understanding *why users switch* products or adopt new ones | `analyze_forces()` + `generate_interview()` | Competitive switching analysis, emotional progress mapping, identifying Push/Pull/Anxiety/Habit dynamics |
| **Ulwick ODI** — Outcome-Driven Innovation | *Quantitative* opportunity scoring, feature roadmaps, survey validation | `score_odi()` + `score_opportunity()` + `render_priority_matrix()` | Measuring underserved outcomes, P0/P1/P2 prioritization, Job Map 8-stage analysis |
| **Wunker** — Jobs Atlas | Holistic 360° view of a Job including social, emotional, financial, and consumption-chain dimensions | `create_jobs_atlas()` + `generate_market_size_estimate()` | Investor pitches, TAM/SAM/SOM sizing, ABC Driver segmentation, multi-stakeholder Jobs |
| **Kalbach** — Job Stories | Solution-agnostic requirement framing, agile user-story replacement, sprint planning | `create_jtbd_statement(format="job_story")` + job story generation | Writing testable Job Stories, VPC integration, When/I want to/So I can format |

| 学派 | 适用场景 | 核心方法 | 用于 |
|------|---------|---------|------|
| **Klement** — 进步力量 | 理解*用户为何切换*产品或采用新产品 | `analyze_forces()` + `generate_interview()` | 竞品切换分析、情感进步映射、推拉焦虑惯性动力学 |
| **Ulwick ODI** — 结果驱动创新 | *量化*机会评分、功能路线图、问卷验证 | `score_odi()` + `score_opportunity()` + `render_priority_matrix()` | 测量未满足结果、P0/P1/P2 优先级、Job Map 八阶段分析 |
| **Wunker** — Jobs Atlas | Job 的 360° 全景视角（社会、情感、财务、消费链维度） | `create_jobs_atlas()` + `generate_market_size_estimate()` | 融资路演、TAM/SAM/SOM 估算、ABC 驱动力细分、多利益相关者 Jobs |
| **Kalbach** — Job Stories | 无解决方案偏向的需求框架、替代敏捷用户故事、迭代规划 | `create_jtbd_statement(format="job_story")` + job story 生成 | 编写可测试的 Job Stories、VPC 集成、"当……我想要……以便……"格式 |

## 🔗 Related Skills in the Ecosystem / 生态系统中的相关技能

JTBD doesn't work in isolation — it's the **demand insight layer** that plugs into a broader research pipeline:

| Skill | Role | How It Connects with JTBD |
|-------|------|---------------------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Methodology core | UDM interviews generate raw data → JTBD structures Jobs and scores opportunities |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | User definition | JTBD task clusters inform Persona segment definition → Personas ground Jobs in real user profiles |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Quantitative validation | JTBD opportunity scores → QuantUX A/B tests and MaxDiff validate priorities |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Product-market fit | JTBD Jobs → VPD canvas filling → experiment validation |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data storytelling | JTBD insights → SWD chart selection → executive narrative |

> 💡 **Recommended chain:** Persona (define who) → JTBD (discover what Jobs) → VPD (map to canvas) → QuantUX (validate) → SWD (present to stakeholders)

### Quick Cross-Skill Example / 跨技能示例

```python
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

# JTBD discovers high-opportunity Jobs
jtbd = JTBDSkill("Travel Booking")
score = jtbd.score_opportunity("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4)

# VPD maps JTBD Jobs to Value Proposition Canvas
vpd = VPDSkill("Travel Booking", "Business Travelers")
vpd.analyze_canvas(product_name="Travel Booking",
    jobs=[{"description": "Find hotel quickly"}])

# QuantUX validates with A/B test
quantux = QuantUXSkill("Travel Booking")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)

# SWD presents to executives
swd = SWDSkill("Q2 JTBD Report")
story = swd.build_story(protagonist="Product Committee",
    imbalance="Business travelers struggle with booking",
    call_to_action="Prioritize one-click rebook")
```

## 🔗 Extended Ecosystem / 扩展生态

JTBD 需求洞察可与 AliDujie 管理层 Advisor 技能结合,将用户 Jobs 转化为商业决策:

| Extended Skill | Collaboration Scenario |
|---------------|------------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | JTBD market sizing → CEO investment decisions / JTBD 市场规模估算 → CEO 投资决策 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | JTBD opportunity scores → CPO roadmap adjustment / JTBD 机会评分 → CPO 产品路线图调整 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | JTBD competitive analysis → CMO brand differentiation / JTBD 竞争分析 → CMO 品牌差异化定位 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | JTBD tech-related Jobs → CTO technology investment priorities / JTBD 技术相关 Jobs → CTO 技术投资优先级 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | JTBD findings → CEO plan review & 10x opportunity / JTBD 发现 → CEO 计划审查与 10x 机会识别 |

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
