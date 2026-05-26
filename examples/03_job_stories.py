#!/usr/bin/env python3
"""Example: Job Stories generation.

Scenario: Creating job stories for a healthcare scheduling app.
"""
from jtbd import JTBDSkill

jtbd = JTBDSkill("Healthcare Scheduling App")

print("=" * 60)
print("Job Stories: Healthcare Scheduling")
print("=" * 60)

stories = jtbd.generate_job_stories(
    domain="Healthcare",
    user_type="Medical Staff",
    context="Busy hospital ward with shift changes and emergencies"
)
print(stories)

# Single job story
print("\n" + "=" * 60)
print("Single Job Story: Patient Scheduling")
print("=" * 60)

story = jtbd.create_job_story(
    when="a patient calls to reschedule during shift change",
    i_want="to quickly find and book an open slot without calling back",
    so_that="I don't lose track of the appointment during the chaos"
)
print(story)
