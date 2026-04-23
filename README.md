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

## 实际案例

### 案例 1：出行平台 JTBD 分析

```python
from jtbd import JTBDAnalyzer

analyzer = JTBDAnalyzer("出行预订平台")
analyzer.add_statement(
    context="出差时",
    motivation="快速找到合适的住宿",
    expected_outcome="专注工作不为住宿烦恼"
)
analyzer.add_force("push", "每次找酒店花15分钟对比", intensity=4)
analyzer.add_force("pull", "竞品有一键预订功能", intensity=5)
analyzer.add_force("anxiety", "担心迁移到新平台的学习成本", intensity=3)

report = analyzer.generate_report()
print(report)
# 机会分数: 8.2/10 → 高优先级改进方向
```

### 案例 2：访谈提纲生成

```python
from jtbd import InterviewBuilder

builder = InterviewBuilder("商务用户住宿体验访谈")
builder.include_dimensions(["competition", "push", "pull", "anxiety"])
questions = builder.build()
print(InterviewBuilder.render_markdown(questions))
# 输出结构化访谈提纲，覆盖 4 个维度共 12 个问题
```

### 案例 3：四力诊断与增长策略

```python
from jtbd import ForcesProfile, InnovationFinder

profile = ForcesProfile()
profile.add("push", "external", "市场竞争加剧，用户流失", intensity=4)
profile.add("pull", "external", "竞品推出 AI 推荐功能", intensity=5)
profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
profile.add("habit", "internal", "用户已习惯现有流程", intensity=4)

diagnosis = profile.diagnose()
print(f"净推动力: {diagnosis.net_force:.2f}")
# 净推动力 < 0 → 需要增强 pull 或减少 anxiety
```

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| JTBD 陈述过于模糊 | 缺少情境要素 | 检查三要素：情境(Context)+动机(Motivation)+期望结果 |
| 机会分数计算异常 | 重要度/满意度评分范围不一致 | 确保使用 1-5 量表，检查异常值 |
| 四力分析结果不均衡 | 只关注单一力量 | 同时评估 push/pull/anxiety/habit 四力 |
| 访谈问题缺乏深度 | 维度覆盖不足 | 使用 include_dimensions 覆盖全部 4 个维度 |

## 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《When Coffee and Kale Compete》 | Alan Klement | 全书方法论基础 |
| 《Competing Against Luck》 | Clayton Christensen | JTBD 理论起源 |
| 《Jobs to Be Done Playbook》 | Jim Kalbach | 实操指南与模板 |
| 《Demand-Side Sales 101》 | Bob Moesta | 销售视角的 JTBD |

## 技能生态导航

与其他 AliDujie 技能协同使用，构建完整用户体验研究体系：

| 关联技能 | 协同场景 | 工作流示例 |
|----------|----------|------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | JTBD 洞察验证 | JTBD 发现需求 → UDM 研究方法验证 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | JTBD 结果可视化 | JTBD 分析 → SWD 图表呈现给利益相关方 |
| [Quantitative UX Research](https://github.com/AliDujie/quantitative-ux-research) | 定量验证机会分数 | JTBD 机会评分 → QuantUX 统计检验 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | JTBD → 价值主张映射 | JTBD 发现 → VPD 画布填充 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | JTBD 驱动角色细分 | JTBD 任务聚类 → Persona 角色定义 |

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

## 许可

基于《When Coffee and Kale Compete》(2nd Edition) by Alan Klement。

v2.0.0

---

*Last Updated: 2026-04-23 | AliDujie Skill Ecosystem*
