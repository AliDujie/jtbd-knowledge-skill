# JTBD Runnable Examples / 可运行示例

These examples demonstrate Jobs to Be Done capabilities with real-world scenarios.
这些示例用真实场景演示 JTBD 能力。

## Quick Start / 快速开始

```bash
cd examples/
python 01_interview_guide.py
python 01_opportunity_scoring.py
python 02_four_forces.py
python 02_opportunity_analysis.py
python 03_job_stories.py
```

All examples use **zero dependencies** — pure Python standard library only.
所有示例使用**零依赖** — 仅 Python 标准库。

## Available Examples / 可用示例

### 01_interview_guide.py
Switch interview guide generation with Forces of Progress framework.
生成基于"进步力量"框架的切换访谈提纲。

**Use when / 适用场景**: Conducting JTBD interviews to understand why users switch.

```bash
python 01_interview_guide.py
```

### 01_opportunity_scoring.py
Opportunity scoring using ODI (Outcome-Driven Innovation) methodology.
使用 ODI（结果驱动创新）方法进行机会评分。

**Use when / 适用场景**: Evaluating potential improvements based on importance vs satisfaction gaps.

```bash
python 01_opportunity_scoring.py
```

### 02_four_forces.py
Four Forces of Progress analysis — PUSH, PULL, ANXIETY, HABIT.
进步四力分析 — 推力、拉力、焦虑、惯性。

**Use when / 适用场景**: Understanding why users switch from one solution to another.

```bash
python 02_four_forces.py
```

### 02_opportunity_analysis.py
Opportunity score analysis to identify underserved needs.
机会评分分析以识别未满足的需求。

**Use when / 适用场景**: Prioritizing which customer needs to address first.

```bash
python 02_opportunity_analysis.py
```

### 03_job_stories.py
Job stories generation in multiple formats (Intercom, Kalbach, Hill, Troeth).
多种格式的 Job Stories 生成（Intercom、Kalbach、Hill、Troeth）。

**Use when / 适用场景**: Translating JTBD research insights into solution-agnostic requirements.

```bash
python 03_job_stories.py
```

## Tips / 提示

- All examples use relative imports — just run from the `examples/` directory
- No `pip install` required — JTBD is zero-dependency
- Feed JTBD insights into VPD for canvas development
- See [USAGE.md](../USAGE.md) for detailed API documentation
