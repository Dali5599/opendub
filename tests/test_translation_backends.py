"""Tests for OpenDub translation backends."""

from unittest.mock import MagicMock, patch
import pytest
from opendub.models import SpeechSegment
from opendub.translation_backends import TranslationBackend, TranslationBackendConfig


def test_mock_backend():
    backend = TranslationBackend(TranslationBackendConfig(backend_type="mock"))
    seg = SpeechSegment(segment_id=1, start_time=0.0, end_time=2.0, original_text="Good night")
    tr = backend.translate_segment(seg, "fr")
    assert tr == "[FR] Good night"


@patch("httpx.Client.post")
def test_ollama_backend_translation(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"response": "Bonne nuit"}
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    backend = TranslationBackend(TranslationBackendConfig(backend_type="ollama"))
    seg = SpeechSegment(segment_id=1, start_time=0.0, end_time=2.0, original_text="Good night")
    translated = backend.translate_all([seg], "fr")

    assert len(translated) == 1
    assert translated[0].translated_text == "Bonne nuit"
