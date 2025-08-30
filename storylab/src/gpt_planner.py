"""GPT planning logic using the OpenAI responses API."""

from __future__ import annotations

import json
from typing import Any, Dict, List

try:  # pragma: no cover - optional dependency
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore

# JSON schema used for structured output from the model.
PLAN_SCHEMA = {
    "name": "plan",
    "schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "scenes": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
            },
        },
        "required": ["title", "scenes"],
        "additionalProperties": False,
    },
}


class GPTPlanner:
    """Planner that requests a structured story plan from GPT."""

    def __init__(self, model: str = "gpt-5", client: Any | None = None):
        self.model = model
        if client is not None:
            self.client = client
        else:
            if OpenAI is None:
                raise RuntimeError("openai package is required when no client is provided")
            self.client = OpenAI()

    def plan(self, topic: str, style: str | None = None) -> Dict[str, List[str]]:
        """Return a plan for the given topic.

        Parameters
        ----------
        topic:
            The subject to plan a story about.
        style:
            Optional visual style hint that is forwarded as a custom HTTP
            header to the API.
        """

        headers = {"style": style} if style else None
        resp = self.client.responses.create(
            model=self.model,
            input=[{"role": "user", "content": [{"type": "text", "text": topic}]}],
            response_format={"type": "json_schema", "json_schema": PLAN_SCHEMA},
            extra_headers=headers,
        )
        raw = resp.output[0].content[0].text
        return json.loads(raw)
