"""GPT-5 planning logic."""

from typing import List, Dict


class GPTPlanner:
    """Simple planner stub emulating GPT-5 logic."""

    def __init__(self, model: str = "gpt-5"):
        self.model = model

    def plan(self, topic: str) -> Dict[str, List[str]]:
        """Return a deterministic plan for the given topic."""
        title = f"Story about {topic}"
        scenes = [f"{topic} scene {i}" for i in range(1, 4)]
        return {"title": title, "scenes": scenes}
