"""Tests for OpenDub subtitle generator."""

import pytest
from opendub.models import SpeechSegment
from opendub.subtitles import SubtitleGenerator


def test_srt_generation():
    segments = [
        SpeechSegment(
            segment_id=1,
            start_time=1.25,
            end_time=3.50,
            original_text="Welcome to OpenDub",
            translated_text="Bienvenue sur OpenDub",
        )
    ]

    srt_orig = SubtitleGenerator.generate_srt(segments, use_translation=False)
    assert "1" in srt_orig
    assert "00:00:01,250 --> 00:00:03,500" in srt_orig
    assert "Welcome to OpenDub" in srt_orig

    srt_trans = SubtitleGenerator.generate_srt(segments, use_translation=True)
    assert "Bienvenue sur OpenDub" in srt_trans


def test_vtt_generation():
    segments = [
        SpeechSegment(
            segment_id=1,
            start_time=0.0,
            end_time=2.0,
            original_text="Hello world",
        )
    ]
    vtt = SubtitleGenerator.generate_vtt(segments)
    assert "WEBVTT" in vtt
    assert "00:00:00.000 --> 00:00:02.000" in vtt
    assert "Hello world" in vtt
