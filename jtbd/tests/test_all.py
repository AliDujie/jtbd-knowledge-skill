"""JTBD Knowledge Skill 全量测试"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from jtbd import (
    JTBDSkill,
    JTBDAnalyzer, JTBDStatement,
    InterviewBuilder, InterviewGuide,
    SurveyBuilder, Survey,
    ForcesProfile, render_forces_markdown,
    InnovationFinder,
    PriorityAnalyzer,
    CompetitionAnalyzer,
    MarketingCopywriter,
    GrowthStrategyBuilder,
)


def test_interview_generator():
    builder = InterviewBuilder("旅行预订用户访谈")
    builder.set_context("针对过去3个月内使用过竞品的用户")
    builder.include_dimensions(["competition", "push", "anxiety"])
    builder.add_custom_question("push", "最近一次出差住宿最大问题是什么？", priority=3)
    guide = builder.build()

    assert isinstance(guide, InterviewGuide)
    assert guide.title == "旅行预订用户访谈"
    assert guide.context == "针对过去3个月内使用过竞品的用户"
    assert len(guide.questions) > 0
    assert any(q.is_custom for q in guide.questions)
    assert len(guide.tips) > 0

    md = InterviewBuilder.render_markdown(guide)
    assert "旅行预订用户访谈" in md
    assert "竞争理解" in md
    assert "推力探索" in md

    comp_qs = guide.get_by_dimension("competition")
    assert len(comp_qs) > 0
    high = guide.get_high_priority(3)
    assert len(high) >= 1

    print("✅ test_interview_generator passed")


def test_survey_generator():
    builder = SurveyBuilder("旅行预订体验调研", "screening")
    builder.set_target("过去3个月使用过在线旅行预订的用户")
    builder.set_product("飞猪旅行")
    builder.set_struggles(["找酒店耗时", "价格不透明", "评价不可信"])
    builder.set_alternatives(["携程", "美团", "自己搜索"])
    survey = builder.build()

    assert isinstance(survey, Survey)
    assert survey.title == "旅行预订体验调研"
    assert survey.survey_type == "screening"
    assert len(survey.questions) >= 4

    md = SurveyBuilder.render_markdown(survey)
    assert "旅行预订体验调研" in md
    assert "筛选型问卷" in md
    assert "找酒店耗时" in md

    builder2 = SurveyBuilder("验证问卷", "validation")
    builder2.set_product("飞猪旅行")
    builder2.set_hypotheses(["快速找到合适住处", "省钱省时间"])
    builder2.set_struggles(["比价耗时", "信息不对称"])
    survey2 = builder2.build()
    assert len(survey2.questions) > 0

    print("✅ test_survey_generator passed")


def test_jtbd_analyzer():
    analyzer = JTBDAnalyzer("旅行预订平台")
    analyzer.set_overview("分析商旅用户的核心JTBD")
    analyzer.add_statement("Help me", "在出差时快速找到合适的住处", "专注于工作而不是为住宿烦恼")
    analyzer.add_force("push", "频繁出差导致每次都要花大量时间找酒店", intensity=4, evidence="用户访谈")
    analyzer.add_force("pull", "一键推荐符合差旅标准的酒店", intensity=3)
    analyzer.add_force("anxiety", "担心照片与实际不符", intensity=3)
    analyzer.add_force("inertia", "习惯用携程", intensity=2)

    balance = analyzer.get_demand_balance()
    assert balance["generating_total"] == 7
    assert balance["reducing_total"] == 5
    assert balance["net_demand"] == 2

    report = analyzer.generate_report()
    assert "旅行预订平台" in report
    assert "Help me" in report
    assert "强度 4/5" in report

    checklist = analyzer.run_innovation_checklist()
    assert len(checklist) > 0

    export = analyzer.export_json()
    assert export["project_name"] == "旅行预订平台"
    assert len(export["statements"]) == 1
    assert len(export["forces"]) == 4

    print("✅ test_jtbd_analyzer passed")


def test_forces_profile():
    profile = ForcesProfile()
    profile.add("push", "external", "市场竞争加剧", intensity=4, evidence="行业报告")
    profile.add("push", "internal", "用户投诉增多", intensity=3)
    profile.add("pull", "functional", "新方案效率提升50%", intensity=4)
    profile.add("anxiety", "choice", "担心迁移成本", intensity=3)
    profile.add("inertia", "habit", "团队已习惯旧流程", intensity=2)

    assert len(profile.items) == 5
    assert len(profile.by_type("push")) == 2
    assert profile.score("push") == 7
    assert profile.score("anxiety") == 3

    generating = profile.by_category("demand_generating")
    assert len(generating) == 3
    reducing = profile.by_category("demand_reducing")
    assert len(reducing) == 2

    diag = profile.diagnose()
    assert isinstance(diag, list)
    assert len(diag) > 0

    md = render_forces_markdown(profile)
    assert "推力" in md
    assert "市场竞争加剧" in md

    print("✅ test_forces_profile passed")


def test_innovation_finder():
    finder = InnovationFinder()
    finder.add_signal("compensating_behavior", "用户用Excel手动追踪行程和比价")
    finder.add_signal("unexpected_users", "发现大量自由职业者使用商旅功能")
    finder.add_signal("upstream_opportunity", "用户在预订前花大量时间做攻略")

    assert len(finder.signals) == 3

    finder.add_opportunity("自动比价工具", "基于用户历史偏好自动比价推荐", feasibility=3, impact=4)
    assert len(finder.opportunities) == 1
    assert finder.opportunities[0].impact == 4

    md = finder.render_markdown()
    assert "补偿行为" in md
    assert "Excel" in md
    assert "自动比价工具" in md

    assert len(finder.checklist_status) > 0

    print("✅ test_innovation_finder passed")


def test_priority_calculator():
    analyzer = PriorityAnalyzer()
    job = analyzer.add_job("在出差时快速找到合适住处", "Help me 快速找住处，这样我就能专注工作")
    analyzer.score_job(job, "struggle", 4, "用户平均花30分钟比价")
    analyzer.score_job(job, "alternative", 3, "携程可用但体验一般")
    analyzer.score_job(job, "market", 4, "商旅市场规模大")
    analyzer.score_job(job, "budget", 4, "企业有差旅预算")

    expected = 4 * 0.30 + 3 * 0.25 + 4 * 0.25 + 4 * 0.20
    assert job.opportunity_score == round(expected, 2)
    assert job.level == "中等机会"
    assert "验证" in job.action

    rubric = analyzer.get_rubric("struggle")
    assert 5 in rubric
    assert 1 in rubric

    print("✅ test_priority_calculator passed")


def test_priority_matrix():
    analyzer = PriorityAnalyzer()

    job1 = analyzer.add_job("快速找住处")
    analyzer.score_job(job1, "struggle", 5)
    analyzer.score_job(job1, "alternative", 4)
    analyzer.score_job(job1, "market", 4)
    analyzer.score_job(job1, "budget", 4)
    analyzer.score_forces(job1, push=4, pull=3, anxiety=2, inertia=1)

    job2 = analyzer.add_job("比价省钱")
    analyzer.score_job(job2, "struggle", 3)
    analyzer.score_job(job2, "alternative", 3)
    analyzer.score_job(job2, "market", 3)
    analyzer.score_job(job2, "budget", 2)

    ranked = analyzer.matrix.ranked()
    assert ranked[0].opportunity_score > ranked[1].opportunity_score
    assert ranked[0].job_description == "快速找住处"

    top = analyzer.matrix.top_n(1)
    assert len(top) == 1

    assert job1.net_force == (4 + 3) - (2 + 1)

    md = analyzer.render_markdown()
    assert "优先级矩阵" in md
    assert "快速找住处" in md
    assert "比价省钱" in md

    json_out = analyzer.render_json()
    assert len(json_out["jobs"]) == 2

    print("✅ test_priority_matrix passed")


def test_competition_analyzer():
    analyzer = CompetitionAnalyzer("飞猪旅行")
    analyzer.add_competitor("携程", "direct", strengths=["酒店资源丰富", "品牌知名度高"], weaknesses=["界面复杂", "价格不透明"])
    analyzer.add_competitor("美团", "indirect", strengths=["本地生活入口"], weaknesses=["旅行专业度不足"])
    analyzer.add_competitor("自己搜索", "non_consumption", strengths=["完全自由"], weaknesses=["极其耗时"])

    assert len(analyzer.analysis.competitors) == 3

    analyzer.add_switch("携程", "飞猪旅行", user_count=15, reason="价格更透明")
    assert len(analyzer.analysis.switch_evidence) == 1

    analyzer.auto_insights()
    assert len(analyzer.analysis.insights) > 0

    md = analyzer.render_markdown()
    assert "飞猪旅行" in md
    assert "携程" in md
    assert "直接竞品" in md

    print("✅ test_competition_analyzer passed")


def test_marketing_copywriter():
    writer = MarketingCopywriter()
    writer.set_brief("飞猪旅行", "快速找到合适住处", "每次出差花30分钟比价", "专注工作不为住宿烦恼", "landing_page")
    writer.add_anxiety("担心酒店照片与实际不符")
    writer.add_inertia("已经习惯用携程")

    plan = writer.generate()
    assert len(plan.drafts) == 3

    has_push = any(d.angle == "push_driven" for d in plan.drafts)
    has_pull = any(d.angle == "pull_driven" for d in plan.drafts)
    has_anxiety = any(d.angle == "anxiety_elimination" for d in plan.drafts)
    assert has_push and has_pull and has_anxiety

    for draft in plan.drafts:
        assert len(draft.headline) > 0
        assert len(draft.body) > 0

    md = MarketingCopywriter.render_markdown(plan)
    assert "飞猪旅行" in md
    assert "比价" in md or "出差" in md

    print("✅ test_marketing_copywriter passed")


def test_growth_strategy():
    builder = GrowthStrategyBuilder("飞猪旅行")
    builder.set_target_job("帮我快速找到合适的住处")
    builder.add_growth_opportunity("upstream", "出行前攻略服务", "AI行程规划", priority=4)
    builder.add_growth_opportunity("downstream", "入住后当地体验", "景点门票推荐", priority=3)
    builder.add_churn_segment("no_progress", "首周未完成预订的用户", 200)
    builder.add_churn_segment("better_alternative", "切换到携程的用户", 80)
    builder.add_key_habit("完成首次预订", best_pct=85, churned_pct=20, timeframe="首周")

    plan = builder.build()
    assert len(plan.growth_opportunities) == 2
    assert len(plan.churn_segments) == 2
    assert len(plan.key_habits) == 1
    assert plan.churn_segments[0].strategy != ""

    md = GrowthStrategyBuilder.render_markdown(plan)
    assert "飞猪旅行" in md
    assert "上游机会" in md
    assert "首周未完成预订" in md

    print("✅ test_growth_strategy passed")


def test_jtbd_statement():
    stmt = JTBDStatement(verb="Help me", struggle="在出差时快速找到合适的住处", desired_outcome="专注于工作而不是为住宿烦恼")
    rendered = stmt.render()
    assert "Help me" in rendered
    assert "快速找到合适的住处" in rendered
    assert "专注于工作" in rendered

    issues = stmt.validate()
    assert len(issues) == 0

    bad_stmt = JTBDStatement(verb="xyz", struggle="ab", desired_outcome="cd")
    bad_issues = bad_stmt.validate()
    assert len(bad_issues) >= 2

    skill = JTBDSkill("测试产品")
    result = skill.create_jtbd_statement("Help me", "快速找住处", "专注工作")
    assert "Help me" in result
    assert "快速找住处" in result

    print("✅ test_jtbd_statement passed")


def test_jtbd_skill_facade():
    """测试 JTBDSkill 门面类的初始化和基本属性"""
    skill = JTBDSkill("测试产品")

    # 验证所有子模块属性存在
    assert hasattr(skill, 'analyzer')
    assert hasattr(skill, 'priority_analyzer')
    assert hasattr(skill, 'competition_analyzer')
    assert hasattr(skill, 'innovation_finder')
    assert hasattr(skill, 'product')
    assert hasattr(skill, 'config')

    # 验证门面方法存在
    assert hasattr(skill, 'generate_interview')
    assert hasattr(skill, 'generate_survey')
    assert hasattr(skill, 'score_opportunity')
    assert hasattr(skill, 'add_job_to_matrix')
    assert hasattr(skill, 'render_priority_matrix')
    assert hasattr(skill, 'add_competitor')
    assert hasattr(skill, 'render_competition')
    assert hasattr(skill, 'generate_marketing_copy')
    assert hasattr(skill, 'generate_growth_strategy')
    assert hasattr(skill, 'create_jtbd_statement')
    assert hasattr(skill, 'add_force')
    assert hasattr(skill, 'generate_analysis_report')
    assert hasattr(skill, 'search_knowledge')
    assert hasattr(skill, 'analyze')

    # 验证 CEO 决策方法存在
    assert hasattr(skill, 'generate_market_size_estimate')
    assert hasattr(skill, 'generate_priority_scoring')
    assert hasattr(skill, 'generate_commercialization_feasibility')

    # 验证子模块类型
    assert isinstance(skill.analyzer, JTBDAnalyzer)
    assert isinstance(skill.priority_analyzer, PriorityAnalyzer)
    assert isinstance(skill.competition_analyzer, CompetitionAnalyzer)
    assert isinstance(skill.innovation_finder, InnovationFinder)

    print("✅ test_jtbd_skill_facade passed")


def test_empty_data_handling():
    """测试各模块在没有数据时的行为是否安全（不崩溃）"""
    skill = JTBDSkill("空数据测试")

    # CEO 方法在无数据时不应崩溃
    market = skill.generate_market_size_estimate()
    assert isinstance(market, str)
    assert len(market) > 0

    priority = skill.generate_priority_scoring()
    assert isinstance(priority, str)
    assert len(priority) > 0

    feasibility = skill.generate_commercialization_feasibility()
    assert isinstance(feasibility, str)
    assert len(feasibility) > 0

    # 空的分析报告不应崩溃
    report = skill.generate_analysis_report()
    assert isinstance(report, str)

    # 空的优先级矩阵
    matrix_md = skill.render_priority_matrix()
    assert isinstance(matrix_md, str)

    # 空的竞争分析
    comp_md = skill.render_competition()
    assert isinstance(comp_md, str)

    # 私有辅助方法在空数据时不应崩溃
    assert isinstance(skill._estimate_tam([]), str)
    assert isinstance(skill._estimate_sam([]), str)
    assert isinstance(skill._estimate_som([]), str)
    assert isinstance(skill._generate_validation_plan(), str)
    assert isinstance(skill._calculate_opportunity_scores([]), str)
    assert isinstance(skill._generate_resource_allocation([]), str)
    assert isinstance(skill._generate_validation_timeline([]), str)
    assert isinstance(skill._assess_willingness_to_pay([]), str)
    assert isinstance(skill._analyze_roi([]), str)
    assert isinstance(skill._make_go_no_go_decision([]), str)
    assert isinstance(skill._generate_recommendations({}), str)
    assert isinstance(skill._generate_p0_analysis({}), str)

    print("✅ test_empty_data_handling passed")


def test_jtbd_skill_analyze():
    """测试 analyze() 门面方法的基本功能"""
    skill = JTBDSkill("分析测试产品")
    skill.analyzer.set_overview("测试分析")
    skill.analyzer.add_statement("Help me", "快速找住处", "专注工作")
    skill.analyzer.add_force("push", "出差频繁", intensity=4)
    skill.analyzer.add_force("pull", "一键推荐", intensity=3)

    # 不包含 CEO 分析
    report_basic = skill.analyze(include_ceo_analysis=False)
    assert isinstance(report_basic, str)
    assert "分析测试产品" in report_basic
    assert "Help me" in report_basic
    assert "CEO" not in report_basic

    # 包含 CEO 分析
    report_full = skill.analyze(include_ceo_analysis=True)
    assert isinstance(report_full, str)
    assert "CEO 决策视角" in report_full
    assert "市场规模估算" in report_full
    assert "优先级评分" in report_full
    assert "商业化可行性" in report_full

    # 完整报告应比基本报告长
    assert len(report_full) > len(report_basic)

    print("✅ test_jtbd_skill_analyze passed")


if __name__ == "__main__":
    tests = [
        test_interview_generator,
        test_survey_generator,
        test_jtbd_analyzer,
        test_forces_profile,
        test_innovation_finder,
        test_priority_calculator,
        test_priority_matrix,
        test_competition_analyzer,
        test_marketing_copywriter,
        test_growth_strategy,
        test_jtbd_statement,
        test_jtbd_skill_facade,
        test_empty_data_handling,
        test_jtbd_skill_analyze,
    ]

    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"❌ {t.__name__} FAILED: {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"测试结果: {passed} passed, {failed} failed, {len(tests)} total")
    if failed == 0:
        print("🎉 全部 {0} 个测试通过！".format(len(tests)))
    else:
        print(f"⚠️ {failed} 个测试失败")
