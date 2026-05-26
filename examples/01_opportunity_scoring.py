#!/usr/bin/env python3
"""Example: JTBD Opportunity Scoring using ODI methodology.

Scenario: Evaluating potential improvements for a project management tool.
"""
from jtbd import JTBDSkill

jtbd = JTBDSkill("Project Management Tool")

print("=" * 60)
print("Opportunity Scoring: Project Management Jobs")
print("=" * 60)

# Score 3 potential job opportunities
jobs_to_evaluate = [
    ("Quickly assign tasks to team members", 9, 4),   # High importance, low satisfaction
    ("Track project budget vs. actual spend", 7, 6),   # Moderate importance, moderate satisfaction
    ("Generate client-ready status reports", 8, 3),    # High importance, very low satisfaction
]

for job_text, importance, satisfaction in jobs_to_evaluate:
    result = jtbd.score_opportunity(job_text, importance=importance, satisfaction=satisfaction)
    print(f"\nJob: '{job_text}'")
    print(f"  Importance: {importance}, Satisfaction: {satisfaction}")
    print(f"  Result: {result}")

# Interpretation guide
print("\n" + "=" * 60)
print("Opportunity Score Interpretation")
print("=" * 60)
print("  Score > 10: HIGH opportunity — invest here first")
print("  Score 7-10: MODERATE — worth exploring")
print("  Score < 7:  LOW — lower priority")
print("  (Formula: Opportunity = Importance + (Importance - Satisfaction))")
