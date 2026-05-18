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

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
