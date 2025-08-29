from storylab.src.gpt_planner import GPTPlanner


def test_plan_contains_title_and_scenes():
    planner = GPTPlanner()
    plan = planner.plan("cats")
    assert plan["title"] == "Story about cats"
    assert plan["scenes"][0] == "cats scene 1"
    assert len(plan["scenes"]) == 3
