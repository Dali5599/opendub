"""Tests for OpenDub audio time stretcher."""

import pytest
from opendub.timestretch import AudioTimeStretcher


def test_speed_factor_calculation():
    # Audio takes 4s in target language, slot in movie is 3s -> must speed up by 1.33x
    ratio, clamped = AudioTimeStretcher.calculate_speed_factor(original_duration=3.0, new_duration=4.0)
    assert ratio == 1.333
    assert clamped is False


def test_speed_factor_clamping():
    # Audio is twice as long (6s vs 2s) -> clamp to MAX_SPEED_RATIO (1.6)
    ratio, clamped = AudioTimeStretcher.calculate_speed_factor(original_duration=2.0, new_duration=6.0)
    assert ratio == 1.6
    assert clamped is True


def test_build_rubberband_filter():
    assert AudioTimeStretcher.build_rubberband_filter(1.0) == "anull"
    assert AudioTimeStretcher.build_rubberband_filter(1.25) == "atempo=1.250"


def test_build_ffmpeg_timestretch_cmd():
    cmd = AudioTimeStretcher.build_ffmpeg_timestretch_cmd("in.wav", "out.wav", speed_factor=1.2)
    assert cmd[0] == "ffmpeg"
    assert "in.wav" in cmd
    assert "out.wav" in cmd
    assert "atempo=1.200" in cmd
