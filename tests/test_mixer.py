"""Tests for OpenDub audio mixer and ducking engine."""

import pytest
from opendub.mixer import AudioMixer


def test_build_ducking_filter_graph():
    filter_graph = AudioMixer.build_ducking_filter_graph(0, 1)
    assert "sidechaincompress" in filter_graph
    assert "amix=inputs=2" in filter_graph


def test_build_full_mix_cmd():
    cmd = AudioMixer.build_full_mix_cmd("vocals.wav", "music.wav", "master.wav")
    assert cmd[0] == "ffmpeg"
    assert "-i" in cmd
    assert "vocals.wav" in cmd
    assert "music.wav" in cmd
    assert "master.wav" in cmd
