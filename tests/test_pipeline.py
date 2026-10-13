"""Tests for OpenDub end-to-end orchestrator pipeline."""

import pytest
from opendub.pipeline import DubbingPipeline


def test_dubbing_pipeline_run(tmp_path):
    media_file = tmp_path / "teaser.mp4"
    media_file.write_bytes(b"video_bytes")

    pipeline = DubbingPipeline()
    res = pipeline.process_media(str(media_file), target_lang="es", output_dir=str(tmp_path / "out"))

    assert res.target_language == "es"
    assert "teaser_dubbed_es.wav" in res.dubbed_audio_path
    assert res.timeline.media_file == str(media_file)
