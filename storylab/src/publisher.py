"""Content publisher placeholder.

This module logs the URI of a rendered video rather than publishing it to an
external service.  The :class:`Publisher` class is intentionally lightweight so
that it can be extended to support integrations with social platforms or
storage services.
"""

from __future__ import annotations

import logging
from typing import Dict

logger = logging.getLogger(__name__)


class Publisher:
    """Placeholder publisher that only logs video URIs.

    Subclass this class to push videos to destinations such as YouTube, TikTok
    or cloud object stores.  The default implementation simply records the URI
    of a rendered video for observability during development.
    """

    def publish(self, video: Dict[str, str]) -> str:
        """Log the video's URI and return it.

        Args:
            video: Mapping containing details about the rendered video. It is
                expected to provide a ``uri`` field identifying the location of
                the rendered asset.  A ``video`` key is used as a fallback for
                tests where a URI is not supplied.

        Returns:
            The URI that would be published.
        """

        uri = video.get("uri") or video.get("video", "")
        logger.info("Publishing video %s", uri)
        return uri

