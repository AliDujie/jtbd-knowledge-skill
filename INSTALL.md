# Installation Guide | 安装指南

[English](#english) | [中文](#中文说明)

---

## 中文说明

### 方式 1: 作为 AI Skill 安装 (推荐)

```bash
# 将技能复制到你的 AI Agent 系统
cp -r ~/.agents/skills/jtbd-knowledge-skill ~/.aoneclaw/skills/

# 验证安装
ls ~/.aoneclaw/skills/jtbd-knowledge-skill
```

### 方式 2: 作为 Python 包使用

#### 步骤 1: 克隆或复制代码

```bash
# 选项 A: 直接从源码使用
cd ~/.agents/skills/jtbd-knowledge-skill

# 选项 B: 克隆到你的项目
git clone <repo-url> your-project/jtbd
```

#### 步骤 2: 添加到 Python 路径

```python
# 方法 1: 在代码中添加路径
import sys
sys.path.insert(0, "/Users/dujie/.agents/skills/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 方法 2: 使用 PYTHONPATH 环境变量
export PYTHONPATH="$HOME/.agents/skills/jtbd-knowledge-skill:$PYTHONPATH"
python -c "from jtbd import JTBDAnalyzer; print('安装成功!')"
```

#### 步骤 3: (可选) 本地安装

```bash
# 使用 pip 安装为本地包
cd ~/.agents/skills/jtbd-knowledge-skill
pip install -e .

# 验证安装
python -c "from jtbd import JTBDAnalyzer; analyzer = JTBDAnalyzer('测试'); print('✓ 安装成功')"
```

### 系统要求

| 组件 | 版本要求 | 说明 |
|------|---------|------|
| Python | 3.8+ | 纯标准库，无需额外依赖 |
| 操作系统 | macOS / Linux / Windows | 跨平台支持 |
| 内存 | ≥512MB | 处理知识库文档 |

### 验证安装

```python
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile

# 测试 JTBD 分析
analyzer = JTBDAnalyzer("旅行预订平台")
analyzer.add_statement(
    main_verb="Help me",
    object="快速找到合适的住处",
    so_that="专注于工作"
)
analyzer.add_force("push", "频繁出差找酒店耗时", intensity=4)
analyzer.add_force("pull", "希望有可靠的预订平台", intensity=5)
report = analyzer.generate_report()
print(f"✓ JTBD 报告：{len(report)} 字符")

# 测试访谈框架
builder = InterviewBuilder("用户访谈")
builder.set_context("过去 3 个月使用过竞品的用户")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
guide = builder.build()
print(f"✓ 访谈提纲：{len(guide['questions'])} 个问题")

# 测试四力分析
profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧", intensity=4)
print(f"✓ 四力分析：{profile.summary()}")

print("\n🎉 安装成功！所有功能正常。")
```

### 故障排除

| 问题 | 解决方案 |
|------|---------|
| `ModuleNotFoundError: No module named 'jtbd'` | 确保路径已添加到 sys.path 或 PYTHONPATH |
| 中文输出乱码 | 确保终端使用 UTF-8 编码 |
| JTBD 陈述太宽泛 | 添加具体场景限定 (时间/地点/情境) |

---

## English

### Method 1: Install as AI Skill (Recommended)

```bash
# Copy skill to your AI Agent system
cp -r ~/.agents/skills/jtbd-knowledge-skill ~/.aoneclaw/skills/

# Verify installation
ls ~/.aoneclaw/skills/jtbd-knowledge-skill
```

### Method 2: Use as Python Package

#### Step 1: Clone or Copy Code

```bash
# Option A: Use directly from source
cd ~/.agents/skills/jtbd-knowledge-skill

# Option B: Clone to your project
git clone <repo-url> your-project/jtbd
```

#### Step 2: Add to Python Path

```python
# Method 1: Add path in code
import sys
sys.path.insert(0, "/Users/dujie/.agents/skills/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# Method 2: Use PYTHONPATH environment variable
export PYTHONPATH="$HOME/.agents/skills/jtbd-knowledge-skill:$PYTHONPATH"
python -c "from jtbd import JTBDAnalyzer; print('Installation successful!')"
```

#### Step 3: (Optional) Local Installation

```bash
# Install as local package with pip
cd ~/.agents/skills/jtbd-knowledge-skill
pip install -e .

# Verify installation
python -c "from jtbd import JTBDAnalyzer; analyzer = JTBDAnalyzer('Test'); print('✓ Installation successful')"
```

### System Requirements

| Component | Version | Description |
|-----------|---------|-------------|
| Python | 3.8+ | Pure standard library, no extra dependencies |
| OS | macOS / Linux / Windows | Cross-platform support |
| Memory | ≥512MB | For processing knowledge base documents |

### Verify Installation

```python
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile

# Test JTBD analysis
analyzer = JTBDAnalyzer("Travel Booking Platform")
analyzer.add_statement(
    main_verb="Help me",
    object="find suitable accommodation quickly",
    so_that="focus on work"
)
analyzer.add_force("push", "Frequent business trips require time finding hotels", intensity=4)
analyzer.add_force("pull", "Want a reliable booking platform", intensity=5)
report = analyzer.generate_report()
print(f"✓ JTBD report: {len(report)} characters")

# Test interview framework
builder = InterviewBuilder("User Interview")
builder.set_context("Users who used competitors in last 3 months")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
guide = builder.build()
print(f"✓ Interview guide: {len(guide['questions'])} questions")

# Test Four Forces analysis
profile = ForcesProfile()
profile.add("push", "external", "Market competition intensifying", intensity=4)
print(f"✓ Four Forces analysis: {profile.summary()}")

print("\n🎉 Installation successful! All features working.")
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'jtbd'` | Ensure path is added to sys.path or PYTHONPATH |
| Chinese characters display incorrectly | Ensure terminal uses UTF-8 encoding |
| JTBD statement too broad | Add specific context (time/place/situation) |

---

## Next Steps | 下一步

安装完成后，查看 [README.md](README.md) 获取快速开始指南，或阅读 [03-forces-of-progress.md](03-forces-of-progress.md) 深入了解四力模型。

After installation, check [README.md](README.md) for quick start guide, or read [03-forces-of-progress.md](03-forces-of-progress.md) for deep dive into Four Forces model.
