#!/usr/bin/env python3
"""JTBD Example 02: ODI Opportunity Scoring / ODI 机会评分

Scores desired outcomes using the ODI Opportunity Algorithm.
使用 ODI 机会评分算法评估期望结果。

Run: python 02_opportunity_analysis.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jtbd import JTBDSkill

print("=" * 60)
print("JTBD Example 02: ODI Opportunity Scoring")
print("示例 02：ODI 机会评分")
print("=" * 60)

skill = JTBDSkill("智能推荐系统")

outcomes = [
    ("快速找到感兴趣的内容", 8, 4),  # 高重要性 + 低满意度 = 高机会
    ("减少信息过载", 7, 5),
    ("个性化推荐准确", 9, 3),  # 最高机会
    ("跨设备同步使用体验", 6, 6),
    ("保护隐私数据", 8, 7),
]

print("\n📊 ODI Opportunity Score Analysis / ODI 机会评分分析")
print("-" * 50)
print(f"{'Outcome / 结果':<20} {'Imp':>4} {'Sat':>4} {'Opp':>4} {'Priority / 优先级':<15}")
print("-" * 50)

for desc, imp, sat in outcomes:
    result = skill.score_odi(desc, imp, sat)
    opp = result.get('odi_score', 0)
    level = result.get('odi_level', '')
    print(f"{desc:<20} {imp:>4} {sat:>4} {float(opp):>4.1f} {level}")

print("-" * 50)
print("\n✅ Tip: Opportunity = Importance + (Importance - Satisfaction)")
print("✅ 公式：机会 = 重要性 + (重要性 - 满意度)")
print("   Prioritize outcomes with Opp > 10.")
print("   优先处理机会分 > 10 的结果。")
