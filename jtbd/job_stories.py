"""JTBD Job Stories 生成模块

支持4种 Job Story 变体格式，基于 Kalbach《The Jobs to Be Done Playbook》。

变体1 - Intercom基本版:
  When [situation], I want to [motivation], so I can [expected outcome].

变体2 - Kalbach结构化版:
  When [situation + emotional trigger],
  Help me [action/desire],
  So I can [desired outcome + emotional reward].

变体3 - Andrea Hill版:
  [Job performer] + [Job] + [Situation] + [Need] + [Outcome]

变体4 - Steph Troeth版:
  In order to [outcome], when [situation], I need [need/solution direction].
"""

from dataclasses import dataclass, field
from typing import Dict, List


STORY_FORMATS = (
    "intercom",
    "kalbach",
    "hill",
    "troeth",
)

FORMAT_LABELS: Dict[str, str] = {
    "intercom": "Intercom 基本版",
    "kalbach": "Kalbach 结构化版",
    "hill": "Andrea Hill 版",
    "troeth": "Steph Troeth 版",
}

FORMAT_TEMPLATES: Dict[str, str] = {
    "intercom": "When {situation}, I want to {motivation}, so I can {outcome}.",
    "kalbach": "When {situation},\nHelp me {motivation},\nSo I can {outcome}.",
    "hill": "{performer} needs to {job} when {situation}, requiring {need}, in order to {outcome}.",
    "troeth": "In order to {outcome}, when {situation}, I need {need}.",
}

FORMAT_DESCRIPTIONS: Dict[str, str] = {
    "intercom": "最简洁的格式，适合快速捕捉需求，聚焦情境-动机-结果三要素",
    "kalbach": "增加情感维度，显式区分情境触发器、行动期望和情感回报",
    "hill": "最完整的格式，明确Job执行者角色，适合B2B和多角色场景",
    "troeth": "以结果为导向的格式，先陈述期望结果再描述情境和需求",
}


@dataclass
class JobStory:
    """一条 Job Story"""
    story_format: str
    situation: str
    motivation: str = ""
    outcome: str = ""
    performer: str = ""
    job: str = ""
    need: str = ""
    emotional_trigger: str = ""
    emotional_reward: str = ""
    job_map_stage: str = ""
    priority: int = 3

    def render(self) -> str:
        if self.story_format == "intercom":
            return (
                f"When {self.situation}, "
                f"I want to {self.motivation}, "
                f"so I can {self.outcome}."
            )
        elif self.story_format == "kalbach":
            sit = self.situation
            if self.emotional_trigger:
                sit = f"{self.situation} ({self.emotional_trigger})"
            out = self.outcome
            if self.emotional_reward:
                out = f"{self.outcome} ({self.emotional_reward})"
            return (
                f"When {sit},\n"
                f"Help me {self.motivation},\n"
                f"So I can {out}."
            )
        elif self.story_format == "hill":
            return (
                f"{self.performer or 'The user'} needs to {self.job or self.motivation} "
                f"when {self.situation}, "
                f"requiring {self.need or self.motivation}, "
                f"in order to {self.outcome}."
            )
        elif self.story_format == "troeth":
            return (
                f"In order to {self.outcome}, "
                f"when {self.situation}, "
                f"I need {self.need or self.motivation}."
            )
        return f"[{self.story_format}] {self.situation} → {self.motivation} → {self.outcome}"

    def render_zh(self) -> str:
        if self.story_format == "intercom":
            return f"当 {self.situation} 时，我想要 {self.motivation}，这样我就能 {self.outcome}。"
        elif self.story_format == "kalbach":
            sit = self.situation
            if self.emotional_trigger:
                sit = f"{self.situation}（{self.emotional_trigger}）"
            out = self.outcome
            if self.emotional_reward:
                out = f"{self.outcome}（{self.emotional_reward}）"
            return f"当 {sit} 时，\n帮我 {self.motivation}，\n这样我就能 {out}。"
        elif self.story_format == "hill":
            return (
                f"{self.performer or '用户'} 在 {self.situation} 时，"
                f"需要 {self.need or self.motivation}，"
                f"以便 {self.outcome}。"
            )
        elif self.story_format == "troeth":
            return f"为了 {self.outcome}，当 {self.situation} 时，我需要 {self.need or self.motivation}。"
        return f"[{self.story_format}] {self.situation} → {self.motivation} → {self.outcome}"


@dataclass
class JobStorySet:
    """一组 Job Stories"""
    title: str
    stories: List[JobStory] = field(default_factory=list)

    def by_format(self, fmt: str) -> List[JobStory]:
        return [s for s in self.stories if s.story_format == fmt]

    def by_stage(self, stage: str) -> List[JobStory]:
        return [s for s in self.stories if s.job_map_stage == stage]

    def by_priority(self, min_priority: int = 3) -> List[JobStory]:
        return [s for s in self.stories if s.priority >= min_priority]


