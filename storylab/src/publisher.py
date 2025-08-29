"""Content publisher stub."""

from typing import Dict


class Publisher:
    """Pretend to publish videos to a platform."""

    def publish(self, video: Dict[str, str]) -> str:
        return f"Published {video.get('video', 'video')}"
