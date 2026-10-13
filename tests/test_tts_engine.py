"""Tests for OpenDub TTS and voice cloning adapter."""

import pytest
from opendub.models import SpeechSegment
from opendub.tts_engine import TTSConfig, VoiceCloningTTSEngine
from opendub.voice_sampler import VoiceSample


def test_synthesize_speech(tmp_path):
    engine = VoiceCloningTTSEngine(TTSConfig(engine_name="mock"))
    out_file = tmp_path / "dub.wav"
    res = engine.synthesize_speech("Hello", output_wav_path=str(out_file))
    assert res == str(out_file)
    assert out_file.is_file()


def test_synthesize_segment(tmp_path):
    engine = VoiceCloningTTSEngine()
    seg = SpeechSegment(
        segment_id=5,
        speaker_id="NARRATOR",
        start_time=1.0,
        end_time=3.0,
        original_text="Once upon a time",
        translated_text="Il était une fois",
    )
    v_ref = VoiceSample(speaker_id="NARRATOR", sample_path="ref.wav", duration_seconds=4.0)

    updated = engine.synthesize_segment(seg, {"NARRATOR": v_ref}, str(tmp_path))
    assert updated.dubbed_audio_path is not None
    assert "dub_seg_0005_NARRATOR.wav" in updated.dubbed_audio_path
