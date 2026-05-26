#!/usr/bin/env python3
"""Example: Four Forces of Progress analysis.

Scenario: Understanding why users switch from a legacy CRM to a new platform.
"""
from jtbd import JTBDSkill

jtbd = JTBDSkill("CRM Migration")

print("=" * 60)
print("Four Forces Analysis: CRM Platform Switch")
print("=" * 60)

analysis = jtbd.four_forces_analysis(
    job="Manage customer relationships effectively",
    current_solution="Legacy CRM (on-premise, complex setup)",
    new_solution="Cloud CRM (AI-powered, easy onboarding)"
)
print(analysis)

# Forces breakdown with specific examples
print("\n" + "=" * 60)
print("Key Forces Identified")
print("=" * 60)
print("""
  PUSH (what's wrong with current):
  → Slow search performance frustrates sales reps
  → Mobile app is unusable — reps can't update on the go
  → Monthly maintenance requires IT intervention

  PULL (what's attractive about new):
  → AI-powered lead scoring promises 30% more conversions
  → Mobile-first design — update from anywhere
  → Zero-IT-setup cloud deployment

  ANXIETY (worries about switching):
  → Data migration — will historical records be lost?
  → Learning curve — will the team resist?
  → Integration — will it work with our existing ERP?

  HABIT (anchoring to current):
  → 5 years of workflow customization
  → Team knows the keyboard shortcuts by muscle memory
  → "If it ain't broke, don't fix it" mentality
""")
