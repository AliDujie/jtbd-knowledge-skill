# JTBD Knowledge Skill

基于 Alan Klement《When Coffee and Kale Compete》的 JTBD (Jobs to Be Done) 理论与实践工具集。提供 9 项可执行能力和 11 篇方法论知识库，覆盖从用户访谈到竞争分析到增长策略的完整 JTBD 工作流。

## 快速开始

作为 Agent Skill 使用：将整个目录复制到你的 skills 目录即可。Agent 会自动读取 `SKILL.md` 获取执行指令。

作为 Python 包使用：

```python
import sys
sys.path.insert(0, "/path/to/jtbd-knowledge-skill")
from jtbd import JTBDAnalyzer, InterviewBuilder, ForcesProfile, InnovationFinder

# 创建 JTBD 分析
analyzer = JTBDAnalyzer("旅行预订平台")
analyzer.add_statement("Help me", "出差时快速找到合适住处", "专注工作不为住宿烦恼")
analyzer.add_force("push", "每次找酒店花15分钟", intensity=4)
analyzer.add_force("pull", "竞品有一键预订", intensity=5)
print(analyzer.generate_report())

# 生成访谈提纲
builder = InterviewBuilder("商务用户访谈")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
print(InterviewBuilder.render_markdown(builder.build()))

# 四力诊断
profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧", intensity=4)
profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
print(profile.diagnose())
```

## 核心能力

本 Skill 提供 9 项执行能力：生成访谈提纲、设计调查问卷、计算机会分数、输出优先级矩阵、竞争分析、营销文案生成、增长与留存策略、JTBD 描述生成与验证、场景库深度分析报告。详细说明见 `SKILL.md`。

Python API 包含 4 个核心组件：`JTBDAnalyzer`（分析引擎）、`InterviewBuilder`（访谈框架）、`ForcesProfile`（四力分析）、`InnovationFinder`（创新发现），以及 `JTBDSkill.analyze()` 一站式入口。纯标准库实现，无外部依赖。

## 文件结构

```
jtbd-knowledge-skill/
├── SKILL.md                       # Agent 入口文件（触发条件 + 能力说明 + API）
├── README.md                      # 本文件
├── pyproject.toml                 # Python 包构建配置
├── jtbd/                          # Python 包
│   ├── __init__.py                # API 入口与导出（含 JTBDSkill facade）
│   ├── analyzer.py                # JTBD 分析引擎
│   ├── interview.py               # 访谈框架生成器
│   ├── forces.py                  # 进步力量分析
│   ├── innovation.py              # 创新机会发现
│   ├── config.py                  # 运行时配置
│   ├── utils.py                   # 知识库加载与搜索
│   ├── templates.py               # 模板常量
│   └── tests/test_all.py          # 测试用例（14 cases）
└── references/                    # 知识库（11 篇方法论文档）
    ├── 01-theory-foundation.md    # 理论基础
    ├── 02-principles.md           # 九大原则
    ├── 03-forces-of-progress.md   # 进步力量模型
    ├── 04-system-of-progress.md   # 进步系统
    ├── 05-research-methods.md     # 信息采集方法
    ├── 06-analysis-framework.md   # 信息整理框架
    ├── 07-innovation-guide.md     # 创新指南
    ├── 08-business-decisions.md   # 业务决策
    ├── 09-case-studies.md         # 案例精华
    ├── 10-two-models.md           # Klement vs Moesta-Ulwick 对比
    └── 11-quick-reference.md      # 速查手册
```

## 运行测试

```bash
cd /path/to/jtbd-knowledge-skill
python3 -m pytest jtbd/tests/test_all.py -v
# 或使用内置 runner
python3 -c "from jtbd.tests.test_all import run_all_tests; run_all_tests()"
```

## 许可

基于《When Coffee and Kale Compete》(2nd Edition) by Alan Klement。

v2.0.0
