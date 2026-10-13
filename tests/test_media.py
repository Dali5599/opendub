"""Tests for OpenDub media extractor and demuxer."""

import pytest
from opendub.media import MediaExtractor, MediaMetadata


def test_inspect_media_video(tmp_path):
    video = tmp_path / "movie.mp4"
    video.write_bytes(b"\x00\x00\x00\x18ftypmp42")

    extractor = MediaExtractor()
    meta = extractor.inspect_file(str(video))
    assert meta.has_video is True
    assert meta.has_audio is True
    assert len(meta.video_streams) == 1
    assert len(meta.audio_streams) == 1


def test_inspect_media_audio_only(tmp_path):
    audio = tmp_path / "sample.wav"
    audio.write_bytes(b"RIFF....WAVEfmt ")

    extractor = MediaExtractor()
    meta = extractor.inspect_file(str(audio))
    assert meta.has_video is False
    assert meta.has_audio is True


def test_build_extract_audio_cmd():
    extractor = MediaExtractor()
    cmd = extractor.build_extract_audio_cmd("input.mp4", "extracted.wav", sample_rate=16000, channels=1)
    assert cmd[0] == "ffmpeg"
    assert "-i" in cmd
    assert "input.mp4" in cmd
    assert "-ar" in cmd
    assert "16000" in cmd
    assert "extracted.wav" in cmd


def test_build_strip_audio_cmd():
    extractor = MediaExtractor()
    cmd = extractor.build_strip_audio_cmd("input.mp4", "silent.mp4")
    assert "-an" in cmd
    assert "-c:v" in cmd
    assert "copy" in cmd
