"""Audio Time Stretcher and Pitch Preserver for OpenDub."""

from typing import List, Tuple


class AudioTimeStretcher:
    """Adjusts speech tempo/speed to match original video duration without altering vocal pitch."""

    MAX_SPEED_RATIO = 1.60  # Maximum acceleration before speech becomes unnatural
    MIN_SPEED_RATIO = 0.70  # Maximum deceleration

    @classmethod
    def calculate_speed_factor(cls, original_duration: float, new_duration: float) -> Tuple[float, bool]:
        """Calculate required tempo ratio (new_duration / original_duration)."""
        if original_duration <= 0 or new_duration <= 0:
            return 1.0, False

        # If new audio is longer than slot, speed it up (ratio > 1)
        ratio = new_duration / original_duration
        is_clamped = False

        if ratio > cls.MAX_SPEED_RATIO:
            ratio = cls.MAX_SPEED_RATIO
            is_clamped = True
        elif ratio < cls.MIN_SPEED_RATIO:
            ratio = cls.MIN_SPEED_RATIO
            is_clamped = True

        return round(ratio, 3), is_clamped

    @classmethod
    def build_rubberband_filter(cls, speed_factor: float) -> str:
        """Build ffmpeg audio filter graph using rubberband or atempo."""
        if abs(speed_factor - 1.0) < 0.02:
            return "anull"
        return f"atempo={speed_factor:.3f}"

    @classmethod
    def build_ffmpeg_timestretch_cmd(
        cls,
        input_audio: str,
        output_audio: str,
        speed_factor: float,
    ) -> List[str]:
        """Generate ffmpeg command to time-stretch audio while keeping pitch unchanged."""
        af_filter = cls.build_rubberband_filter(speed_factor)
        return [
            "ffmpeg",
            "-y",
            "-i",
            input_audio,
            "-filter:a",
            af_filter,
            "-vn",
            output_audio,
        ]
