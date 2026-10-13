"""Tests for OpenDub video remuxer."""

import pytest
from opendub.remuxer import VideoRemuxer


def test_build_remux_cmd_basic():
    remuxer = VideoRemuxer()
    cmd = remuxer.build_remux_cmd("orig.mp4", "dub.wav", "final.mp4")
    assert cmd[0] == "ffmpeg"
    assert "orig.mp4" in cmd
    assert "dub.wav" in cmd
    assert "final.mp4" in cmd
    assert "-c:v" in cmd
    assert "copy" in cmd


def test_build_remux_cmd_with_subtitles_and_offset():
    remuxer = VideoRemuxer()
    cmd = remuxer.build_remux_cmd(
        "orig.mp4", "dub.wav", "final.mp4", subtitles_srt="subs.srt", audio_delay_ms=120
    )
    assert "-itsoffset" in cmd
    assert "0.120" in cmd
    assert "subs.srt" in cmd
    assert "-c:s" in cmd
