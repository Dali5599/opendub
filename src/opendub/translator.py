"""Multi-Language Translator with Token Budgeting for OpenDub."""

from typing import List, Optional
from opendub.models import SpeechSegment


class DialogueTranslator:
    """Translates dialogue segments while preserving movie subtext and character voice style."""

    LANGUAGE_NAMES = {
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ar": "Arabic",
        "ja": "Japanese",
        "zh": "Chinese",
        "ru": "Russian",
        "en": "English",
    }

    def __init__(self, target_language: str = "fr"):
        self.target_language = target_language.lower()

    def build_translation_prompt(self, segments: List[SpeechSegment]) -> str:
        """Create structured prompt for LLM dialogue dubbing translation."""
        target_name = self.LANGUAGE_NAMES.get(self.target_language, self.target_language.upper())
        lines = [
            f"You are a master movie dialogue dubbing translator.",
            f"Translate the following spoken film dialogue from its source language into natural, idiomatic {target_name}.",
            f"IMPORTANT: Match the syllable length and pacing closely for video lip-synchronization.",
            f"",
            f"Format response as line-by-line translation:",
        ]
        for seg in segments:
            lines.append(f"[{seg.segment_id}] ({seg.speaker_id}): {seg.original_text}")
        return "\n".join(lines)

    def apply_translations(self, segments: List[SpeechSegment], translated_texts: List[str]) -> List[SpeechSegment]:
        """Apply translated text back to segments."""
        if len(segments) != len(translated_texts):
            raise ValueError("Segments count and translated text count mismatch")

        updated = []
        for s, tr in zip(segments, translated_texts):
            c = s.model_copy()
            c.translated_text = tr.strip()
            updated.append(c)
        return updated
