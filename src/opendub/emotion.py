"""Emotion and Expressive Tone Preserver for OpenDub."""

from enum import Enum
from typing import Dict
from pydantic import BaseModel


class VocalEmotion(str, Enum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    ANGRY = "angry"
    SAD = "sad"
    WHISPER = "whisper"
    SHOUT = "shout"


class ExpressiveToneConfig(BaseModel):
    emotion: VocalEmotion = VocalEmotion.NEUTRAL
    pitch_shift_semitones: float = 0.0
    energy_boost: float = 1.0


class EmotionAnalyzer:
    """Analyzes source vocal energy and punctuation to preserve dramatic acting emotions."""

    @classmethod
    def detect_emotion_from_text_and_volume(
        cls,
        text: str,
        peak_volume_db: float = -12.0,
    ) -> ExpressiveToneConfig:
        """Infer actor emotion to guide the voice cloning synthesizer."""
        t_clean = text.strip()

        if t_clean.endswith("!!!") or peak_volume_db > -3.0:
            return ExpressiveToneConfig(emotion=VocalEmotion.SHOUT, energy_boost=1.35)
        elif t_clean.endswith("!"):
            return ExpressiveToneConfig(emotion=VocalEmotion.ANGRY, energy_boost=1.15)
        elif "..." in t_clean or peak_volume_db < -35.0:
            return ExpressiveToneConfig(emotion=VocalEmotion.WHISPER, energy_boost=0.75)

        return ExpressiveToneConfig(emotion=VocalEmotion.NEUTRAL, energy_boost=1.0)
