#!/usr/bin/env python3
"""Example: Job Stories generation.

Scenario: Creating job stories for a healthcare scheduling app.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jtbd import JTBDSkill

jtbd = JTBDSkill("Healthcare Scheduling App")

print("=" * 60)
print("Job Stories: Healthcare Scheduling")
print("=" * 60)

# Create job stories builder
stories = jtbd.create_job_stories("Book patient appointments during shift changes")

# Add job stories in different formats (intercom, kalbach, hill, troeth)
stories.add_story("intercom",
    situation="a patient calls to reschedule during shift change",
    motivation="quickly find and book an open slot",
    outcome="I don't lose track of the appointment during the chaos",
    priority=5
)

stories.add_story("kalbach",
    situation="I'm managing 30+ patients across two wards",
    motivation="see all upcoming appointments at a glance",
    outcome="I can prioritize without missing critical follow-ups",
    priority=4
)

stories.add_story("hill",
    situation="a doctor needs to squeeze in an urgent case",
    motivation="find the earliest available slot within 2 hours",
    outcome="the patient gets care without disrupting the schedule",
    priority=5
)

result = stories.build()
print(result)

# Interpretation guide
print("\n" + "=" * 60)
print("Job Stories vs User Stories")
print("=" * 60)
print("""
  User Story: "As a nurse, I want to reschedule patients so that..."
  -> Assumes a role and solution

  Job Story: "When a patient calls during shift change,
              I want to quickly find an open slot
              so I don't lose the appointment"
  -> Focuses on context + motivation -> outcome
  -> Solution-agnostic
  -> Capturable from JTBD interviews

  Supported formats:
  -> intercom: When [situation], I want to [motivation], so I can [outcome]
  -> kalbach: When [situation], I want to [motivation], so I can [outcome], but [concern]
  -> hill: As a [role], I want to [motivation], so that [outcome]
  -> troeth: As a [role], I want [motivation], and I need [action] to [outcome]
""")
