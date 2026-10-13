"""Tests for OpenDub Whisper transcription client."""

import pytest
from opendub.transcription import WhisperTranscriptionClient


def test_parse_whisper_result():
    client = WhisperTranscriptionClient()
    raw = [
        {"start": 1.25, "end": 4.5, "text": "  Hello from Whisper  ", "confidence": 0.92, "speaker": "ALICE"}
    ]
    segments = client.parse_whisper_result(raw)
    assert len(segments) == 1
    seg = segments[0]
    assert seg.segment_id == 1
    assert seg.speaker_id == "ALICE"
    assert seg.start_time == 1.25
    assert seg.end_time == 4.5
    assert seg.original_text == "Hello from Whisper"
    assert seg.confidence == 0.92


def test_transcribe_fallback():
    client = WhisperTranscriptionClient(model_size="small")
    segments = client.transcribe("sample.wav")
    assert len(segments) == 2
    assert "cinematic movie" in segments[0].original_text
