# JTBD (Jobs to Be Done) Knowledge Skill v3.0

> **Understand What Users Really Hire Your Product to Do.**

![Version](https://img.shields.io/badge/version-3.1.79-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)

A complete JTBD toolkit fusing **four schools of thought** — Klement's Forces of Progress, Ulwick's ODI (Opportunity-Driven Innovation), Wunker's Jobs Atlas, and Kalbach's Job Stories — with **13 executable capabilities** and **15 methodology knowledge documents**. Covers the full workflow: interviews → surveys → scoring → prioritization → competition → marketing → growth → Jobs Atlas, plus CEO-level market sizing and commercialization analysis.

## 🌟 Why JTBD?

| Challenge | Without JTBD | With JTBD |
|-----------|-------------|----------|
| Need Insights | "Users say they want X" — surface feedback | "They hire it to accomplish Y" — deep insight |
| Feature Priorities | Guesswork or HiPPO decisions | Opportunity scoring + data-driven ranking |
| Competitive Analysis | Feature comparison checklist | Jobs-based alternative landscape |
| Innovation Direction | Copy competitor features | Identify underserved high-opportunity Jobs |
| Marketing Messaging | Generic value propositions | Precision messaging from Switch interviews |

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r jtbd-knowledge-skill /your/agent/skills/
```

### Use in Python

```python
from jtbd import JTBDSkill

skill = JTBDSkill("Travel Booking Platform")

# 1. Score a job opportunity (4-dimension model)
score = skill.score_opportunity(
    "Find suitable accommodation quickly",
    struggle=4, alternative=3, market=4, budget=4
)
# → Score: 7.6 / 10

# 2. ODI dual-track scoring
odi = skill.score_odi("Find suitable accommodation quickly", importance=8, satisfaction=3)
# → Opportunity Score: 13 (high opportunity area)

# 3. Four forces analysis — why users switch
forces = skill.analyze_forces("Users switching from competitor to our product")
# Push: What's wrong with current solution
# Pull: What's attractive about new solution
# Anxiety: What worries them about switching
# Habit: What keeps them anchored to current

# 4. Generate Switch interview guide
guide = skill.generate_interview("User Switch Interview", ["competition", "push", "anxiety"])
print(guide)

# 5. Create Jobs Atlas (7 dimensions)
atlas = skill.create_jobs_atlas("Travel Booking Platform")
atlas.set_core_job("Quickly find suitable accommodation during business trips")
atlas.add_related_job("Manage travel budget")
atlas.add_driver("circumstances", "Urgent business trip, tight schedule", influence_level=4)
print(atlas.build())

# 6. Priority matrix for multiple Jobs
skill.add_job_to_matrix("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4, importance=8, satisfaction=3)
skill.add_job_to_matrix("Compare prices easily", struggle=3, alternative=2, market=5, budget=3, importance=7, satisfaction=5)
print(skill.render_priority_matrix())

# 7. Full analysis with CEO decision support
report = skill.analyze(include_ceo_analysis=True)
# → Standard report + market sizing + priority scoring + commercialization feasibility
```

**Zero dependencies** — pure Python standard library. No `pip install` needed.

## 🧩 13 Capabilities

| # | Capability | Key Methods |
|---|-----------|-------------|
| 1 | **Interview Guide Generation** | Switch, ODI, Churn interview types |
| 2 | **Survey Design** | Screening, validation, competitive, ODI outcome pairing, Job scoring |
| 3 | **Opportunity Scoring** | 4-dimension model (30/25/25/20%) + ODI algorithm |
| 4 | **Priority Matrix** | Multi-Job normalization, four-forces analysis, ranked output |
| 5 | **Competitive Analysis** | Direct/indirect/non-consumption, Outcome comparison, disruption diagnosis |
| 6 | **Marketing Copy Generation** | Struggle resonance → progress vision → anxiety removal → inertia override → CTA |
| 7 | **Growth & Retention Strategy** | Upstream/downstream/lateral growth, 3 churn reasons, ODI 5-strategy matrix |
| 8 | **JTBD Description Generation** | Klement / Outcome / Job Story / Traditional — 4 formats |
| 9 | **Universal Job Map** | 8-stage Ulwick map with importance/satisfaction per stage |
| 10 | **Desired Outcome Statements** | Ulwick standard format with minimize/increase directions |
| 11 | **Job Stories Generation** | Classic / Anxious / Force / Context-Rich — 4 variants |
| 12 | **Adoption Obstacle Diagnosis** | Awareness / value clarity / trust / switching cost / complexity |
| 13 | **Jobs Atlas (7 Dimensions)** | Core functional, related, emotional, social, financial, consumption chain, context |

### CEO Extensions

| Method | Output |
|--------|--------|
| `generate_market_size_estimate(jobs)` | TAM/SAM/SOM derivation, key assumptions, phased validation plan |
| `generate_priority_scoring(jobs)` | Composite opportunity scoring, P0/P1/P2 resource allocation |
| `generate_commercialization_feasibility(jobs)` | WTP, ROI, payback period, Go/No-Go decision |

## 🔄 Four Schools of Progress

| School | Key Concepts | JTBD Methods |
|--------|-------------|-------------|
| **Klement** | Forces of Progress, Switch Interviews | Push/Pull/Anxiety/Habit, struggle moment, emotional progress |
| **Ulwick ODI** | Opportunity Algorithm, Universal Job Map | Outcome scoring, Job Map 8 stages, desired outcome statements |
| **Wunker** | Jobs Atlas, ABC Drivers | 7-dimension panorama, Attitude/Background/Circumstance |
| **Kalbach** | Job Stories, VPC Integration | When...I want to...So I can... format, multi-format descriptions |

## 🌐 Ecosystem Integration

JTBD is the **need insight layer** — it sits after Persona definition and before VPD canvas filling:

```
Persona → JTBD → UDM → QuantUX → VPD → SWD → STM
            ↑ You are here
```

| Upstream | Downstream | Collaboration |
|----------|-----------|---------------|
| Persona (user segments) | JTBD (Job clustering) | Persona segments → JTBD task clustering |
| JTBD (Jobs discovery) | VPD (canvas filling) | JTBD Jobs → VPD canvas mapping |
| JTBD (opportunity scores) | QuantUX (A/B validation) | JTBD scores → QuantUX experiment design |
| JTBD (interview findings) | UDM (method validation) | JTBD hypotheses → UDM interview validation |
| JTBD (insights) | SWD (data storytelling) | JTBD findings → SWD executive presentation |

Cross-skill example:
```python
# JTBD → VPD → QuantUX end-to-end
from jtbd import JTBDSkill
from vpd import VPDSkill
from quantux import QuantUXSkill

jtbd = JTBDSkill("Travel Booking")
opportunity = jtbd.score_opportunity("Find hotel quickly", struggle=4, alternative=3, market=4, budget=4)

vpd = VPDSkill("Travel Booking", "Business Travelers")
canvas = vpd.analyze_canvas(product_name="Travel Booking", jobs=[{"description": "Find hotel quickly"}])

quantux = QuantUXSkill("Travel Booking")
n = quantux.calculate_ab_sample_size(0.35, 0.03)
```

## 📖 Knowledge Base (15 Documents)

| File | Topic | Key Content |
|------|-------|------------|
| `references/01-theory-foundation.md` | Theory foundation | Klement JTBD definition vs traditional requirements |
| `references/02-principles.md` | Core principles | 9 principles with实战 applications |
| `references/03-forces-of-progress.md` | Forces of Progress model | Four forces, subtypes, diagnostic methods |
| `references/04-system-of-progress.md` | System of Progress | Complete System of Progress framework |
| `references/05-research-methods.md` | Research methods | Interview design, survey design, observation |
| `references/06-analysis-framework.md` | Analysis framework | Opportunity scoring, priority matrix, scenario layering |
| `references/07-innovation-guide.md` | Innovation guide | Innovation signal identification, compensatory behavior |
| `references/08-business-decisions.md` | Business decisions | Competitive analysis, marketing copy, growth strategy |
| `references/09-case-studies.md` | Case studies | Classic JTBD case analysis |
| `references/10-two-models.md` | Two models comparison | Klement vs Moesta-Ulwick differences |
| `references/11-quick-reference.md` | Quick reference | All concepts and formulas summary |
| `references/12-odi-methodology.md` | ODI methodology | Ulwick algorithm, Job Map, Outcome Statements |
| `references/13-jobs-atlas.md` | Jobs Atlas | Wunker 7 dimensions, ABC Drivers |
| `references/14-playbook-tools.md` | Playbook tools | Job Stories templates, obstacle checklists |
| `references/15-glossary.md` | Glossary | Four-school core terms (CN/EN bilingual) |

## 📁 Project Structure

```
jtbd-knowledge-skill/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── references/           # 15 knowledge base documents
├── jtbd/                 # Python executable toolkit
│   ├── __init__.py       # JTBDSkill unified entry point
│   ├── config.py         # Runtime configuration
│   ├── jtbd_analyzer.py  # JTBD description management (4 formats), four-forces
│   ├── interview_generator.py  # Switch/ODI/Churn interview guides
│   ├── survey_generator.py     # 5 survey types (incl. ODI pairing)
│   ├── priority_calculator.py  # 4-dimension scoring + ODI algorithm
│   ├── competition.py          # Competitive analysis + outcome comparison
│   ├── marketing.py            # Marketing copy + VPC integration
│   ├── growth.py               # Growth strategy + ODI 5-strategy matrix
│   ├── forces.py               # Push/Pull/Anxiety/Habit structured analysis
│   ├── innovation.py           # Innovation signals, compensatory behavior
│   ├── job_map.py              # Universal Job Map 8-stage builder
│   ├── outcome_statement.py    # Desired Outcome Statement management
│   ├── job_stories.py          # Job Stories 4 variants
│   ├── obstacles.py            # Adoption/usage obstacle diagnosis
│   ├── jobs_atlas.py           # Jobs Atlas 7 dimensions + ABC Drivers
│   ├── templates.py            # Templates
│   ├── utils.py                # Knowledge base utilities
│   └── tests/
│       └── test_all.py   # Test suite
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Testing

```bash
cd jtbd-knowledge-skill
python jtbd/tests/test_all.py
# Or with pytest:
python -m pytest jtbd/tests/test_all.py -v
```

## 📋 When NOT to Use JTBD

- **Choosing research methods or designing interviews** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Statistical analysis or A/B testing** → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Creating user personas** → [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Value proposition canvas analysis** → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **Data visualization & storytelling** → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **When Coffee and Kale Compete** | Alan Klement (2023) | Foundation — JTBD four-school fusion |
| Competing Against Luck | Clayton Christensen (2016) | JTBD theory foundation |
| Demand-Side Sales | Bob Moesta (2021) | Switch interviews, Forces of Progress |
| Jobs to Be Done | Tony Ulwick (2016) | ODI methodology, opportunity algorithm |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | JTBD market sizing → CEO investment decisions |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | JTBD opportunity scores → CPO roadmap adjustment |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | JTBD competitive analysis → CMO brand differentiation |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | JTBD findings → CEO plan review & 10x opportunity |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
