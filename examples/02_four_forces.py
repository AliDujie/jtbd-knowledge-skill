#!/usr/bin/env python3
"""Example: Four Forces of Progress analysis.

Scenario: Understanding why users switch from a legacy CRM to a new platform.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jtbd import JTBDSkill

jtbd = JTBDSkill("CRM Migration")

print("=" * 60)
print("Four Forces Analysis: CRM Platform Switch")
print("=" * 60)

# Add forces: PUSH (away from current), PULL (toward new), ANXIETY (worries), HABIT (anchoring)

# Push forces — what's wrong with the current CRM
jtbd.add_force("push", "Slow search performance frustrates sales reps", intensity=4)
jtbd.add_force("push", "Mobile app is unusable — reps can't update on the go", intensity=5)
jtbd.add_force("push", "Monthly maintenance requires IT intervention", intensity=3)

# Pull forces — what's attractive about the new solution
jtbd.add_force("pull", "AI-powered lead scoring promises 30% more conversions", intensity=4)
jtbd.add_force("pull", "Mobile-first design — update from anywhere", intensity=5)
jtbd.add_force("pull", "Zero-IT-setup cloud deployment", intensity=3)

# Anxiety forces — worries about switching
jtbd.add_force("anxiety", "Data migration — will historical records be lost?", intensity=4)
jtbd.add_force("anxiety", "Learning curve — will the team resist?", intensity=3)
jtbd.add_force("anxiety", "Integration — will it work with our existing ERP?", intensity=3)

# Habit/Inertia forces — anchoring to current
jtbd.add_force("inertia", "5 years of workflow customization", intensity=4)
jtbd.add_force("inertia", "Team knows the keyboard shortcuts by muscle memory", intensity=3)
jtbd.add_force("inertia", "\"If it ain't broke, don't fix it\" mentality", intensity=2)

# Generate analysis report
report = jtbd.generate_analysis_report()
print(report)

# Interpretation guide
print("\n" + "=" * 60)
print("Four Forces Interpretation")
print("=" * 60)
print("""
  Switch happens when: PUSH + PULL > ANXIETY + HABIT
  
  To accelerate switching:
  → Amplify PUSH: Make current pain visible (metrics, anecdotes)
  → Amplify PULL: Demonstrate new value clearly (demos, trials)
  → Reduce ANXIETY: Address fears proactively (migration plan, training)
  → Reduce HABIT: Make transition effortless (import tools, familiar UI)
""")
