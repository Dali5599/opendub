"""Tests for OpenDub voice sampler and normalizer."""

import pytest
from opendub.models import SpeechSegment
from opendub.voice_sampler import VoiceSampler


def test_extract_best_sample_for_speaker(tmp_path):
    sampler = VoiceSampler()
    segments = [
        SpeechSegment(segment_id=1, speaker_id="HERO", start_time=1.0, end_time=2.5, original_text="Short"),
        SpeechSegment(segment_id=2, speaker_id="HERO", start_time=5.0, end_time=11.0, original_text="Long clean dialogue"),
    ]
    sample = sampler.extract_best_sample_for_speaker("HERO", segments, "vocals.wav", str(tmp_path))
    assert sample is not None
    assert sample.speaker_id == "HERO"
    assert sample.duration_seconds == 6.0
    assert "ref_HERO.wav" in sample.sample_path


def test_extract_all_speakers(tmp_path):
    sampler = VoiceSampler()
    segments = [
        SpeechSegment(segment_id=1, speaker_id="A", start_time=0.0, end_time=3.0, original_text="A"),
        SpeechSegment(segment_id=2, speaker_id="B", start_time=3.0, end_time=5.0, original_text="B"),
    ]
    samples = sampler.extract_all_speakers(segments, "vocals.wav", str(tmp_path))
    assert len(samples) == 2
    assert "A" in samples
    assert "B" in samples
