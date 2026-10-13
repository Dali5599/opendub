"""Tests for OpenDub audio stem separator."""

from pathlib import Path
import pytest
from opendub.stems import SeparatedStems, StemSeparator


def test_build_demucs_cmd():
    separator = StemSeparator(model_name="htdemucs_ft", device="cuda")
    cmd = separator.build_demucs_cmd("audio.wav", "/tmp/out")
    assert cmd[0] == "demucs"
    assert "--two-stems=vocals" in cmd
    assert "-n" in cmd
    assert "htdemucs_ft" in cmd
    assert "-d" in cmd
    assert "cuda" in cmd
    assert "audio.wav" in cmd


def test_separate_generates_stems(tmp_path):
    input_wav = tmp_path / "dialogue.wav"
    input_wav.write_bytes(b"audio_bytes")

    separator = StemSeparator()
    stems = separator.separate(str(input_wav), str(tmp_path / "stems"))

    assert Path(stems.vocals_path).is_file()
    assert Path(stems.accompaniment_path).is_file()
    assert stems.duration_seconds == 30.0
    assert "vocals" in stems.vocals_path
    assert "accompaniment" in stems.accompaniment_path
