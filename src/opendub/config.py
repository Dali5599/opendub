"""Dubbing Preset and Configuration Manager for OpenDub."""

from pathlib import Path
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore


class DubbingPreset(BaseModel):
    """Presets tailored for specific content types (e.g. Cinema, Anime, Podcast, Tutorial)."""

    name: str
    target_language: str = "fr"
    whisper_model: str = "base"
    translation_model: str = "qwen2.5-coder:32b"
    tts_engine: str = "kokoro"
    ducking_db: float = -12.0
    preserve_sfx: bool = True
    speed_clamp_max: float = 1.50


class OpenDubConfig(BaseModel):
    """Global configuration settings for OpenDub."""

    default_preset: str = "cinema"
    presets: Dict[str, DubbingPreset] = Field(
        default_factory=lambda: {
            "cinema": DubbingPreset(name="cinema", ducking_db=-14.0),
            "podcast": DubbingPreset(name="podcast", ducking_db=-6.0),
            "anime": DubbingPreset(name="anime", ducking_db=-10.0, speed_clamp_max=1.65),
        }
    )
    temp_dir: str = "/tmp/opendub"
    output_dir: str = "output"

    @classmethod
    def load(cls, config_path: Optional[str] = None) -> "OpenDubConfig":
        """Load from opendub.toml or default."""
        if config_path and Path(config_path).is_file():
            try:
                with open(config_path, "rb") as f:
                    data = tomllib.load(f)
                return cls(**data)
            except Exception:
                pass
        return cls()
