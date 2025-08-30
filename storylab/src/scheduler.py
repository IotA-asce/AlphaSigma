"""Daily scheduler."""

from typing import Dict

from .gpt_planner import GPTPlanner
from .veo_client import VeoClient
from .styles import StyleRotator
from .publisher import Publisher


class Scheduler:
    """Coordinate planning, rendering and publishing."""

    def __init__(self,
                 planner: GPTPlanner,
                 renderer: VeoClient,
                 rotator: StyleRotator,
                 publisher: Publisher):
        self.planner = planner
        self.renderer = renderer
        self.rotator = rotator
        self.publisher = publisher

    def run_daily(self, topic: str) -> Dict[str, Dict[str, str] | str]:
        plan = self.planner.plan(topic)
        style = self.rotator.get_style()
        video = self.renderer.render(plan, style)
        publication = self.publisher.publish(video)
        return {"plan": plan, "video": video, "publication": publication}
