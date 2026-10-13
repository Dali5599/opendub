"""Subtitle Generator (SRT & VTT) for OpenDub."""

from typing import List
from opendub.models import SpeechSegment


class SubtitleGenerator:
    """Formats dialogue segments into SRT and WebVTT standard subtitle formats."""

    @staticmethod
    def _format_timestamp(seconds: float, vtt: bool = False) -> str:
        """Format seconds into HH:MM:SS,mmm (SRT) or HH:MM:SS.mmm (VTT)."""
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int(round((seconds - int(seconds)) * 1000))
        sep = "." if vtt else ","
        return f"{hrs:02d}:{mins:02d}:{secs:02d}{sep}{millis:03d}"

    @classmethod
    def generate_srt(cls, segments: List[SpeechSegment], use_translation: bool = False) -> str:
        """Generate SRT format subtitles."""
        blocks = []
        for idx, seg in enumerate(segments, start=1):
            t_start = cls._format_timestamp(seg.start_time, vtt=False)
            t_end = cls._format_timestamp(seg.end_time, vtt=False)
            text = (seg.translated_text if use_translation and seg.translated_text else seg.original_text).strip()
            blocks.append(f"{idx}\n{t_start} --> {t_end}\n{text}\n")
        return "\n".join(blocks)

    @classmethod
    def generate_vtt(cls, segments: List[SpeechSegment], use_translation: bool = False) -> str:
        """Generate WebVTT format subtitles."""
        lines = ["WEBVTT\n"]
        for idx, seg in enumerate(segments, start=1):
            t_start = cls._format_timestamp(seg.start_time, vtt=True)
            t_end = cls._format_timestamp(seg.end_time, vtt=True)
            text = (seg.translated_text if use_translation and seg.translated_text else seg.original_text).strip()
            lines.append(f"{t_start} --> {t_end}\n{text}\n")
        return "\n".join(lines)
