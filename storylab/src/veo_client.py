"""Veo-3 rendering client stub."""

from typing import Dict, List


class VeoClient:
    """Client that renders a plan into a video."""

    def __init__(self, model: str = "veo-3"):
        self.model = model

    def render(self, plan: Dict[str, List[str]], style: str) -> Dict[str, str]:
        title = plan.get("title", "untitled")
        return {"video": f"Rendered {title} in {style} style"}
