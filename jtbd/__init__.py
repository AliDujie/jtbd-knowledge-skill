"""JTBD (Jobs to Be Done) Python Toolkit v3.0

融合三大JTBD学派的完整工具包:
- Klement 学派: 进步力量、切换访谈、情感分析
- Ulwick ODI 学派: Opportunity Algorithm、Desired Outcome、Universal Job Map
- Wunker Jobs Atlas 学派: 七维度分析、障碍诊断、ABC Job Drivers
- Kalbach 整合学派: Job Stories、VPC整合、多格式描述

覆盖 SKILL.md 全部执行能力:
1. 访谈提纲生成（含Switch/ODI/Churn三种类型）
2. 调查问卷生成（含ODI Outcome配对量表）
3. 机会评分（四维模型 + ODI Opportunity Algorithm）
4. 优先级矩阵与策略建议
5. 竞争分析（含Outcome对比 + 颠覆诊断）
6. 营销文案（含VPC价值主张）
7. 增长策略（含ODI五策略矩阵）
8. JTBD描述（Klement/Outcome/Job Story/Traditional四格式）
9. Universal Job Map 构建
10. Desired Outcome Statement 管理
11. Job Stories 生成（四种变体）
12. 采用障碍诊断
13. Jobs Atlas 七维度构建

快速开始::

    from jtbd import JTBDSkill
    skill = JTBDSkill("旅行预订平台")

    # 基础能力
    guide = skill.generate_interview("用户访谈", ["competition", "push"])
    survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])

    # ODI 能力
    score = skill.score_odi("快速找住处", importance=8, satisfaction=3)
    job_map = skill.create_job_map("预订商务出行酒店")
    outcomes = skill.create_outcome_statements("预订商务出行酒店")

    # Atlas 能力
    atlas = skill.create_jobs_atlas("预订商务出行酒店")
    obstacles = skill.diagnose_obstacles("旅行预订平台")

    # 分析报告
    report = skill.generate_analysis_report()
"""

__version__ = "3.0.0"

from .config import (
    AnalysisConfig, FORCE_TYPES, FORCE_LABELS, KNOWLEDGE_FILES,
    INTERVIEW_DIMENSIONS, ALL_INTERVIEW_DIMENSIONS,
    JTBD_STATEMENT_FORMATS,
)
from .utils import load_knowledge, load_all_knowledge, search_knowledge
from .templates import (
    INTERVIEW_QUESTIONS, JTBD_STATEMENT_TEMPLATE,
    JTBD_STATEMENT_EXAMPLES, INNOVATION_CHECKLIST, REPORT_TEMPLATE,
    SCENARIO_MERGE_RULES, EXAMPLE_SELECTION_CRITERIA,
    INSIGHT_QUALITY_RULES, SECTION_INSIGHT_PROMPTS, HTML_REPORT_STYLE_RULES,
    OUTCOME_STATEMENT_TEMPLATE, OUTCOME_STATEMENT_EXAMPLES,
    JOB_STORY_TEMPLATES, JOB_STORY_EXAMPLES,
    OBSTACLE_CHECKLIST,
)
from .jtbd_analyzer import (
    JTBDAnalyzer, JTBDAnalysis, JTBDStatement,
    STATEMENT_FORMATS, STATEMENT_FORMAT_LABELS,
)
from .interview_generator import (
    InterviewBuilder, InterviewGuide,
    ALL_INTERVIEW_DIMENSIONS as INTERVIEW_ALL_DIMS,
    INTERVIEW_TYPES, EXTENDED_QUESTIONS,
)
from .forces import ForcesProfile, ForceItem, render_forces_markdown
from .innovation import InnovationFinder, InnovationSignal, InnovationOpportunity
from .survey_generator import SurveyBuilder, Survey, ODI_SAMPLE_SIZE_GUIDANCE
from .priority_calculator import (
    PriorityAnalyzer, JobScore, PriorityMatrix,
    ODI_INTERPRETATION, ODI_STRATEGIES,
)
from .competition import (
    CompetitionAnalyzer, CompetitiveAnalysis, Competitor,
    OutcomeComparison, DisruptionDiagnostic,
)
from .marketing import (
    MarketingCopywriter, CopyPlan, CopyBrief,
    VPC_TEMPLATE, VPC_TEMPLATE_ZH,
)
from .growth import (
    GrowthStrategyBuilder, GrowthPlan,
    ODIStrategyChoice, ODI_GROWTH_STRATEGIES, PRODUCT_STRATEGY_ACTIONS,
)
from .job_map import JobMapBuilder, JobMap, JobMapStage, StageNeed, JOB_MAP_STAGES
from .outcome_statement import (
    OutcomeBuilder, OutcomeSet, DesiredOutcome,
    OUTCOME_DIRECTIONS, NEED_TYPES,
)
from .job_stories import JobStoryBuilder, JobStorySet, JobStory
from .obstacles import (
    ObstacleAnalyzer, ObstacleDiagnosis, ObstacleItem,
    ADOPTION_OBSTACLES, USAGE_OBSTACLES,
)
from .jobs_atlas import JobsAtlasBuilder, JobsAtlas, ATLAS_DIMENSIONS

