"""Core smoke test for OpenDub package initialization."""

import opendub
from opendub import cli


def test_opendub_version():
    assert opendub.__version__ == "0.1.0"
    assert isinstance(opendub.__version__, str)


def test_cli_app_initialization():
    assert cli.app is not None
    assert cli.app.info.name == "opendub"
