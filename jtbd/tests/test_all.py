"""JTBD Knowledge Skill v3.0 全量测试"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from jtbd import (
    JTBDSkill,
    JTBDAnalyzer, JTBDStatement, STATEMENT_FORMATS,
    InterviewBuilder, InterviewGuide, INTERVIEW_TYPES,
    SurveyBuilder, Survey,
    ForcesProfile, render_forces_markdown,
    InnovationFinder,
    PriorityAnalyzer, ODI_INTERPRETATION,
    CompetitionAnalyzer, OutcomeComparison, DisruptionDiagnostic,
    MarketingCopywriter, VPC_TEMPLATE,
    GrowthStrategyBuilder, ODIStrategyChoice,
    JobMapBuilder, JobMap, StageNeed, JOB_MAP_STAGES,
    OutcomeBuilder, OutcomeSet, DesiredOutcome, NEED_TYPES,
    JobStoryBuilder, JobStorySet, JobStory,
    ObstacleAnalyzer, ObstacleDiagnosis, ObstacleItem, ADOPTION_OBSTACLES, USAGE_OBSTACLES,
    JobsAtlasBuilder, JobsAtlas, ATLAS_DIMENSIONS,
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


def test_interview_types():
    for itype in INTERVIEW_TYPES:
        builder = InterviewBuilder(f"{itype}访谈")
        builder.set_interview_type(itype)
        guide = builder.build()
        assert len(guide.questions) > 0
        md = InterviewBuilder.render_markdown(guide)
        assert len(md) > 0

    print("✅ test_interview_types passed")


def test_survey_generator():
    builder = SurveyBuilder("旅行预订体验调研", "screening")
    builder.set_target("过去3个月使用过在线旅行预订的用户")
    builder.set_product("旅行预订平台")
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
    builder2.set_product("旅行预订平台")
    builder2.set_hypotheses(["快速找到合适住处", "省钱省时间"])
    builder2.set_struggles(["比价耗时", "信息不对称"])
    survey2 = builder2.build()
    assert len(survey2.questions) > 0

    print("✅ test_survey_generator passed")


def test_odi_survey():
    builder = SurveyBuilder("ODI量表", "odi_outcome")
    builder.set_product("旅行预订平台")
    builder.set_outcomes(["快速找到合适酒店", "价格透明可比较"])
    survey = builder.build()

    assert survey.survey_type == "odi_outcome"
    assert len(survey.questions) > 0
    assert survey.sample_size_note != ""

    md = SurveyBuilder.render_markdown(survey)
    assert "ODI" in md or "odi" in md.lower() or "Outcome" in md

    builder2 = SurveyBuilder("Job评分", "jobs_scoring")
    builder2.set_product("旅行预订平台")
    builder2.set_jobs(["快速找住处", "比价省钱"])
    survey2 = builder2.build()
    assert len(survey2.questions) > 0

    print("✅ test_odi_survey passed")


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


def test_multi_format_statement():
    analyzer = JTBDAnalyzer("测试项目")

    stmt1 = analyzer.add_statement("Help me", "快速找住处", "专注工作")
    assert stmt1.statement_format == "klement"
    assert "Help me" in stmt1.render()

    stmt2 = analyzer.add_outcome_statement(
        direction="minimize", metric="the time",
        object_of_control="finding a suitable hotel",
        clarifier="when traveling for business")
    assert stmt2.statement_format == "outcome"
    rendered2 = stmt2.render()
    assert "minimize" in rendered2.lower() or "Minimize" in rendered2

    stmt3 = analyzer.add_job_story(
        situation="出差需要住酒店",
        want="快速找到合适的住处",
        outcome="专注工作而不是为住宿烦恼")
    assert stmt3.statement_format == "job_story"

    stmt4 = analyzer.add_traditional_statement(
        role="商务旅客",
        want="快速找到合适的酒店",
        outcome="专注工作")
    assert stmt4.statement_format == "traditional"

    analysis = analyzer.analysis
    assert len(analysis.statements) == 4
    klement_stmts = analysis.get_statements_by_format("klement")
    assert len(klement_stmts) == 1
    outcome_stmts = analysis.get_statements_by_format("outcome")
    assert len(outcome_stmts) == 1

    print("✅ test_multi_format_statement passed")


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


def test_odi_scoring():
    analyzer = PriorityAnalyzer()
    job = analyzer.add_job("快速找到合适酒店")
    analyzer.score_odi(job, importance=8, satisfaction=3)

    expected_odi = 8 + max(8 - 3, 0)
    assert job.odi_opportunity == expected_odi
    assert job.odi_level != "未评估"
    assert job.odi_action != "需要评估"

    strategy = analyzer.suggest_strategy(job)
    assert strategy != ""

    job2 = analyzer.add_job("查看酒店照片")
    analyzer.score_odi(job2, importance=3, satisfaction=8)
    assert job2.odi_opportunity == 3 + max(3 - 8, 0)
    assert job2.odi_opportunity == 3.0

    matrix = analyzer.matrix
    underserved = matrix.get_underserved()
    overserved = matrix.get_overserved()
    assert len(underserved) + len(overserved) <= len(matrix.jobs)

    print("✅ test_odi_scoring passed")


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
    analyzer = CompetitionAnalyzer("旅行预订平台")
    analyzer.add_competitor("携程", "direct", strengths=["酒店资源丰富", "品牌知名度高"], weaknesses=["界面复杂", "价格不透明"])
    analyzer.add_competitor("美团", "indirect", strengths=["本地生活入口"], weaknesses=["旅行专业度不足"])
    analyzer.add_competitor("自己搜索", "non_consumption", strengths=["完全自由"], weaknesses=["极其耗时"])

    assert len(analyzer.analysis.competitors) == 3

    analyzer.add_switch("携程", "旅行预订平台", user_count=15, reason="价格更透明")
    assert len(analyzer.analysis.switch_evidence) == 1

    analyzer.auto_insights()
    assert len(analyzer.analysis.insights) > 0

    md = analyzer.render_markdown()
    assert "旅行预订平台" in md
    assert "携程" in md
    assert "直接竞品" in md

    print("✅ test_competition_analyzer passed")


def test_outcome_comparison():
    analyzer = CompetitionAnalyzer("旅行预订平台")
    analyzer.add_competitor("携程", "direct", strengths=["品牌"], weaknesses=["价格"])

    comp = analyzer.add_outcome_comparison("最小化找酒店时间", 7, "携程", 5)
    assert isinstance(comp, OutcomeComparison)
    assert comp.gap == 2

    comp2 = analyzer.add_outcome_comparison("最小化价格不透明", 4, "携程", 8)
    assert comp2.gap == -4

    diag = analyzer.add_disruption(
        "AI旅行助手",
        disruptor_advantages=["智能推荐", "自动比价"],
        our_advantages=["供应链", "售后服务"],
        adoption_barriers=["AI信任度低"],
        threat_level="medium")
    assert isinstance(diag, DisruptionDiagnostic)
    assert diag.threat_level == "medium"

    analyzer.auto_insights()
    md = analyzer.render_markdown()
    assert "Outcome" in md or "outcome" in md.lower() or "满意度" in md

    print("✅ test_outcome_comparison passed")


def test_marketing_copywriter():
    writer = MarketingCopywriter()
    writer.set_brief("旅行预订平台", "快速找到合适住处", "每次出差花30分钟比价", "专注工作不为住宿烦恼", "landing_page")
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
    assert "旅行预订平台" in md
    assert "比价" in md or "出差" in md

    print("✅ test_marketing_copywriter passed")


def test_vpc_marketing():
    writer = MarketingCopywriter()
    writer.set_brief("旅行预订平台", "快速找到合适住处", "每次出差花30分钟比价", "专注工作", "landing_page")
    writer.set_vpc(
        executor="商务出差人群",
        current_approach="手动在多个平台比价",
        value_proposition="一站式智能比价推荐")
    writer.add_outcome("3分钟内找到最优价格酒店")

    plan = writer.generate()
    assert plan.vpc_statement != ""
    assert plan.vpc_statement_zh != ""

    md = MarketingCopywriter.render_markdown(plan)
    assert "VPC" in md or "价值主张" in md

    print("✅ test_vpc_marketing passed")


def test_growth_strategy():
    builder = GrowthStrategyBuilder("旅行预订平台")
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
    assert "旅行预订平台" in md
    assert "上游机会" in md
    assert "首周未完成预订" in md

    print("✅ test_growth_strategy passed")


def test_odi_growth_strategy():
    builder = GrowthStrategyBuilder("旅行预订平台")
    builder.set_target_job("帮我快速找到合适的住处")
    builder.set_odi_strategy("differentiated", "多个Outcome未满足，聚焦差异化")

    plan = builder.build()
    assert plan.odi_strategy is not None
    assert plan.odi_strategy.strategy == "differentiated"

    md = GrowthStrategyBuilder.render_markdown(plan)
    assert "ODI" in md or "增长策略" in md

    print("✅ test_odi_growth_strategy passed")


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


def test_job_map():
    builder = JobMapBuilder("预订商务出行酒店")
    builder.set_executor("商务旅客")
    builder.add_need("define", "确定出差日期和目的地", importance=9, satisfaction=7)
    builder.add_need("locate", "搜索符合差旅标准的酒店", importance=8, satisfaction=4)
    builder.add_need("execute", "完成预订流程", importance=7, satisfaction=6)
    builder.add_need("conclude", "获取发票和报销凭证", importance=8, satisfaction=3)

    job_map = builder.build()
    assert isinstance(job_map, JobMap)
    assert job_map.job_statement == "预订商务出行酒店"
    assert job_map.executor == "商务旅客"
    all_needs = []
    for s in job_map.stages.values():
        all_needs.extend(s.needs)
    assert len(all_needs) == 4

    locate_stage = job_map.get_stage("locate")
    assert locate_stage is not None
    assert len(locate_stage.needs) == 1
    assert locate_stage.needs[0].importance == 8

    top = job_map.get_top_opportunities(2)
    assert len(top) == 2
    assert top[0].opportunity >= top[1].opportunity

    md = JobMapBuilder.render_markdown(job_map)
    assert "预订商务出行酒店" in md
    assert "商务旅客" in md
    assert "Define" in md or "定义" in md

    json_out = JobMapBuilder.render_json(job_map)
    assert json_out["job_statement"] == "预订商务出行酒店"

    print("✅ test_job_map passed")


def test_outcome_statement():
    builder = OutcomeBuilder("预订商务出行酒店")
    builder.add_outcome(
        direction="minimize", metric="the time",
        object_of_control="finding a suitable hotel",
        clarifier="when traveling for business",
        importance=8, satisfaction=3)
    builder.add_outcome(
        direction="minimize", metric="the likelihood",
        object_of_control="booking a hotel that doesn't match its photos",
        importance=9, satisfaction=4)
    builder.add_outcome_simple(
        direction="maximize",
        description_zh="预算估算的准确性",
        importance=6, satisfaction=7,
        need_type="financial")

    outcome_set = builder.build()
    assert isinstance(outcome_set, OutcomeSet)
    assert len(outcome_set.outcomes) == 3

    landscape = outcome_set.get_opportunity_landscape()
    assert "underserved" in landscape
    assert "overserved" in landscape
    assert "appropriately_served" in landscape

    first = outcome_set.outcomes[0]
    assert first.opportunity == 8 + max(8 - 3, 0)

    md = OutcomeBuilder.render_markdown(outcome_set)
    assert "Desired Outcome" in md or "Outcome" in md
    assert "minimize" in md.lower() or "Minimize" in md

    json_out = OutcomeBuilder.render_json(outcome_set)
    assert json_out["total_outcomes"] == 3

    print("✅ test_outcome_statement passed")


def test_job_stories():
    builder = JobStoryBuilder("预订商务出行酒店")
    builder.add_story(
        "intercom",
        situation="出差需要住酒店",
        motivation="快速找到合适的住处",
        outcome="专注工作而不是为住宿烦恼")
    builder.add_story(
        "kalbach",
        situation="临时接到出差通知",
        motivation="快速预订符合差旅标准的酒店",
        outcome="不用担心报销问题",
        emotional_trigger="时间紧迫带来的焦虑")
    builder.add_story_zh(
        "intercom",
        situation="出差需要住酒店",
        motivation="快速找到合适的住处",
        outcome="专注工作而不是为住宿烦恼")

    story_set = builder.build()
    assert isinstance(story_set, JobStorySet)
    assert len(story_set.stories) == 3

    md = JobStoryBuilder.render_markdown(story_set)
    assert "预订商务出行酒店" in md
    assert "出差" in md or "When" in md

    json_out = JobStoryBuilder.render_json(story_set)
    assert len(json_out["stories"]) == 3

    print("✅ test_job_stories passed")


def test_obstacles():
    analyzer = ObstacleAnalyzer("旅行预订平台")
    analyzer.set_target_job("快速找到合适的商务酒店")
    analyzer.add_obstacle(
        "lack_of_knowledge", "用户不知道平台有商旅专属功能",
        severity=4, evidence="访谈中80%用户不知道商旅频道")
    analyzer.add_obstacle(
        "high_cost", "高星酒店价格偏高",
        severity=3)
    analyzer.add_obstacle(
        "usage_pain_points", "搜索结果排序不够智能",
        severity=3)
    analyzer.add_inertia_strategy("lower_trial_barriers")
    analyzer.add_inertia_strategy("social_proof")

    diagnosis = analyzer.build()
    assert isinstance(diagnosis, ObstacleDiagnosis)
    assert len(diagnosis.obstacles) == 3

    adoption = diagnosis.adoption_obstacles()
    usage = diagnosis.usage_obstacles()
    assert len(adoption) == 2
    assert len(usage) == 1

    for item in diagnosis.obstacles:
        assert len(item.countermeasures) > 0

    md = ObstacleAnalyzer.render_markdown(diagnosis)
    assert "旅行预订平台" in md
    assert "采用障碍" in md or "障碍" in md

    print("✅ test_obstacles passed")


def test_jobs_atlas():
    builder = JobsAtlasBuilder("旅行预订平台")
    builder.set_core_job("快速找到合适的商务酒店")
    builder.add_related_job("管理差旅报销")
    builder.add_driver("circumstances", "临时出差通知，时间紧迫", influence_level=5)
    builder.add_driver("attitudes", "公司倡导节约差旅费用", influence_level=3)
    builder.add_driver("background", "每月出差2-3次的商务人士", influence_level=4)
    builder.add_current_approach(
        "携程", "老牌OTA平台",
        pain_points=["界面复杂", "价格不透明"],
        workarounds=["用比价网站辅助"])
    builder.add_success_criterion(
        "5分钟内完成预订", "从打开到确认的时间",
        current_score=6, target_score=9, priority=5)
    builder.add_obstacle("不知道平台有商旅功能")
    builder.add_value("functional", "一站式比价节省时间", magnitude=4)
    builder.add_value("emotional", "预订后的安心感", magnitude=3)
    builder.add_competitor(
        "携程", job_overlap="商务酒店预订",
        strengths=["品牌", "资源"], weaknesses=["价格"],
        threat_level=4)

    atlas = builder.build()
    assert isinstance(atlas, JobsAtlas)
    assert atlas.core_job == "快速找到合适的商务酒店"
    assert len(atlas.drivers) == 3
    assert len(atlas.current_approaches) == 1
    assert len(atlas.success_criteria) == 1
    assert len(atlas.obstacles) == 1
    assert len(atlas.values) == 2
    assert len(atlas.competitors) == 1

    completeness = atlas.completeness()
    assert isinstance(completeness, dict)
    filled = sum(1 for v in completeness.values() if v)
    assert filled >= 5

    md = JobsAtlasBuilder.render_markdown(atlas)
    assert "旅行预订平台" in md
    assert "Jobs Atlas" in md or "Atlas" in md
    assert "携程" in md

    print("✅ test_jobs_atlas passed")


def test_skill_unified_api():
    skill = JTBDSkill("旅行预订平台")

    guide = skill.generate_interview("测试访谈", ["competition", "push"])
    assert "测试访谈" in guide

    survey = skill.generate_survey("测试问卷", "screening", struggles=["找酒店慢"])
    assert "测试问卷" in survey

    score = skill.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)
    assert "score" in score
    assert "level" in score

    odi = skill.score_odi("快速找住处", importance=8, satisfaction=3)
    assert "odi_score" in odi
    assert "odi_level" in odi
    assert "suggested_strategy" in odi
    assert odi["odi_score"] == 8 + max(8 - 3, 0)

    jm = skill.create_job_map("预订商务出行酒店", executor="商务旅客")
    assert isinstance(jm, JobMapBuilder)

    ob = skill.create_outcome_statements("预订商务出行酒店")
    assert isinstance(ob, OutcomeBuilder)

    js = skill.create_job_stories("预订商务出行酒店")
    assert isinstance(js, JobStoryBuilder)

    diag = skill.diagnose_obstacles()
    assert isinstance(diag, ObstacleAnalyzer)

    atlas = skill.create_jobs_atlas("预订商务出行酒店")
    assert isinstance(atlas, JobsAtlasBuilder)

    stmt = skill.create_jtbd_statement("Help me", "快速找住处", "专注工作")
    assert "Help me" in stmt

    outcome = skill.create_outcome_statement(
        direction="minimize", metric="the time",
        object_of_control="finding a suitable hotel")
    assert len(outcome) > 0

    print("✅ test_skill_unified_api passed")


def test_knowledge_search():
    from jtbd import search_knowledge, load_knowledge

    results = search_knowledge("焦虑")
    assert isinstance(results, dict)
    found_count = sum(len(v) for v in results.values())
    assert found_count > 0

    content = load_knowledge("theory")
    assert len(content) > 0

    odi_content = load_knowledge("odi")
    assert len(odi_content) > 0
    assert "Opportunity" in odi_content or "ODI" in odi_content

    atlas_content = load_knowledge("atlas")
    assert len(atlas_content) > 0

    glossary_content = load_knowledge("glossary")
    assert len(glossary_content) > 0

    print("✅ test_knowledge_search passed")


def test_version():
    from jtbd import __version__
    assert __version__ == "3.0.0"
    print("✅ test_version passed")


if __name__ == "__main__":
    tests = [
        test_interview_generator,
        test_interview_types,
        test_survey_generator,
        test_odi_survey,
        test_jtbd_analyzer,
        test_multi_format_statement,
        test_forces_profile,
        test_innovation_finder,
        test_priority_calculator,
        test_odi_scoring,
        test_priority_matrix,
        test_competition_analyzer,
        test_outcome_comparison,
        test_marketing_copywriter,
        test_vpc_marketing,
        test_growth_strategy,
        test_odi_growth_strategy,
        test_jtbd_statement,
        test_job_map,
        test_outcome_statement,
        test_job_stories,
        test_obstacles,
        test_jobs_atlas,
        test_skill_unified_api,
        test_knowledge_search,
        test_version,
    ]

    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"❌ {t.__name__} FAILED: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print(f"\n{'='*50}")
    print(f"测试结果: {passed} passed, {failed} failed, {len(tests)} total")
    if failed == 0:
        print(f"🎉 全部 {len(tests)} 个测试通过！")
    else:
        print(f"⚠️ {failed} 个测试失败")
