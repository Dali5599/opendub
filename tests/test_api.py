"""Tests for OpenDub REST API and task dispatcher."""

import pytest
from opendub.api import DubbingApiDispatcher, DubbingRequest


def test_submit_job():
    dispatcher = DubbingApiDispatcher()
    req = DubbingRequest(video_path="input.mp4", target_lang="es")
    ticket = dispatcher.submit_job(req)
    assert ticket.startswith("ticket_")
    assert dispatcher.active_jobs[ticket] == "PENDING"


def test_run_synchronous_job(tmp_path):
    video = tmp_path / "vid.mp4"
    video.write_bytes(b"data")

    dispatcher = DubbingApiDispatcher()
    req = DubbingRequest(video_path=str(video), target_lang="fr")
    res = dispatcher.run_synchronous_job(req)
    assert res.target_language == "fr"
    assert "vid_dubbed_fr.wav" in res.dubbed_audio_path
