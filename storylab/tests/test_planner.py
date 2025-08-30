import json
from types import SimpleNamespace

from storylab.src.gpt_planner import GPTPlanner, PLAN_SCHEMA


def test_plan_uses_json_schema_and_style_header():
    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        data = {"title": "Story about cats", "scenes": ["a", "b"]}
        return SimpleNamespace(
            output=[SimpleNamespace(content=[SimpleNamespace(text=json.dumps(data))])]
        )

    fake_client = SimpleNamespace(responses=SimpleNamespace(create=fake_create))
    planner = GPTPlanner(client=fake_client, model="test-model")

    plan = planner.plan("cats", style="comic")

    assert plan == {"title": "Story about cats", "scenes": ["a", "b"]}
    assert captured["response_format"]["json_schema"] == PLAN_SCHEMA
    assert captured["extra_headers"] == {"style": "comic"}
