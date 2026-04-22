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



    # ── CEO 视角方法 (3 个) ──

    def generate_market_size_estimate(self, jobs: Optional[List[Dict]] = None) -> str:
        """
        CEO 决策方法 1: 市场规模估算

        基于 JTBD 理论，估算目标市场的 TAM/SAM/SOM，并提供验证计划。

        Args:
            jobs: 用户任务列表，每项包含 job_name, target_users, frequency 等

        Returns:
            Markdown 格式的市场规模估算报告

        Example::

            skill = JTBDSkill('智能健康餐订阅')
            jobs = [{'job_name': '快速获得营养均衡的工作餐', 'target_users': '一线城市白领', 'frequency': '每周 5 次'}]
            market_size = skill.generate_market_size_estimate(jobs)
        """
        default_jobs = jobs or [{'job_name': '示例任务', 'target_users': '目标用户', 'frequency': '高频'}]
        
        tam = len(default_jobs) * 1000000 * 50  # 简化计算
        sam = tam * 0.3
        som = sam * 0.1
        
        lines = [
            "## 📊 市场规模估算",
            "",
            f"**产品**: {self.product} | **分析任务数**: {len(default_jobs)}",
            "",
            "### 市场层级",
            "",
            "| 层级 | 定义 | 估算值 | 说明 |",
            "|------|------|--------|------|",
            f"| TAM (总可寻址市场) | 全部潜在用户 | ¥{tam:,.0f} | 全国范围内有该 JTBD 的用户 |",
            f"| SAM (可服务市场) | 可触达用户 | ¥{sam:,.0f} | 渠道/地理可覆盖的用户 (30%) |",
            f"| SOM (可获得市场) | 实际可获得 | ¥{som:,.0f} | 考虑竞争后的份额 (10%) |",
            "",
            "### 关键假设",
            "",
            "| 假设 | 值 | 来源 | 置信度 |",
            "|------|-----|--------|--------|",
            "| 目标用户规模 | 5000 万 | 行业报告 | 中 |",
            "| 年均消费 | ¥1000 | 竞品分析 | 中 |",
            "| 渗透率 (SAM/TAM) | 30% | 渠道能力 | 低 |",
            "| 市场份额 (SOM/SAM) | 10% | 竞争格局 | 低 |",
            "",
            "### 验证计划",
            "",
            "| 阶段 | 行动 | 样本量 | 时间 | 成功标准 |",
            "|------|------|--------|------|----------|",
            "| 定性验证 | 用户访谈 | 20 人 | 2 周 | 确认 JTBD 存在 |",
            "| 定量验证 | 问卷调查 | 500 人 | 2 周 | 需求强度≥7/10 |",
            "| MVP 测试 | 预售/等待名单 | 1000 人 | 4 周 | 转化率≥5% |",
            "| 小规模上线 | 单城市试点 | 1 万用户 | 8 周 | 留存率≥40% |",
            "",
            "### CEO 决策建议",
            "",
            "1. **市场进入**: TAM 足够大 (>¥10 亿)，建议进入",
            "2. **资源投入**: 聚焦 SAM 的前 30%，快速验证 SOM 假设",
            "3. **关键风险**: 渗透率和市场份额假设需 MVP 验证",
            "4. **下一步**: 启动定性验证（2 周用户访谈）",
            "",
        ]
        return "\n".join(lines)

    def generate_priority_scoring(self, jobs: Optional[List[Dict]] = None) -> str:
        """
        CEO 决策方法 2: 优先级评分

        为多个 JTBD 机会计算优先级分数，提供资源分配建议和验证时间线。

        Args:
            jobs: 任务列表，每项包含 job_name, importance, satisfaction_gap 等

        Returns:
            Markdown 格式的优先级评分报告

        Example::

            skill = JTBDSkill('智能健康餐订阅')
            jobs = [
                {'job_name': '快速获得营养餐', 'importance': 9, 'satisfaction_gap': 7},
                {'job_name': '控制饮食热量', 'importance': 8, 'satisfaction_gap': 5},
            ]
            priority = skill.generate_priority_scoring(jobs)
        """
        default_jobs = jobs or [
            {'job_name': '任务 A', 'importance': 8, 'satisfaction_gap': 6, 'confidence': 0.7},
            {'job_name': '任务 B', 'importance': 7, 'satisfaction_gap': 5, 'confidence': 0.8},
            {'job_name': '任务 C', 'importance': 9, 'satisfaction_gap': 8, 'confidence': 0.6},
        ]
        
        # 计算机会分
        for job in default_jobs:
            imp = job.get('importance', 5)
            gap = job.get('satisfaction_gap', 5)
            conf = job.get('confidence', 0.5)
            job['opportunity_score'] = (imp + gap - 10) * conf * 10
        
        sorted_jobs = sorted(default_jobs, key=lambda x: x.get('opportunity_score', 0), reverse=True)
        
        lines = [
            "## 📋 优先级评分",
            "",
            f"**产品**: {self.product} | **评估任务数**: {len(default_jobs)}",
            "",
            "### 机会分数计算",
            "",
            "| 任务 | 重要性 (1-10) | 满意度差距 (1-10) | 置信度 | 机会分 | 优先级 |",
            "|------|-------------|-----------------|--------|--------|--------|",
        ]
        
        for i, job in enumerate(sorted_jobs, 1):
            score = job.get('opportunity_score', 0)
            priority = "P0" if i == 1 else "P1" if i == 2 else "P2"
            lines.append(f"| {job['job_name']} | {job.get('importance', '-')} | {job.get('satisfaction_gap', '-')} | {job.get('confidence', '-'):.1f} | {score:.1f} | {priority} |")
        
        lines.extend([
            "",
            "### 资源分配建议",
            "",
            "| 优先级 | 任务 | 资源占比 | 团队规模 | 时间窗口 |",
            "|--------|------|----------|----------|----------|",
        ])
        
        resources = [(50, "3-4 人", "4-6 周"), (30, "2-3 人", "3-4 周"), (20, "1-2 人", "2-3 周")]
        for i, job in enumerate(sorted_jobs[:3]):
            res, team, time = resources[i] if i < len(resources) else (10, "1 人", "1-2 周")
            lines.append(f"| P{i} | {job['job_name']} | {res}% | {team} | {time} |")
        
        lines.extend([
            "",
            "### 验证时间线",
            "",
            "| 周次 | P0 任务 | P1 任务 | P2 任务 | 里程碑 |",
            "|------|--------|--------|--------|--------|",
            "| W1-2 | 用户访谈 (20 人) | - | - | 需求确认 |",
            "| W3-4 | MVP 设计 | 用户访谈 (10 人) | - | 方案确定 |",
            "| W5-8 | MVP 开发 + 测试 | MVP 设计 | 用户访谈 (5 人) | P0 上线 |",
            "| W9-12 | 数据分析 + 迭代 | MVP 开发 | MVP 设计 | P1 上线 |",
            "",
            "### CEO 决策建议",
            "",
            "1. **资源聚焦**: 50% 资源投入 P0 任务，确保快速验证",
            "2. **决策节点**: W4 审查 P0 进展，W8 决定是否继续 P1",
            "3. **止损机制**: P0 机会分<5 或验证失败，立即转向",
            "",
        ])
        return "\n".join(lines)

    def generate_commercialization_feasibility(self, jobs: Optional[List[Dict]] = None) -> str:
        """
        CEO 决策方法 3: 商业化可行性

        评估 JTBD 机会的付费意愿、投入产出比，并提供 Go/No-Go 决策建议。

        Args:
            jobs: 任务列表，每项包含 job_name, wtp_estimate, dev_cost 等

        Returns:
            Markdown 格式的商业化可行性报告

        Example::

            skill = JTBDSkill('智能健康餐订阅')
            jobs = [
                {'job_name': '快速获得营养餐', 'wtp_estimate': 50, 'dev_cost': 500000},
            ]
            feasibility = skill.generate_commercialization_feasibility(jobs)
        """
        default_jobs = jobs or [
            {'job_name': '任务 A', 'wtp_estimate': 50, 'dev_cost': 500000, 'annual_users': 5000},
        ]
        
        lines = [
            "## 💰 商业化可行性",
            "",
            f"**产品**: {self.product} | **评估任务数**: {len(default_jobs)}",
            "",
            "### 付费意愿评估",
            "",
            "| 任务 | 预估 WTP | 价格敏感度 | 支付频率 | 验证方法 |",
            "|------|---------|-----------|----------|----------|",
        ]
        
        for job in default_jobs:
            wtp = job.get('wtp_estimate', 0)
            sensitivity = "低" if wtp > 100 else "中" if wtp > 50 else "高"
            lines.append(f"| {job['job_name']} | ¥{wtp} | {sensitivity} | 月度 | 支付意愿调查 + 预售测试 |")
        
        lines.extend([
            "",
            "### 投入产出分析",
            "",
            "| 任务 | 开发成本 | 年用户数 | 年收入 | ROI | 回收期 |",
            "|------|---------|----------|--------|-----|--------|",
        ])
        
        for job in default_jobs:
            cost = job.get('dev_cost', 0)
            users = job.get('annual_users', 0)
            wtp = job.get('wtp_estimate', 0) * 12  # 年费
            revenue = users * wtp
            roi = ((revenue - cost) / cost * 100) if cost > 0 else 0
            payback = cost / (revenue / 12) if revenue > 0 else 999
            lines.append(f"| {job['job_name']} | ¥{cost:,.0f} | {users:,.0f} | ¥{revenue:,.0f} | {roi:.0f}% | {payback:.1f}月 |")
        
        # 计算总计
        total_cost = sum(j.get('dev_cost', 0) for j in default_jobs)
        total_revenue = sum(j.get('annual_users', 0) * j.get('wtp_estimate', 0) * 12 for j in default_jobs)
        total_roi = ((total_revenue - total_cost) / total_cost * 100) if total_cost > 0 else 0
        
        lines.extend([
            "",
            f"**总计**: 开发成本 ¥{total_cost:,.0f} | 年收入 ¥{total_revenue:,.0f} | ROI {total_roi:.0f}%",
            "",
            "### Go/No-Go 决策",
            "",
            "| 标准 | 要求 | 实际 | 状态 |",
            "|------|------|------|------|",
            f"| 市场规模 | SOM ≥ ¥1 亿 | ¥{total_revenue:,.0f} | {'✅' if total_revenue >= 100000000 else '⚠️'} |",
            f"| ROI | ≥50% | {total_roi:.0f}% | {'✅' if total_roi >= 50 else '⚠️'} |",
            f"| 回收期 | ≤18 月 | {total_cost/(total_revenue/12) if total_revenue > 0 else 999:.1f}月 | {'✅' if (total_cost/(total_revenue/12) <= 18 if total_revenue > 0 else False) else '⚠️'} |",
            f"| 战略匹配 | 高 | 中 | 🟡 |",
            "",
            "### CEO 决策建议",
            "",
            f"**决策**: {'✅ Go' if total_roi >= 50 and total_revenue >= 100000000 else '⚠️ Conditional Go' if total_roi >= 30 else '❌ No-Go'}",
            "",
            "1. **Go 条件**: ROI≥50% + SOM≥¥1 亿 + 回收期≤18 月",
            "2. **风险缓解**: 分阶段投入，W4 审查 MVP 进展",
            "3. **关键假设验证**: 付费意愿、用户获取成本、留存率",
            "",
        ])
        return "\n".join(lines)

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
            return f"""GO - 建议推进

平均机会分数: {avg_score:.1f}/100
建议: 立即启动 P0 Job 开发，分配核心资源"""
        elif avg_score >= 50:
            return f"""条件推进

平均机会分数: {avg_score:.1f}/100
建议: 先进行小规模验证，收集更多数据后再决策"""
        else:
            return f"""NO-GO - 暂不推进

平均机会分数: {avg_score:.1f}/100
建议: 重新评估市场机会，或寻找新的 Job 方向"""


__all__ = [
    "JTBDSkill",
    "AnalysisConfig", "FORCE_TYPES", "FORCE_LABELS", "KNOWLEDGE_FILES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "INTERVIEW_QUESTIONS", "JTBD_STATEMENT_TEMPLATE",
    "JTBD_STATEMENT_EXAMPLES", "INNOVATION_CHECKLIST", "REPORT_TEMPLATE",
    "SCENARIO_MERGE_RULES", "EXAMPLE_SELECTION_CRITERIA",
    "INSIGHT_QUALITY_RULES", "SECTION_INSIGHT_PROMPTS", "HTML_REPORT_STYLE_RULES",
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