from typing import Dict, List, Optional


class JTBDSkill:
    """JTBD 统一入口类 — 封装全部执行能力

    用法::

        skill = JTBDSkill("旅行预订平台")

        # 能力1: 访谈提纲（支持Switch/ODI/Churn三种类型）
        guide = skill.generate_interview("用户访谈", ["competition", "push", "anxiety"])
        odi_guide = skill.generate_interview("ODI访谈", interview_type="odi")

        # 能力2: 调查问卷（支持ODI配对量表）
        survey = skill.generate_survey("体验调研", "screening", struggles=["找酒店耗时"])
        odi_survey = skill.generate_survey("ODI量表", "odi_outcome")

        # 能力3: 机会评分（四维模型 + ODI双轨）
        score = skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)
        odi = skill.score_odi("快速找住处", importance=8, satisfaction=3)

        # 能力4: 优先级矩阵
        skill.add_job_to_matrix("快速找住处", struggle=4, alternative=3, market=4, budget=4)
        matrix = skill.render_priority_matrix()

        # 能力5: 竞争分析（含Outcome对比 + 颠覆诊断）
        skill.add_competitor("携程", "direct", strengths=["酒店多"], weaknesses=["界面复杂"])
        competition = skill.render_competition()

        # 能力6: 营销文案（含VPC价值主张）
        copy = skill.generate_marketing_copy(struggle="花30分钟比价", desired_outcome="专注工作")

        # 能力7: 增长策略（含ODI五策略矩阵）
        growth = skill.generate_growth_strategy(churn_segments=[("no_progress", "首周未预订", 200)])

        # 能力8: JTBD描述（四种格式）
        stmt = skill.create_jtbd_statement("Help me", "快速找住处", "专注工作")
        outcome = skill.create_outcome_statement(
            direction="minimize", metric="the time",
            obj="finding a suitable hotel", clarifier="when traveling for business"
        )

        # 能力9: Universal Job Map
        jm = skill.create_job_map("预订商务出行酒店")
        jm.add_need("define", "确定出差日期和目的地", importance=9, satisfaction=7)
        job_map = jm.build()

        # 能力10: Desired Outcome 管理
        ob = skill.create_outcome_statements("预订商务出行酒店")
        ob.add("minimize", "the time", "finding a suitable hotel", "when traveling for business")
        outcome_set = ob.build()

        # 能力11: Job Stories（四种变体）
        js = skill.create_job_stories("预订商务出行酒店")
        js.add("出差需要住酒店", "快速找到合适的住处", "专注工作而不是为住宿烦恼")
        stories = js.build()

        # 能力12: 障碍诊断
        diag = skill.diagnose_obstacles("旅行预订平台")
        diag.add_obstacle("adoption", "lack_of_knowledge", severity=4)
        diagnosis = diag.build()

        # 能力13: Jobs Atlas
        atlas = skill.create_jobs_atlas("预订商务出行酒店")
        atlas.add_job("快速找到合适的住处")
        atlas_result = atlas.build()
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
                           context: str = "",
                           interview_type: str = "") -> str:
        builder = InterviewBuilder(title, self.config)
        if context:
            builder.set_context(context)
        if interview_type:
            builder.set_interview_type(interview_type)
        if dimensions:
            builder.include_dimensions(dimensions)
        guide = builder.build()
        return InterviewBuilder.render_markdown(guide)

    def generate_survey(self, title: str, survey_type: str,
                        struggles: Optional[List[str]] = None,
                        alternatives: Optional[List[str]] = None,
                        hypotheses: Optional[List[str]] = None,
                        outcomes: Optional[List[str]] = None,
                        jobs: Optional[List[str]] = None) -> str:
        builder = SurveyBuilder(title, survey_type)
        builder.set_product(self.product)
        if struggles:
            builder.set_struggles(struggles)
        if alternatives:
            builder.set_alternatives(alternatives)
        if hypotheses:
            builder.set_hypotheses(hypotheses)
        if outcomes:
            builder.set_outcomes(outcomes)
        if jobs:
            builder.set_jobs(jobs)
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

    def score_odi(self, job_desc: str, importance: int = 5,
                  satisfaction: int = 5) -> Dict:
        job = self.priority_analyzer.add_job(job_desc)
        self.priority_analyzer.score_odi(job, importance, satisfaction)
        strategy = self.priority_analyzer.suggest_strategy(job)
        return {
            "importance": importance,
            "satisfaction": satisfaction,
            "odi_score": job.odi_opportunity,
            "odi_level": job.odi_level,
            "suggested_strategy": strategy,
        }

    def add_job_to_matrix(self, job_desc: str, struggle: int = 3,
                          alternative: int = 3, market: int = 3, budget: int = 3,
                          push: int = 0, pull: int = 0,
                          anxiety: int = 0, inertia: int = 0,
                          importance: int = 0, satisfaction: int = 0) -> JobScore:
        job = self.priority_analyzer.add_job(job_desc)
        self.priority_analyzer.score_job(job, "struggle", struggle)
        self.priority_analyzer.score_job(job, "alternative", alternative)
        self.priority_analyzer.score_job(job, "market", market)
        self.priority_analyzer.score_job(job, "budget", budget)
        if any([push, pull, anxiety, inertia]):
            self.priority_analyzer.score_forces(job, push, pull, anxiety, inertia)
        if importance > 0 and satisfaction > 0:
            self.priority_analyzer.score_odi(job, importance, satisfaction)
        return job

    def render_priority_matrix(self) -> str:
        return self.priority_analyzer.render_markdown()

    def add_competitor(self, name: str, category: str = "direct",
                       strengths: Optional[List[str]] = None,
                       weaknesses: Optional[List[str]] = None) -> None:
        self.competition_analyzer.add_competitor(
            name, category, strengths=strengths or [], weaknesses=weaknesses or [])

    def add_outcome_comparison(self, outcome_desc: str, our_satisfaction: int,
                               competitor_name: str, their_satisfaction: int) -> None:
        self.competition_analyzer.add_outcome_comparison(
            outcome_desc, our_satisfaction, competitor_name, their_satisfaction)

    def add_disruption(self, disruptor_name: str,
                       disruptor_advantages: Optional[List[str]] = None,
                       our_advantages: Optional[List[str]] = None,
                       adoption_barriers: Optional[List[str]] = None,
                       threat_level: str = "medium") -> None:
        self.competition_analyzer.add_disruption(
            disruptor_name,
            disruptor_advantages=disruptor_advantages,
            our_advantages=our_advantages,
            adoption_barriers=adoption_barriers,
            threat_level=threat_level)

    def render_competition(self) -> str:
        self.competition_analyzer.auto_insights()
        return self.competition_analyzer.render_markdown()

    def generate_marketing_copy(self, struggle: str, desired_outcome: str,
                                purpose: str = "landing_page",
                                anxieties: Optional[List[str]] = None,
                                inertias: Optional[List[str]] = None,
                                executor: str = "",
                                current_approach: str = "",
                                value_proposition: str = "") -> str:
        writer = MarketingCopywriter()
        writer.set_brief(self.product, f"{self.product}的核心Job",
                         struggle, desired_outcome, purpose)
        if executor or current_approach or value_proposition:
            writer.set_vpc(
                executor=executor or "目标用户",
                current_approach=current_approach or "现有方案",
                value_proposition=value_proposition or f"{self.product}的差异化价值",
            )
        for a in (anxieties or []):
            writer.add_anxiety(a)
        for i in (inertias or []):
            writer.add_inertia(i)
        plan = writer.generate()
        return MarketingCopywriter.render_markdown(plan)

    def generate_growth_strategy(self, target_job: str = "",
                                 growth_opps: Optional[List[tuple]] = None,
                                 churn_segments: Optional[List[tuple]] = None,
                                 key_habits: Optional[List[tuple]] = None,
                                 odi_strategy: str = "",
                                 odi_rationale: str = "") -> str:
        builder = GrowthStrategyBuilder(self.product)
        if target_job:
            builder.set_target_job(target_job)
        if odi_strategy:
            builder.set_odi_strategy(odi_strategy, odi_rationale)
        for opp in (growth_opps or []):
            builder.add_growth_opportunity(*opp)
        for seg in (churn_segments or []):
            builder.add_churn_segment(*seg)
        for hab in (key_habits or []):
            builder.add_key_habit(*hab)
        plan = builder.build()
        return GrowthStrategyBuilder.render_markdown(plan)

    def create_jtbd_statement(self, verb: str, struggle: str,
                              desired_outcome: str,
                              statement_format: str = "klement") -> str:
        if statement_format == "klement":
            stmt = self.analyzer.add_statement(verb, struggle, desired_outcome)
            return stmt.render()
        elif statement_format == "outcome":
            stmt = self.analyzer.add_outcome_statement(
                direction=verb, metric=struggle,
                object_of_control=desired_outcome, clarifier="")
            return stmt.render()
        elif statement_format == "job_story":
            stmt = self.analyzer.add_job_story(
                situation=verb, want=struggle,
                outcome=desired_outcome)
            return stmt.render()
        else:
            stmt = self.analyzer.add_traditional_statement(
                role=verb, want=struggle, outcome=desired_outcome)
            return stmt.render()

    def create_outcome_statement(self, direction: str, metric: str,
                                 object_of_control: str,
                                 clarifier: str = "") -> str:
        stmt = self.analyzer.add_outcome_statement(
            direction=direction, metric=metric,
            object_of_control=object_of_control, clarifier=clarifier)
        return stmt.render()

    def create_job_map(self, job_statement: str,
                       executor: str = "") -> JobMapBuilder:
        builder = JobMapBuilder(job_statement)
        if executor:
            builder.set_executor(executor)
        return builder

    def create_outcome_statements(self, job_statement: str) -> OutcomeBuilder:
        return OutcomeBuilder(job_statement)

    def create_job_stories(self, job_statement: str) -> JobStoryBuilder:
        return JobStoryBuilder(job_statement)

    def diagnose_obstacles(self, product_name: str = "") -> ObstacleAnalyzer:
        return ObstacleAnalyzer(product_name or self.product)

    def create_jobs_atlas(self, job_statement: str) -> JobsAtlasBuilder:
        return JobsAtlasBuilder(job_statement)

    def add_force(self, force_type: str, description: str,
                  intensity: int = 3, evidence: str = "") -> None:
        self.analyzer.add_force(force_type, description, intensity, evidence)

    def generate_analysis_report(self) -> str:
        return self.analyzer.generate_report()

    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)

    def generate_market_size_estimate(self, jobs: Optional[List[Dict]] = None) -> str:
        if not jobs:
            jobs = []

        tam_estimate = self._estimate_tam(jobs)
        sam_estimate = self._estimate_sam(jobs)
        som_estimate = self._estimate_som(jobs)
        validation_plan = self._generate_validation_plan()

        report = f"""## 市场规模估算

