#!/usr/bin/env python3
"""Example: JTBD Opportunity Scoring using ODI methodology.

Scenario: Evaluating potential improvements for a project management tool.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jtbd import JTBDSkill

jtbd = JTBDSkill("Project Management Tool")

print("=" * 60)
print("Opportunity Scoring: Project Management Jobs")
print("=" * 60)

# Score 3 potential job opportunities using ODI (Importance/Satisfaction)
odi_jobs = [
    ("Quickly assign tasks to team members", 9, 4),   # High importance, low satisfaction
    ("Track project budget vs. actual spend", 7, 6),   # Moderate importance, moderate satisfaction
    ("Generate client-ready status reports", 8, 3),    # High importance, very low satisfaction
]

for job_text, importance, satisfaction in odi_jobs:
    result = jtbd.score_odi(job_text, importance=importance, satisfaction=satisfaction)
    print(f"\nJob: '{job_text}'")
    print(f"  Importance: {importance}, Satisfaction: {satisfaction}")
    print(f"  ODI Score: {result['odi_score']} ({result['odi_level']})")
    print(f"  Suggested Strategy: {result['suggested_strategy']}")

# Also score using the 4-dimension opportunity model
print("\n" + "=" * 60)
print("4-Dimension Opportunity Score")
print("=" * 60)

jobs_4d = [
    ("Quickly assign tasks to team members", 4, 3, 4, 3),
    ("Track project budget vs. actual spend", 3, 3, 4, 2),
    ("Generate client-ready status reports", 4, 2, 5, 3),
]

for job_text, struggle, alternative, market, budget in jobs_4d:
    result = jtbd.score_opportunity(job_text, struggle=struggle, alternative=alternative, market=market, budget=budget)
    print(f"\nJob: '{job_text}'")
    print(f"  Struggle={struggle}, Alt={alternative}, Market={market}, Budget={budget}")
    print(f"  Score: {result['score']} ({result['level']})")
    print(f"  Action: {result['action']}")

# Interpretation guide
print("\n" + "=" * 60)
print("Opportunity Score Interpretation")
print("=" * 60)
print("  ODI Score > 10: HIGH opportunity — invest here first")
print("  ODI Score 7-10: MODERATE — worth exploring")
print("  ODI Score < 7:  LOW — lower priority")
print("  (Formula: Opportunity = Importance + (Importance - Satisfaction))")
