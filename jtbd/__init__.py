"""JTBD (Jobs to Be Done) Python Toolkit

基于 Alan Klement《When Coffee and Kale Compete》的 JTBD 理论工具包。
覆盖 SKILL.md 全部 8 大执行能力。

快速开始::

    from jtbd import JTBDSkill
    skill = JTBDSkill("飞猪旅行")
    # 8大能力一站式调用
    guide = skill.generate_interview("用户访谈", ["competition", "push"])
    survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])
    score = skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)
    report = skill.generate_analysis_report()
"""

__version__ = "2.0.0"

from .config import AnalysisConfig, FORCE_TYPES, FORCE_LABELS, KNOWLEDGE_FILES
from .utils import load_knowledge, load_all_knowledge, search_knowledge
from .templates import (
    INTERVIEW_QUESTIONS, JTBD_STATEMENT_TEMPLATE,
    JTBD_STATEMENT_EXAMPLES, INNOVATION_CHECKLIST, REPORT_TEMPLATE,
)
from .jtbd_analyzer import JTBDAnalyzer, JTBDAnalysis, JTBDStatement
from .interview_generator import InterviewBuilder, InterviewGuide
from .forces import ForcesProfile, ForceItem, render_forces_markdown
from .innovation import InnovationFinder, InnovationSignal, InnovationOpportunity
from .survey_generator import SurveyBuilder, Survey
from .priority_calculator import PriorityAnalyzer, JobScore, PriorityMatrix
from .competition import CompetitionAnalyzer, CompetitiveAnalysis, Competitor
from .marketing import MarketingCopywriter, CopyPlan, CopyBrief
from .growth import GrowthStrategyBuilder, GrowthPlan

from typing import Dict, List, Optional


