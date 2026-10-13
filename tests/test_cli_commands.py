"""Tests for OpenDub complete CLI commands."""

from typer.testing import CliRunner
import pytest
from opendub.cli import app

runner = CliRunner()


def test_cli_version():
    res = runner.invoke(app, ["version"])
    assert res.exit_code == 0
    assert "OpenDub" in res.stdout


def test_cli_presets():
    res = runner.invoke(app, ["presets"])
    assert res.exit_code == 0
    assert "Available Presets:" in res.stdout
    assert "cinema" in res.stdout


def test_cli_transcribe_and_run(tmp_path):
    media = tmp_path / "clip.mp4"
    media.write_bytes(b"data")
    out_srt = tmp_path / "out.srt"

    res_tr = runner.invoke(app, ["transcribe", str(media), "--output", str(out_srt)])
    assert res_tr.exit_code == 0
    assert out_srt.is_file()

    res_run = runner.invoke(app, ["run", str(media), "--target-lang", "fr"])
    assert res_run.exit_code == 0
    assert "Dubbing complete" in res_run.stdout