> 注意: 以下估算基于Job数据的相对强度推导，仅供内部讨论参考，
> 需通过市场调研、行业报告和用户验证进一步校准。

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
        return f"""### P0 级 Job 深度分析: {job.get('description', '未知')}

**核心痛点**: {job.get('struggle', '未定义')}
**期望结果**: {job.get('desired_outcome', '未定义')}
**机会分数**: {job.get('opportunity_score', 0)}/100

**市场特征**:
- 用户规模: {job.get('market_size', '待验证')}
- 付费意愿: {job.get('willingness_to_pay', '待验证')}
- 竞争强度: {job.get('competition_level', '待验证')}

**建议行动**:
{self._generate_recommendations(job)}
"""

    def _generate_recommendations(self, job: Dict) -> str:
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
        if not jobs:
            return "暂无Job数据，请先添加Job并评分后再进行市场估算。"

        high_struggle_count = sum(1 for j in jobs if j.get('struggle', 0) >= 4)
        avg_struggle = sum(j.get('struggle', 3) for j in jobs) / len(jobs) if jobs else 0
        market_signal = "强" if avg_struggle >= 3.5 else "中" if avg_struggle >= 2.5 else "弱"

        return f"""基于 {len(jobs)} 个Job的痛点强度分析:
- 高痛点Job(≥4分): {high_struggle_count} 个
- 平均痛点强度: {avg_struggle:.1f}/5
- 市场信号: {market_signal}
- TAM估算需结合行业报告验证，建议参考: 目标用户群体规模 × 年均消费频次 × 单次价值"""

    def _estimate_sam(self, jobs: List[Dict]) -> str:
        if not jobs:
            return "暂无Job数据。"

        serviceable_count = sum(1 for j in jobs if j.get('market', 0) >= 3)
        ratio = serviceable_count / len(jobs) * 100 if jobs else 0

        return f"""基于产品能力与市场匹配度:
- 可服务Job占比: {serviceable_count}/{len(jobs)} ({ratio:.0f}%)
- SAM = TAM × 产品覆盖率（需根据产品定位具体计算）
- 建议: 聚焦高痛点+高市场评分的交叉Job"""

    def _estimate_som(self, jobs: List[Dict]) -> str:
        if not jobs:
            return "暂无Job数据。"

        high_score_count = sum(
            1 for j in jobs
            if j.get('opportunity_score', 0) >= 60
        )

        return f"""基于当前竞争力和资源:
- 高机会Job(≥60分): {high_score_count} 个
- SOM = SAM × 预期市场份额（需根据竞争分析确定）
- 首年建议: 聚焦{min(high_score_count, 3)}个P0级Job，快速验证PMF"""

    def _generate_validation_plan(self) -> str:
        return """1. 第1-2周: 用户访谈验证Job真实性（n≥15）
2. 第3周: ODI问卷量化重要性-满意度（n≥150）
3. 第4-6周: MVP原型测试核心Job（n≥30）
4. 第7-8周: A/B测试关键体验指标
总计: 8周 | 每阶段设置明确的Go/No-Go标准"""

    def _calculate_opportunity_scores(self, jobs: List[Dict]) -> str:
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
        if not jobs:
            return "暂无 Job 数据"

        p0_count = sum(1 for j in jobs if j.get('opportunity_score', 0) >= 80)
        p1_count = sum(1 for j in jobs if 60 <= j.get('opportunity_score', 0) < 80)

        return f"""P0 级 Job: {p0_count} 个 - 分配 60% 资源
P1 级 Job: {p1_count} 个 - 分配 30% 资源
其他: {len(jobs) - p0_count - p1_count} 个 - 分配 10% 资源"""

    def _generate_validation_timeline(self, jobs: List[Dict]) -> str:
        if not jobs:
            return "暂无 Job 数据"

        p0_count = sum(1 for j in jobs if j.get('opportunity_score', 0) >= 80)
        p1_count = sum(1 for j in jobs if 60 <= j.get('opportunity_score', 0) < 80)

        return f"""第1-2周: P0 Job 用户验证（{p0_count} 个）
第3-4周: P1 Job 用户验证（{p1_count} 个）
第5-6周: MVP 开发
第7-8周: 数据收集与分析"""

    def _assess_willingness_to_pay(self, jobs: List[Dict]) -> str:
        if not jobs:
            return "暂无数据"

        high_wtp = sum(1 for j in jobs if j.get('willingness_to_pay', 'medium') == 'high')
        medium_wtp = sum(1 for j in jobs if j.get('willingness_to_pay', 'medium') == 'medium')

        return f"""高付费意愿: {high_wtp} 个 Job
中等付费意愿: {medium_wtp} 个 Job
低付费意愿: {len(jobs) - high_wtp - medium_wtp} 个 Job

付费意愿评估建议: 通过Van Westendorp价格敏感度测试或Gabor-Granger定价分析进一步验证"""

    def _analyze_roi(self, jobs: List[Dict]) -> str:
        if not jobs:
            return "暂无数据"

        avg_struggle = sum(j.get('struggle', 3) for j in jobs) / len(jobs)
        avg_market = sum(j.get('market', 3) for j in jobs) / len(jobs)
        roi_signal = "高" if avg_struggle >= 4 and avg_market >= 4 else "中" if avg_struggle >= 3 else "低"

        return f"""ROI信号强度: {roi_signal}
- 平均痛点强度: {avg_struggle:.1f}/5（痛点越强 → 付费意愿越高）
- 平均市场评分: {avg_market:.1f}/5（市场越大 → 收益天花板越高）
- 建议: 具体ROI需结合定价策略、获客成本(CAC)、客户生命周期价值(LTV)计算
- 初步判断: {"值得投入，预期正向ROI" if roi_signal != "低" else "需谨慎评估，建议先小规模验证"}"""

    def _make_go_no_go_decision(self, jobs: List[Dict]) -> str:
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
    "__version__",
    "AnalysisConfig", "FORCE_TYPES", "FORCE_LABELS", "KNOWLEDGE_FILES",
    "INTERVIEW_DIMENSIONS", "ALL_INTERVIEW_DIMENSIONS", "JTBD_STATEMENT_FORMATS",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "INTERVIEW_QUESTIONS", "JTBD_STATEMENT_TEMPLATE",
    "JTBD_STATEMENT_EXAMPLES", "INNOVATION_CHECKLIST", "REPORT_TEMPLATE",
    "OUTCOME_STATEMENT_TEMPLATE", "OUTCOME_STATEMENT_EXAMPLES",
    "JOB_STORY_TEMPLATES", "JOB_STORY_EXAMPLES", "OBSTACLE_CHECKLIST",
    "JTBDAnalyzer", "JTBDAnalysis", "JTBDStatement",
    "STATEMENT_FORMATS", "STATEMENT_FORMAT_LABELS",
    "InterviewBuilder", "InterviewGuide",
    "INTERVIEW_TYPES", "EXTENDED_QUESTIONS",
    "ForcesProfile", "ForceItem", "render_forces_markdown",
    "InnovationFinder", "InnovationSignal", "InnovationOpportunity",
    "SurveyBuilder", "Survey", "ODI_SAMPLE_SIZE_GUIDANCE",
    "PriorityAnalyzer", "JobScore", "PriorityMatrix",
    "ODI_INTERPRETATION", "ODI_STRATEGIES",
    "CompetitionAnalyzer", "CompetitiveAnalysis", "Competitor",
    "OutcomeComparison", "DisruptionDiagnostic",
    "MarketingCopywriter", "CopyPlan", "CopyBrief",
    "VPC_TEMPLATE", "VPC_TEMPLATE_ZH",
    "GrowthStrategyBuilder", "GrowthPlan",
    "ODIStrategyChoice", "ODI_GROWTH_STRATEGIES", "PRODUCT_STRATEGY_ACTIONS",
    "JobMapBuilder", "JobMap", "JobMapStage", "StageNeed", "JOB_MAP_STAGES",
    "OutcomeBuilder", "OutcomeSet", "DesiredOutcome",
    "OUTCOME_DIRECTIONS", "NEED_TYPES",
    "JobStoryBuilder", "JobStorySet", "JobStory",
    "ObstacleAnalyzer", "ObstacleDiagnosis", "ObstacleItem",
    "ADOPTION_OBSTACLES", "USAGE_OBSTACLES",
    "JobsAtlasBuilder", "JobsAtlas", "ATLAS_DIMENSIONS",
]
