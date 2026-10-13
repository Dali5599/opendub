"""Tests for OpenDub dialogue translator."""

import pytest
from opendub.models import SpeechSegment
from opendub.translator import DialogueTranslator


def test_build_translation_prompt():
    translator = DialogueTranslator(target_language="fr")
    segments = [
        SpeechSegment(segment_id=1, speaker_id="NEO", start_time=1.0, end_time=3.0, original_text="I know kung fu.")
    ]
    prompt = translator.build_translation_prompt(segments)
    assert "French" in prompt
    assert "NEO" in prompt
    assert "I know kung fu." in prompt
    assert "lip-synchronization" in prompt


def test_apply_translations():
    translator = DialogueTranslator(target_language="es")
    segments = [
        SpeechSegment(segment_id=1, start_time=0.0, end_time=2.0, original_text="Hello")
    ]
    updated = translator.apply_translations(segments, ["Hola"])
    assert updated[0].translated_text == "Hola"
    assert updated[0].original_text == "Hello"
