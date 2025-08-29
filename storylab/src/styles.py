"""Style rotation utilities."""

from typing import List


class StyleRotator:
    """Rotate through a list of visual styles."""

    def __init__(self, styles: List[str] | None = None):
        self.styles = styles or ["cinematic", "comic", "watercolor"]
        self._index = 0

    def get_style(self) -> str:
        style = self.styles[self._index]
        self._index = (self._index + 1) % len(self.styles)
        return style
