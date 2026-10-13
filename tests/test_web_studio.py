"""Tests for OpenDub Web Studio."""

import pytest
from opendub.web_studio import WebStudioDashboard


def test_web_studio_html_content():
    html = WebStudioDashboard.get_html()
    assert "<!DOCTYPE html>" in html
    assert "OpenDub Studio" in html
    assert "Target Language" in html
    assert "Voice Cloner" in html
