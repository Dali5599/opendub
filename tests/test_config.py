"""Tests for OpenDub preset and configuration manager."""

import pytest
from opendub.config import DubbingPreset, OpenDubConfig


def test_default_config():
    cfg = OpenDubConfig.load()
    assert "cinema" in cfg.presets
    assert "podcast" in cfg.presets
    assert cfg.presets["cinema"].ducking_db == -14.0


def test_custom_preset():
    preset = DubbingPreset(name="documentary", ducking_db=-18.0)
    assert preset.name == "documentary"
    assert preset.preserve_sfx is True
