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
    SCENARIO_MERGE_RULES, EXAMPLE_SELECTION_CRITERIA,
    INSIGHT_QUALITY_RULES, SECTION_INSIGHT_PROMPTS, HTML_REPORT_STYLE_RULES,
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

    def generate_market_size_estimate(self, jobs: Optional[List[Dict]] = None) -> str:
        """市场规模估算（TAM/SAM/SOM + 验证计划）"""
        if not jobs:
            jobs = []
        
        tam_estimate = self._estimate_tam(jobs)
        sam_estimate = self._estimate_sam(jobs)
        som_estimate = self._estimate_som(jobs)
        validation_plan = self._generate_validation_plan()
        
        report = f"""## 市场规模估算

### 总可寻址市场（TAM）
{tam_estimate}

### 可服务市场（SAM）
{sam_estimate}

### 可获得市场（SOM）
{som_estimate}

### 验证计划
{validation_plan}
"""
        return report

    def generate_priority_scoring(self, jobs: Optional[List[Dict]] = None) -> str:
        """优先级评分（机会分计算 + 资源分配建议 + 验证时间线）"""
        if not jobs:
            jobs = []
        
        opportunity_scores = self._calculate_opportunity_scores(jobs)
        resource_allocation = self._generate_resource_allocation(jobs)
        validation_timeline = self._generate_validation_timeline(jobs)
        
        report = f"""## 优先级评分

### 机会分数
{opportunity_scores}

### 资源分配建议
{resource_allocation}

### 验证时间线
{validation_timeline}
"""
        return report

    def generate_commercialization_feasibility(self, jobs: Optional[List[Dict]] = None) -> str:
        """商业化可行性（付费意愿 + 投入产出 + Go/No-Go 决策）"""
        if not jobs:
            jobs = []
        
        willingness_to_pay = self._assess_willingness_to_pay(jobs)
        roi_analysis = self._analyze_roi(jobs)
        go_no_go_decision = self._make_go_no_go_decision(jobs)
        
        report = f"""## 商业化可行性

### 付费意愿评估
{willingness_to_pay}

### 投入产出分析
{roi_analysis}

### Go/No-Go 决策
{go_no_go_decision}
"""
        return report

    def analyze(self, include_ceo_analysis: bool = False) -> str:
        """综合分析报告（可选包含 CEO 决策模块）"""
        report = self.generate_analysis_report()
        
        if include_ceo_analysis:
            report += "\n\n---\n\n"
            report += "# CEO 决策视角\n\n"
            report += self.generate_market_size_estimate()
            report += "\n\n"
            report += self.generate_priority_scoring()
            report += "\n\n"
            report += self.generate_commercialization_feasibility()
        
        return report

    def _generate_p0_analysis(self, job: Dict) -> str:
        """P0 级 Job 深度分析"""
        return f"""### P0 级 Job 深度分析: {job.get('description', '未知')}

**核心痛点**: {job.get('struggle', '未定义')}
**期望结果**: {job.get('desired_outcome', '未定义')}
**机会分数**: {job.get('opportunity_score', 0)}/100

**市场特征**:
- 用户规模: {job.get('market_size', '未知')}
- 付费意愿: {job.get('willingness_to_pay', '未知')}
- 竞争强度: {job.get('competition_level', '未知')}

**建议行动**:
{self._generate_recommendations(job)}
"""

    def _generate_recommendations(self, job: Dict) -> str:
        """各优先级建议生成"""
        score = job.get('opportunity_score', 0)
        
        if score >= 80:
            return """- 立即启动开发，分配核心团队
- 优先级: P0
- 预计投入: 高
- 预期回报: 极高"""
        elif score >= 60:
            return """- 列入下季度规划
- 优先级: P1
- 预计投入: 中
- 预期回报: 高"""
        elif score >= 40:
            return """- 保持观察，收集更多数据
- 优先级: P2
- 预计投入: 低
- 预期回报: 中"""
        else:
            return """- 暂不投入，定期评估
- 优先级: P3
- 预计投入: 无
- 预期回报: 低"""

    def _estimate_tam(self, jobs: List[Dict]) -> str:
        """估算总可寻址市场"""
        return f"基于 {len(jobs)} 个 Job 的分析，TAM 估算为：¥{len(jobs) * 1000000:,}（假设每个 Job 对应 100 万潜在用户）"

    def _estimate_sam(self, jobs: List[Dict]) -> str:
        """估算可服务市场"""
        return f"基于产品定位，SAM 估算为 TAM 的 40%：¥{len(jobs) * 1000000 * 0.4:,.0f}"

    def _estimate_som(self, jobs: List[Dict]) -> str:
        """估算可获得市场"""
        return f"基于当前资源，SOM 估算为 SAM 的 20%：¥{len(jobs) * 1000000 * 0.4 * 0.2:,.0f}"

    def _generate_validation_plan(self) -> str:
        """生成验证计划"""
        return """1. 用户访谈验证（2周）
2. 问卷调研（1周）
3. MVP 原型测试（3周）
4. A/B 测试（2周）
总计: 8周"""

    def _calculate_opportunity_scores(self, jobs: List[Dict]) -> str:
        """计算机会分数"""
        if not jobs:
            return "暂无 Job 数据"
        
        scores = []
        for job in jobs:
            struggle = job.get('struggle', 3)
            alternative = job.get('alternative', 3)
            market = job.get('market', 3)
            budget = job.get('budget', 3)
            score = (struggle + alternative + market + budget) * 100 / 16
            scores.append(score)
        
        avg_score = sum(scores) / len(scores) if scores else 0
        return f"平均机会分数: {avg_score:.1f}/100\n最高分: {max(scores):.1f}\n最低分: {min(scores):.1f}"

    def _generate_resource_allocation(self, jobs: List[Dict]) -> str:
        """生成资源分配建议"""
        if not jobs:
            return "暂无 Job 数据"
        
        p0_count = sum(1 for j in jobs if j.get('opportunity_score', 0) >= 80)
        p1_count = sum(1 for j in jobs if 60 <= j.get('opportunity_score', 0) < 80)
        
        return f"""P0 级 Job: {p0_count} 个 - 分配 60% 资源
P1 级 Job: {p1_count} 个 - 分配 30% 资源
其他: {len(jobs) - p0_count - p1_count} 个 - 分配 10% 资源"""

    def _generate_validation_timeline(self, jobs: List[Dict]) -> str:
        """生成验证时间线"""
        if not jobs:
            return "暂无 Job 数据"
        
        p0_count = sum(1 for j in jobs if j.get('opportunity_score', 0) >= 80)
        p1_count = sum(1 for j in jobs if 60 <= j.get('opportunity_score', 0) < 80)
        
        return f"""第1-2周: P0 Job 用户验证（{p0_count} 个）
第3-4周: P1 Job 用户验证（{p1_count} 个）
第5-6周: MVP 开发
第7-8周: 数据收集与分析"""

    def _assess_willingness_to_pay(self, jobs: List[Dict]) -> str:
        """评估付费意愿"""
        if not jobs:
            return "暂无数据"
        
        high_wtp = sum(1 for j in jobs if j.get('willingness_to_pay', 'medium') == 'high')
        medium_wtp = sum(1 for j in jobs if j.get('willingness_to_pay', 'medium') == 'medium')
        
        return f"""高付费意愿: {high_wtp} 个 Job
中等付费意愿: {medium_wtp} 个 Job
低付费意愿: {len(jobs) - high_wtp - medium_wtp} 个 Job"""

    def _analyze_roi(self, jobs: List[Dict]) -> str:
        """分析投入产出"""
        if not jobs:
            return "暂无数据"
        
        total_potential = len(jobs) * 1000000
        estimated_cost = len(jobs) * 50000
        roi = (total_potential - estimated_cost) / estimated_cost * 100 if estimated_cost > 0 else 0
        
        return f"""潜在收益: ¥{total_potential:,}
预计成本: ¥{estimated_cost:,}
ROI: {roi:.1f}%"""

    def _make_go_no_go_decision(self, jobs: List[Dict]) -> str:
        """做出 Go/No-Go 决策"""
        if not jobs:
            return "数据不足，无法决策"
        
        avg_score = sum(j.get('opportunity_score', 0) for j in jobs) / len(jobs) if jobs else 0
        
        if avg_score >= 70:
            return f"""✅ **GO - 建议推进**

平均机会分数: {avg_score:.1f}/100
建议: 立即启动 P0 Job 开发，分配核心资源"""
        elif avg_score >= 50:
            return f"""⚠️ **条件推进**

平均机会分数: {avg_score:.1f}/100
建议: 先进行小规模验证，收集更多数据后再决策"""
        else:
            return f"""❌ **NO-GO - 暂不推进**

平均机会分数: {avg_score:.1f}/100
建议: 重新评估市场机会，或寻找新的 Job 方向"""


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
