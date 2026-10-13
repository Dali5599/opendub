"""Tests for OpenDub speech segment models and timeline."""

import pytest
from opendub.models import DubbingTimeline, SpeechSegment


def test_speech_segment_duration():
    seg = SpeechSegment(
        segment_id=1,
        speaker_id="SPEAKER_01",
        start_time=1.5,
        end_time=4.2,
        original_text="Hello world",
    )
    assert round(seg.duration, 2) == 2.70
    assert seg.speaker_id == "SPEAKER_01"


def test_dubbing_timeline_aggregation():
    timeline = DubbingTimeline(media_file="movie.mp4", source_language="en", target_language="fr")
    assert timeline.speaker_count == 0

    s1 = SpeechSegment(segment_id=1, speaker_id="ALICE", start_time=1.0, end_time=3.0, original_text="Hi")
    s2 = SpeechSegment(segment_id=2, speaker_id="BOB", start_time=3.5, end_time=6.0, original_text="Hey")
    s3 = SpeechSegment(segment_id=3, speaker_id="ALICE", start_time=6.5, end_time=9.0, original_text="Bye")

    timeline.add_segment(s2)  # Insert out of order
    timeline.add_segment(s1)
    timeline.add_segment(s3)

    assert timeline.speaker_count == 2
    assert timeline.total_duration_seconds == 9.0
    # Check automatic chronological sorting
    assert timeline.segments[0].speaker_id == "ALICE"
    assert timeline.segments[1].speaker_id == "BOB"
    assert len(timeline.get_speaker_segments("ALICE")) == 2