class JTBDSkill:
    """JTBD 统一入口类 — 封装全部 8 大执行能力

    用法::

        skill = JTBDSkill("飞猪旅行")

        # 能力1: 访谈提纲
        guide = skill.generate_interview("用户访谈", ["competition", "push", "anxiety"])

        # 能力2: 调查问卷
        survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])

        # 能力3: 机会分数
        score = skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)

        # 能力4: 优先级矩阵
        skill.add_job_to_matrix("快速找住处", struggle=4, alternative=3, market=4, budget=4)
        skill.add_job_to_matrix("比价省钱", struggle=3, alternative=4, market=3, budget=3)
        matrix = skill.render_priority_matrix()

        # 能力5: 竞争分析
        skill.add_competitor("携程", "direct", strengths=["酒店多"], weaknesses=["界面复杂"])
        competition = skill.render_competition()

        # 能力6: 营销文案
        copy = skill.generate_marketing_copy(struggle="花30分钟比价", desired_outcome="专注工作")

        # 能力7: 增长策略
        growth = skill.generate_growth_strategy(churn_segments=[("no_progress", "首周未预订", 200)])

        # 能力8: JTBD描述
        stmt = skill.create_jtbd_statement("Help me", "快速找住处", "专注工作")
    """

    def __init__(self, product_name: str, config: Optional[AnalysisConfig] = None):
        self.product = product_name
        self.config = config or AnalysisConfig()
        self.analyzer = JTBDAnalyzer(product_name, self.config)
        self.priority_analyzer = PriorityAnalyzer()
        self.competition_analyzer = CompetitionAnalyzer(product_name)
        self.innovation_finder = InnovationFinder()

    def generate_interview(self, title: str,
                           dimensions: Optional[List[str]] = None,
                           context: str = "") -> str:
        builder = InterviewBuilder(title, self.config)
        if context:
            builder.set_context(context)
        if dimensions:
            builder.include_dimensions(dimensions)
        guide = builder.build()
        return InterviewBuilder.render_markdown(guide)

    def generate_survey(self, title: str, survey_type: str,
                        struggles: Optional[List[str]] = None,
                        alternatives: Optional[List[str]] = None,
                        hypotheses: Optional[List[str]] = None) -> str:
        builder = SurveyBuilder(title, survey_type)
        builder.set_product(self.product)
        if struggles:
            builder.set_struggles(struggles)
        if alternatives:
            builder.set_alternatives(alternatives)
        if hypotheses:
            builder.set_hypotheses(hypotheses)
        survey = builder.build()
        return SurveyBuilder.render_markdown(survey)

    def score_opportunity(self, job_desc: str, struggle: int = 3,
                          alternative: int = 3, market: int = 3,
                          budget: int = 3) -> Dict:
        job = self.priority_analyzer.add_job(job_desc)
        self.priority_analyzer.score_job(job, "struggle", struggle)
        self.priority_analyzer.score_job(job, "alternative", alternative)
        self.priority_analyzer.score_job(job, "market", market)
        self.priority_analyzer.score_job(job, "budget", budget)
        return {"score": job.opportunity_score, "level": job.level, "action": job.action}

    def add_job_to_matrix(self, job_desc: str, struggle: int = 3,
                          alternative: int = 3, market: int = 3, budget: int = 3,
                          push: int = 0, pull: int = 0,
                          anxiety: int = 0, inertia: int = 0) -> JobScore:
        job = self.priority_analyzer.add_job(job_desc)
        self.priority_analyzer.score_job(job, "struggle", struggle)
        self.priority_analyzer.score_job(job, "alternative", alternative)
        self.priority_analyzer.score_job(job, "market", market)
        self.priority_analyzer.score_job(job, "budget", budget)
        if any([push, pull, anxiety, inertia]):
            self.priority_analyzer.score_forces(job, push, pull, anxiety, inertia)
        return job

    def render_priority_matrix(self) -> str:
        return self.priority_analyzer.render_markdown()

    def add_competitor(self, name: str, category: str = "direct",
                       strengths: Optional[List[str]] = None,
                       weaknesses: Optional[List[str]] = None) -> None:
        self.competition_analyzer.add_competitor(
            name, category, strengths=strengths or [], weaknesses=weaknesses or [])

    def render_competition(self) -> str:
        self.competition_analyzer.auto_insights()
        return self.competition_analyzer.render_markdown()

    def generate_marketing_copy(self, struggle: str, desired_outcome: str,
                                purpose: str = "landing_page",
                                anxieties: Optional[List[str]] = None,
                                inertias: Optional[List[str]] = None) -> str:
        writer = MarketingCopywriter()
        writer.set_brief(self.product, f"{self.product}的核心Job",
                         struggle, desired_outcome, purpose)
        for a in (anxieties or []):
            writer.add_anxiety(a)
        for i in (inertias or []):
            writer.add_inertia(i)
        plan = writer.generate()
        return MarketingCopywriter.render_markdown(plan)

    def generate_growth_strategy(self, target_job: str = "",
                                 growth_opps: Optional[List[tuple]] = None,
                                 churn_segments: Optional[List[tuple]] = None,
                                 key_habits: Optional[List[tuple]] = None) -> str:
        builder = GrowthStrategyBuilder(self.product)
        if target_job:
            builder.set_target_job(target_job)
        for opp in (growth_opps or []):
            builder.add_growth_opportunity(*opp)
        for seg in (churn_segments or []):
            builder.add_churn_segment(*seg)
        for hab in (key_habits or []):
            builder.add_key_habit(*hab)
        plan = builder.build()
        return GrowthStrategyBuilder.render_markdown(plan)

    def create_jtbd_statement(self, verb: str, struggle: str,
                              desired_outcome: str) -> str:
        stmt = self.analyzer.add_statement(verb, struggle, desired_outcome)
        return stmt.render()

    def add_force(self, force_type: str, description: str,
                  intensity: int = 3, evidence: str = "") -> None:
        self.analyzer.add_force(force_type, description, intensity, evidence)

    def generate_analysis_report(self) -> str:
        return self.analyzer.generate_report()

    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)


__all__ = [
    "JTBDSkill",
    "AnalysisConfig", "FORCE_TYPES", "FORCE_LABELS", "KNOWLEDGE_FILES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "INTERVIEW_QUESTIONS", "JTBD_STATEMENT_TEMPLATE",
    "JTBD_STATEMENT_EXAMPLES", "INNOVATION_CHECKLIST", "REPORT_TEMPLATE",
    "JTBDAnalyzer", "JTBDAnalysis", "JTBDStatement",
    "InterviewBuilder", "InterviewGuide",
    "ForcesProfile", "ForceItem", "render_forces_markdown",
    "InnovationFinder", "InnovationSignal", "InnovationOpportunity",
    "SurveyBuilder", "Survey",
    "PriorityAnalyzer", "JobScore", "PriorityMatrix",
    "CompetitionAnalyzer", "CompetitiveAnalysis", "Competitor",
    "MarketingCopywriter", "CopyPlan", "CopyBrief",
    "GrowthStrategyBuilder", "GrowthPlan",
]
