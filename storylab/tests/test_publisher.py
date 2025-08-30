"""Tests for the publisher module."""

import logging

from storylab.src.publisher import Publisher


def test_publish_logs_uri(caplog):
    publisher = Publisher()
    video = {"uri": "https://example.com/video.mp4"}

    with caplog.at_level(logging.INFO):
        uri = publisher.publish(video)

    assert uri == video["uri"]
    assert video["uri"] in caplog.text