class JobStoryBuilder:
    """Job Story 构建器

    用法示例::

        builder = JobStoryBuilder("商旅住宿预订 Job Stories")

        builder.add_story(
            story_format="intercom",
            situation="I'm booking a hotel for a business trip with limited time",
            motivation="quickly find a hotel that meets company standards",
            outcome="focus on preparing for my meetings instead of worrying about accommodation",
            job_map_stage="locate",
        )

        builder.add_story(
            story_format="kalbach",
            situation="I arrive at a hotel after a long flight",
            motivation="check in quickly without hassle",
            outcome="get to my room and rest",
            emotional_trigger="exhausted and stressed",
            emotional_reward="feeling relieved and in control",
            job_map_stage="execute",
        )

        story_set = builder.build()
        print(JobStoryBuilder.render_markdown(story_set))
    """

    def __init__(self, title: str):
        self._title = title
        self._stories: List[JobStory] = []

    def add_story(self, story_format: str, situation: str,
                  motivation: str = "", outcome: str = "",
                  performer: str = "", job: str = "",
                  need: str = "",
                  emotional_trigger: str = "",
                  emotional_reward: str = "",
                  job_map_stage: str = "",
                  priority: int = 3) -> "JobStoryBuilder":
        if story_format not in STORY_FORMATS:
            raise ValueError(f"未知格式: {story_format}，可选: {STORY_FORMATS}")
        story = JobStory(
            story_format=story_format, situation=situation,
            motivation=motivation, outcome=outcome,
            performer=performer, job=job, need=need,
            emotional_trigger=emotional_trigger,
            emotional_reward=emotional_reward,
            job_map_stage=job_map_stage, priority=priority,
        )
        self._stories.append(story)
        return self

    def add_story_zh(self, story_format: str, situation: str,
                     motivation: str = "", outcome: str = "",
                     performer: str = "", job: str = "",
                     need: str = "",
                     emotional_trigger: str = "",
                     emotional_reward: str = "",
                     job_map_stage: str = "",
                     priority: int = 3) -> "JobStoryBuilder":
        return self.add_story(
            story_format=story_format, situation=situation,
            motivation=motivation, outcome=outcome,
            performer=performer, job=job, need=need,
            emotional_trigger=emotional_trigger,
            emotional_reward=emotional_reward,
            job_map_stage=job_map_stage, priority=priority,
        )

    def build(self) -> JobStorySet:
        return JobStorySet(title=self._title, stories=list(self._stories))

    @staticmethod
    def render_markdown(story_set: JobStorySet) -> str:
        lines = [f"# {story_set.title}\n"]

        format_groups: Dict[str, List[JobStory]] = {}
        for s in story_set.stories:
            format_groups.setdefault(s.story_format, []).append(s)

        for fmt in STORY_FORMATS:
            stories = format_groups.get(fmt, [])
            if not stories:
                continue
            lines.append(f"## {FORMAT_LABELS[fmt]}\n")
            lines.append(f"*{FORMAT_DESCRIPTIONS[fmt]}*\n")

            for i, story in enumerate(stories, 1):
                priority_marker = " ⭐" if story.priority >= 4 else ""
                stage_tag = f" `[{story.job_map_stage}]`" if story.job_map_stage else ""
                lines.append(f"### Story {i}{priority_marker}{stage_tag}\n")
                lines.append(f"**English:**\n{story.render()}\n")
                lines.append(f"**中文:**\n{story.render_zh()}\n")

        if not format_groups:
            lines.append("*尚未添加任何 Job Story*\n")
            lines.append("**可用格式:**\n")
            for fmt in STORY_FORMATS:
                lines.append(f"- **{FORMAT_LABELS[fmt]}**: {FORMAT_DESCRIPTIONS[fmt]}")

        high_priority = story_set.by_priority(4)
        if high_priority:
            lines.append(f"\n## 高优先级 Stories ({len(high_priority)}条)\n")
            for s in high_priority:
                lines.append(f"- [{FORMAT_LABELS[s.story_format]}] {s.render_zh()}")

        return "\n".join(lines)

    @staticmethod
    def render_json(story_set: JobStorySet) -> Dict:
        return {
            "title": story_set.title,
            "total": len(story_set.stories),
            "stories": [
                {
                    "format": s.story_format,
                    "format_label": FORMAT_LABELS.get(s.story_format, s.story_format),
                    "rendered": s.render(),
                    "rendered_zh": s.render_zh(),
                    "situation": s.situation,
                    "motivation": s.motivation,
                    "outcome": s.outcome,
                    "performer": s.performer,
                    "emotional_trigger": s.emotional_trigger,
                    "emotional_reward": s.emotional_reward,
                    "job_map_stage": s.job_map_stage,
                    "priority": s.priority,
                }
                for s in story_set.stories
            ],
        }
