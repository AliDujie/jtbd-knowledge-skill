"""JTBD 调查问卷生成模块

对应 SKILL.md 执行能力二：设计 JTBD 调查问卷。
支持五种问卷类型:
1. 筛选型 (screening) — 快速识别挣扎人群
2. 验证型 (validation) — 验证已发现的JTBD假设
3. 竞争型 (competition) — 了解替代方案和切换原因
4. ODI Outcome型 (odi_outcome) — 配对测量Importance×Satisfaction（Ulwick ODI标准）
5. Jobs Scoring型 (jobs_scoring) — 重要性×频率×挫折感三维评分
"""

from dataclasses import dataclass, field
from typing import Dict, List


SURVEY_TYPES = ("screening", "validation", "competition", "odi_outcome", "jobs_scoring")

SURVEY_TYPE_LABELS: Dict[str, str] = {
    "screening": "筛选型问卷",
    "validation": "验证型问卷",
    "competition": "竞争型问卷",
    "odi_outcome": "ODI Outcome问卷",
    "jobs_scoring": "Jobs Scoring问卷",
}

SURVEY_TYPE_DESCRIPTIONS: Dict[str, str] = {
    "screening": "快速识别哪些人群挣扎最强烈（适合创新探索前期）",
    "validation": "验证已发现的JTBD假设（适合定性研究后的量化验证）",
    "competition": "了解用户使用的替代方案和切换原因",
    "odi_outcome": "基于Ulwick ODI方法论，对每个Desired Outcome配对测量重要性(1-10)和满意度(1-10)，计算Opportunity分数",
    "jobs_scoring": "对每个Job从重要性、频率、挫折感三维度评分，识别高价值创新机会",
}

QUESTION_FORMATS = ("single_choice", "multiple_choice", "scale", "ranking", "open_ended", "paired_scale")

FORMAT_LABELS: Dict[str, str] = {
    "single_choice": "单选",
    "multiple_choice": "多选",
    "scale": "量表1-5",
    "ranking": "排序",
    "open_ended": "开放题",
    "paired_scale": "配对量表1-10",
}

ODI_SAMPLE_SIZE_GUIDANCE = {
    "minimum": 150,
    "recommended": 300,
    "ideal": 600,
    "note": "ODI问卷建议样本量≥150以确保统计显著性，理想样本量为300-600",
}


@dataclass
class SurveyQuestion:
    """单个问卷题目"""
    question_format: str
    text: str
    options: List[str] = field(default_factory=list)
    scale_labels: Dict[int, str] = field(default_factory=dict)
    required: bool = True
    skip_logic: str = ""
    paired_with: str = ""


@dataclass
class Survey:
    """完整问卷"""
    title: str
    survey_type: str
    description: str = ""
    target_audience: str = ""
    estimated_time: str = ""
    sample_size_note: str = ""
    questions: List[SurveyQuestion] = field(default_factory=list)
    closing_text: str = "感谢您的参与！您的反馈将帮助我们更好地改进产品。"


