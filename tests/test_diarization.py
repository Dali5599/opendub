"""Tests for OpenDub speaker diarization engine."""

import pytest
from opendub.diarization import SpeakerDiarizationEngine
from opendub.models import SpeechSegment


def test_assign_speakers_by_cluster():
    engine = SpeakerDiarizationEngine()
    segments = [
        SpeechSegment(segment_id=1, start_time=0.0, end_time=2.0, original_text="Hi"),
        SpeechSegment(segment_id=2, start_time=2.5, end_time=4.0, original_text="Hello"),
    ]
    labeled = engine.assign_speakers_by_cluster(segments, [0, 1])
    assert labeled[0].speaker_id == "SPEAKER_00"
    assert labeled[1].speaker_id == "SPEAKER_01"


def test_group_dialogue_by_speaker():
    engine = SpeakerDiarizationEngine()
    segments = [
        SpeechSegment(segment_id=1, speaker_id="HERO", start_time=1.0, end_time=2.0, original_text="A"),
        SpeechSegment(segment_id=2, speaker_id="VILLAIN", start_time=2.0, end_time=3.0, original_text="B"),
        SpeechSegment(segment_id=3, speaker_id="HERO", start_time=3.0, end_time=4.0, original_text="C"),
    ]
    grouped = engine.group_dialogue_by_speaker(segments)
    assert len(grouped["HERO"]) == 2
    assert len(grouped["VILLAIN"]) == 1
    assert engine.detect_distinct_speakers(segments) == {"HERO", "VILLAIN"}
