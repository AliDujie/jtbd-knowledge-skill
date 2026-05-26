# JTBD Knowledge Skill — Runnable Examples

Zero-dependency Python examples demonstrating JTBD capabilities. Each script is standalone.

## Quick Start

```bash
PYTHONPATH=. python examples/01_opportunity_scoring.py
PYTHONPATH=. python examples/02_four_forces.py
PYTHONPATH=. python examples/03_job_stories.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_opportunity_scoring.py` | ODI opportunity scoring with decision thresholds |
| `02_four_forces.py` | Four Forces of Progress analysis (push, pull, anxiety, habit) |
| `03_job_stories.py` | Job Stories generation with context and desired outcomes |

## Try Before You Decide

```bash
PYTHONPATH=. python -c "
from jtbd import JTBDSkill
skill = JTBDSkill('My Product')
score = skill.score_opportunity('Quick onboarding', importance=9, satisfaction=3)
print(score)
"
```
