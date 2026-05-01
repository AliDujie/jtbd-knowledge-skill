# Installation Guide — JTBD Knowledge Skill

## Prerequisites

- Python 3.8 or higher
- Git

## Installation Steps

### Option 1: OpenClaw Skills Directory (Recommended)

```bash
# Clone the repository
git clone https://github.com/AliDujie/jtbd-knowledge-skill.git

# Copy to your OpenClaw skills directory
cp -r jtbd-knowledge-skill ~/.openclaw/skills/
```

### Option 2: Custom Skills Directory

```bash
# Clone the repository
git clone https://github.com/AliDujie/jtbd-knowledge-skill.git

# Copy to your agent's skills directory
cp -r jtbd-knowledge-skill /your/agent/skills/
```

### Option 3: As a Python Package

```bash
cd jtbd-knowledge-skill
pip install -e .
```

## Verify Installation

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDSkill, JTBDAnalyzer, InterviewBuilder, ForcesProfile

# Quick test
skill = JTBDSkill("Test Product")
print("JTBD Knowledge Skill installed successfully! ✓")
```

## Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Compatible with macOS, Linux, and Windows

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'jtbd'` | Ensure the skill directory is in your Python path |
| Import errors | Verify Python version is 3.8+ |
| Permission denied | Check file permissions on the skill directory |
