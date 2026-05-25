#!/usr/bin/env python3
"""JTBD Example 01: Switch Interview Guide / 切换访谈提纲

Generates a JTBD switch interview guide covering all Forces of Progress.
生成覆盖全部"进步力量"的 JTBD 切换访谈提纲。

Run: python 01_interview_guide.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jtbd import JTBDSkill

print("=" * 60)
print("JTBD Example 01: Switch Interview Guide")
print("示例 01：切换访谈提纲")
print("=" * 60)

# Scenario: Understanding why users switch to a meal delivery app
skill = JTBDSkill("Meal Delivery App")

print("\n🎯 Product: Meal Delivery App")
print("🎯 产品：外卖订餐应用")
print("-" * 50)

# Generate the Switch interview guide
guide = skill.generate_interview('switch')
print(guide[:600])
print("...\n")

print("✅ Tip: Use this guide to uncover the 'Forces of Progress'")
print("✅ 提示：使用此提纲揭示推动用户改变的'进步力量'")
print("   (Push, Pull, Anxiety, Habit)")
print("   （推力、拉力、焦虑、惯性）")