class SurveyBuilder:
    """问卷构建器

    用法示例::

        # 传统筛选型
        builder = SurveyBuilder("旅行预订体验调研", "screening")
        builder.set_target("过去3个月使用过在线旅行预订的用户")
        builder.set_product("旅行预订平台")
        builder.set_struggles(["找酒店耗时", "价格不透明", "评价不可信"])
        survey = builder.build()

        # ODI Outcome型
        builder = SurveyBuilder("商旅住宿Outcome调研", "odi_outcome")
        builder.set_target("过去6个月有商务出差经历的用户")
        builder.set_outcomes([
            "快速找到符合公司标准的酒店",
            "确认酒店照片与实际一致",
            "获得最优价格",
        ])
        survey = builder.build()
        print(builder.render_markdown(survey))
    """

    def __init__(self, title: str, survey_type: str):
        if survey_type not in SURVEY_TYPES:
            raise ValueError(f"未知问卷类型: {survey_type}，可选: {SURVEY_TYPES}")
        self.title = title
        self.survey_type = survey_type
        self._target = ""
        self._product = ""
        self._struggles: List[str] = []
        self._hypotheses: List[str] = []
        self._alternatives: List[str] = []
        self._outcomes: List[str] = []
        self._jobs: List[str] = []
        self._custom_questions: List[SurveyQuestion] = []

    def set_target(self, target: str) -> "SurveyBuilder":
        self._target = target
        return self

    def set_product(self, product: str) -> "SurveyBuilder":
        self._product = product
        return self

    def set_struggles(self, struggles: List[str]) -> "SurveyBuilder":
        self._struggles = struggles
        return self

    def set_hypotheses(self, hypotheses: List[str]) -> "SurveyBuilder":
        self._hypotheses = hypotheses
        return self

    def set_alternatives(self, alternatives: List[str]) -> "SurveyBuilder":
        self._alternatives = alternatives
        return self

    def set_outcomes(self, outcomes: List[str]) -> "SurveyBuilder":
        self._outcomes = outcomes
        return self

    def set_jobs(self, jobs: List[str]) -> "SurveyBuilder":
        self._jobs = jobs
        return self

    def add_question(self, question: SurveyQuestion) -> "SurveyBuilder":
        self._custom_questions.append(question)
        return self

    def _build_screening(self) -> List[SurveyQuestion]:
        product = self._product or "该产品"
        questions: List[SurveyQuestion] = []

        struggle_options = list(self._struggles) + ["其他（请填写）"]
        questions.append(SurveyQuestion(
            question_format="single_choice",
            text=f"你目前在使用{product}相关服务时面临的最大挑战是什么？",
            options=struggle_options,
        ))

        questions.append(SurveyQuestion(
            question_format="scale",
            text="这个挑战对你的影响有多大？",
            scale_labels={1: "几乎没影响", 3: "有一定影响", 5: "严重影响日常工作/生活"},
        ))

        questions.append(SurveyQuestion(
            question_format="single_choice",
            text="你是否尝试过解决这个问题？",
            options=[
                "是，投入了大量时间和精力",
                "是，但只是偶尔尝试",
                "没有，因为不知道怎么解决",
                "没有，因为觉得不值得解决",
            ],
        ))

        if self._alternatives:
            questions.append(SurveyQuestion(
                question_format="multiple_choice",
                text="你用过哪些方式来解决？",
                options=self._alternatives + ["其他（请填写）"],
            ))

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text=f"你注册/购买{product}时，生活中正在发生什么？",
            required=False,
        ))

        return questions

    def _build_validation(self) -> List[SurveyQuestion]:
        product = self._product or "该产品"
        questions: List[SurveyQuestion] = []

        if self._hypotheses:
            questions.append(SurveyQuestion(
                question_format="single_choice",
                text=f"以下哪个描述最符合你使用{product}的原因？",
                options=self._hypotheses,
            ))

        if self._struggles:
            questions.append(SurveyQuestion(
                question_format="ranking",
                text="请按重要性排列以下因素：",
                options=self._struggles,
            ))

            questions.append(SurveyQuestion(
                question_format="scale",
                text=f"在使用{product}之前，以下问题对你的困扰程度：",
                scale_labels={1: "完全不困扰", 3: "有些困扰", 5: "非常困扰"},
            ))

        questions.append(SurveyQuestion(
            question_format="scale",
            text=f"在决定使用{product}时，以下因素的吸引程度：",
            scale_labels={1: "完全不吸引", 3: "有些吸引", 5: "非常吸引"},
        ))

        questions.append(SurveyQuestion(
            question_format="scale",
            text=f"在使用{product}时，以下因素让你担忧的程度：",
            scale_labels={1: "完全不担忧", 3: "有些担忧", 5: "非常担忧"},
        ))

        return questions

    def _build_competition(self) -> List[SurveyQuestion]:
        product = self._product or "该产品"
        questions: List[SurveyQuestion] = []

        if self._alternatives:
            questions.append(SurveyQuestion(
                question_format="multiple_choice",
                text=f"在使用{product}之前，你用过以下哪些替代方案？",
                options=self._alternatives + ["自己手动处理", "什么都没用", "其他（请填写）"],
            ))

        questions.append(SurveyQuestion(
            question_format="single_choice",
            text=f"你是从哪个方案切换到{product}的？",
            options=(self._alternatives or ["其他产品"]) + ["这是我第一次使用此类产品"],
        ))

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text="你为什么决定切换？之前的方案有什么让你不满意的？",
        ))

        questions.append(SurveyQuestion(
            question_format="scale",
            text=f"与之前的方案相比，{product}在以下方面的表现如何？",
            scale_labels={1: "差很多", 3: "差不多", 5: "好很多"},
        ))

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text=f"如果{product}明天消失了，你会用什么来替代？",
            required=False,
        ))

        return questions

    def _build_odi_outcome(self) -> List[SurveyQuestion]:
        questions: List[SurveyQuestion] = []

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text="请简要描述你在完成此类任务时的典型场景和主要挑战。",
            required=False,
        ))

        for idx, outcome in enumerate(self._outcomes, 1):
            imp_key = f"outcome_{idx}_importance"
            sat_key = f"outcome_{idx}_satisfaction"

            questions.append(SurveyQuestion(
                question_format="paired_scale",
                text=f"关于「{outcome}」— 这件事对你有多重要？",
                scale_labels={1: "完全不重要", 5: "中等重要", 10: "极其重要"},
                paired_with=sat_key,
            ))

            questions.append(SurveyQuestion(
                question_format="paired_scale",
                text=f"关于「{outcome}」— 你对目前方案在这方面的表现有多满意？",
                scale_labels={1: "完全不满意", 5: "中等满意", 10: "非常满意"},
                paired_with=imp_key,
            ))

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text="在上述需求中，哪一项如果能得到显著改善，会对你的工作/生活产生最大影响？为什么？",
            required=False,
        ))

        return questions

    def _build_jobs_scoring(self) -> List[SurveyQuestion]:
        questions: List[SurveyQuestion] = []

        questions.append(SurveyQuestion(
            question_format="open_ended",
            text="请简要描述你在这个领域的典型使用场景。",
            required=False,
        ))

        for job in (self._jobs or self._struggles):
            questions.append(SurveyQuestion(
                question_format="scale",
                text=f"「{job}」— 这件事对你有多重要？",
                scale_labels={1: "完全不重要", 3: "中等", 5: "极其重要"},
            ))

            questions.append(SurveyQuestion(
                question_format="scale",
                text=f"「{job}」— 你多久需要做一次？",
                scale_labels={1: "极少（每年几次）", 3: "经常（每周）", 5: "非常频繁（每天）"},
            ))

            questions.append(SurveyQuestion(
                question_format="scale",
                text=f"「{job}」— 目前完成这件事的挫折感有多强？",
                scale_labels={1: "几乎没有挫折感", 3: "有一定挫折感", 5: "极度沮丧"},
            ))

        questions.append(SurveyQuestion(
            question_format="ranking",
            text="请将以下任务按照「最想得到改善」的程度排序：",
            options=list(self._jobs or self._struggles),
        ))

        return questions

    def build(self) -> Survey:
        builders = {
            "screening": self._build_screening,
            "validation": self._build_validation,
            "competition": self._build_competition,
            "odi_outcome": self._build_odi_outcome,
            "jobs_scoring": self._build_jobs_scoring,
        }
        questions = builders[self.survey_type]()
        questions.extend(self._custom_questions)

        q_count = len(questions)
        estimated = f"{max(3, q_count * 1)}~{q_count * 2}分钟"

        sample_note = ""
        if self.survey_type == "odi_outcome":
            sample_note = ODI_SAMPLE_SIZE_GUIDANCE["note"]

        return Survey(
            title=self.title,
            survey_type=self.survey_type,
            description=SURVEY_TYPE_DESCRIPTIONS[self.survey_type],
            target_audience=self._target,
            estimated_time=estimated,
            sample_size_note=sample_note,
            questions=questions,
        )

    @staticmethod
    def render_markdown(survey: Survey) -> str:
        lines = [f"# {survey.title}\n"]
        lines.append(f"**问卷类型:** {SURVEY_TYPE_LABELS[survey.survey_type]} — {survey.description}")
        if survey.target_audience:
            lines.append(f"**目标人群:** {survey.target_audience}")
        lines.append(f"**预计填写时长:** {survey.estimated_time}")
        if survey.sample_size_note:
            lines.append(f"**样本量建议:** {survey.sample_size_note}")
        lines.append("\n---\n")

        for i, q in enumerate(survey.questions, 1):
            fmt = FORMAT_LABELS.get(q.question_format, q.question_format)
            lines.append(f"**Q{i}. [{fmt}]** {q.text}")

            if q.options:
                for opt in q.options:
                    if q.question_format == "multiple_choice":
                        lines.append(f"   - [ ] {opt}")
                    else:
                        lines.append(f"   - {opt}")

            if q.scale_labels:
                parts = [f"{k}={v}" for k, v in sorted(q.scale_labels.items())]
                lines.append(f"   ({' / '.join(parts)})")

            if q.skip_logic:
                lines.append(f"   *跳转逻辑: {q.skip_logic}*")

            if not q.required:
                lines.append("   *（选填）*")
            lines.append("")

        if survey.survey_type == "odi_outcome":
            lines.append("---\n")
            lines.append("## ODI分析说明\n")
            lines.append("收集数据后，按以下公式计算每条Outcome的机会分数：")
            lines.append("```")
            lines.append("Opportunity = Importance + max(Importance - Satisfaction, 0)")
            lines.append("```")
            lines.append("- 机会分 ≥ 12: 未被充分满足 (Underserved) — 优先创新方向")
            lines.append("- 机会分 8-12: 基本满足 (Appropriately Served)")
            lines.append("- 机会分 < 8: 过度满足 (Overserved) — 可简化以降低成本")
            lines.append("")

        lines.append("---")
        lines.append(f"\n{survey.closing_text}")
        return "\n".join(lines)

    @staticmethod
    def render_json(survey: Survey) -> Dict:
        return {
            "title": survey.title,
            "type": survey.survey_type,
            "description": survey.description,
            "target_audience": survey.target_audience,
            "estimated_time": survey.estimated_time,
            "sample_size_note": survey.sample_size_note,
            "questions": [
                {
                    "format": q.question_format,
                    "text": q.text,
                    "options": q.options,
                    "scale_labels": q.scale_labels,
                    "required": q.required,
                    "skip_logic": q.skip_logic,
                    "paired_with": q.paired_with,
                }
                for q in survey.questions
            ],
        }
