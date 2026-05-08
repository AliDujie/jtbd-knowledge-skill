# Installation Guide / 安装指南 — JTBD Knowledge Skill

## Prerequisites / 前置要求

- Python 3.8 or higher / Python 3.8 或更高版本
- Git

## Installation Steps / 安装步骤

### Option 1: OpenClaw Skills Directory (Recommended) / 方式一：OpenClaw 技能目录（推荐）

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/jtbd-knowledge-skill.git

# Copy to your OpenClaw skills directory / 复制到 OpenClaw 技能目录
cp -r jtbd-knowledge-skill ~/.openclaw/skills/
```

### Option 2: Custom Skills Directory / 方式二：自定义技能目录

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/jtbd-knowledge-skill.git

# Copy to your agent's skills directory / 复制到你的 Agent 技能目录
cp -r jtbd-knowledge-skill /your/agent/skills/
```

### Option 3: As a Python Package / 方式三：作为 Python 包安装

```bash
cd jtbd-knowledge-skill
pip install -e .
```

## Verify Installation / 验证安装

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDSkill, JTBDAnalyzer, InterviewBuilder, ForcesProfile

# Quick test / 快速测试
skill = JTBDSkill("Test Product")
print("JTBD Knowledge Skill installed successfully! ✓")
# JTBD 知识技能安装成功！✓
```

## Dependencies / 依赖

- Python >= 3.8
- **No external dependencies** (pure standard library) / **无外部依赖**（纯标准库）
- Compatible with macOS, Linux, and Windows / 兼容 macOS、Linux 和 Windows

## Troubleshooting / 故障排查

| Issue / 问题 | Solution / 解决方案 |
|-------|----------|
| `ModuleNotFoundError: No module named 'jtbd'` | Ensure the skill directory is in your Python path / 确保技能目录在 Python 路径中 |
| Import errors / 导入错误 | Verify Python version is 3.8+ / 确认 Python 版本为 3.8+ |
| Permission denied / 权限被拒绝 | Check file permissions on the skill directory / 检查技能目录的文件权限 |

## Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem:
本技能是 AliDujie UX 研究生态系统的一部分：

- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — JTBD 访谈可用 UDM 方法收集数据
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — JTBD 机会评分可用 QuantUX 定量验证
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — JTBD 发现的"工作"映射到 VPD 画布
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — JTBD 细分可与 Persona 角色结合
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — JTBD 分析结果可交给 SWD 进行数据叙事
