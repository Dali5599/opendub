"""Tests for OpenDub dialogue timing adjuster."""

import pytest
from opendub.timing import DialogueTimingAdjuster


def test_estimate_syllables():
    assert DialogueTimingAdjuster.estimate_syllables("hello") == 2
    assert DialogueTimingAdjuster.estimate_syllables("internationalization") >= 6
    assert DialogueTimingAdjuster.estimate_syllables("") == 0


def test_evaluate_timing_optimal():
    factor, status = DialogueTimingAdjuster.evaluate_timing(
        source_text="Good morning",
        translated_text="Bonjour",
        time_slot_seconds=2.0,
    )
    assert factor == 1.0
    assert status == "OPTIMAL_PACING"


def test_evaluate_timing_overflow():
    factor, status = DialogueTimingAdjuster.evaluate_timing(
        source_text="Yes",
        translated_text="Absolument et sans aucun doute possible mon cher ami",
        time_slot_seconds=1.0,
    )
    assert factor > 1.0
    assert "OVERFLOW" in status
