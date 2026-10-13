"""Dialogue Timing Adjuster and Syllable Counter for OpenDub."""

import re
from typing import Tuple


class DialogueTimingAdjuster:
    """Analyzes syllable count and spoken duration to prevent audio overflow."""

    VOWEL_RE = re.compile(r"[aeiouyàâäéèêëîïôöùûü]+", re.IGNORECASE)

    @classmethod
    def estimate_syllables(cls, text: str) -> int:
        """Estimate spoken syllable count based on vowel groups."""
        if not text:
            return 0
        words = text.strip().split()
        total = 0
        for w in words:
            vowels = len(cls.VOWEL_RE.findall(w))
            total += max(1, vowels)
        return total

    @classmethod
    def evaluate_timing(
        cls,
        source_text: str,
        translated_text: str,
        time_slot_seconds: float,
    ) -> Tuple[float, str]:
        """Estimate speech rate and recommend speed adjustment or text shortening."""
        src_syl = cls.estimate_syllables(source_text)
        tr_syl = cls.estimate_syllables(translated_text)

        # Average speaking speed: ~4 syllables per second
        syllables_per_second = tr_syl / max(0.5, time_slot_seconds)

        if syllables_per_second > 6.0:
            status = "CRITICAL_OVERFLOW: Translation too long for video slot"
            factor = min(1.5, syllables_per_second / 4.0)
        elif syllables_per_second > 4.5:
            status = "SLIGHT_OVERFLOW: Speed up recommended"
            factor = syllables_per_second / 4.0
        else:
            status = "OPTIMAL_PACING"
            factor = 1.0

        return round(factor, 2), status
