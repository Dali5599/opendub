"""Tests for OpenDub emotion and expressive tone preserver."""

import pytest
from opendub.emotion import EmotionAnalyzer, VocalEmotion


def test_detect_shout():
    tone = EmotionAnalyzer.detect_emotion_from_text_and_volume("Run for your lives!!!", peak_volume_db=-1.0)
    assert tone.emotion == VocalEmotion.SHOUT
    assert tone.energy_boost > 1.2


def test_detect_whisper():
    tone = EmotionAnalyzer.detect_emotion_from_text_and_volume("Be very quiet...", peak_volume_db=-40.0)
    assert tone.emotion == VocalEmotion.WHISPER
    assert tone.energy_boost < 0.9


def test_detect_neutral():
    tone = EmotionAnalyzer.detect_emotion_from_text_and_volume("The meeting starts at noon.", peak_volume_db=-15.0)
    assert tone.emotion == VocalEmotion.NEUTRAL
    assert tone.energy_boost == 1.0
