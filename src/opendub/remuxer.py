"""Video Remuxer with Lip-Sync Drift Compensation for OpenDub."""

from typing import List, Optional


class VideoRemuxer:
    """Combines original video stream with newly dubbed multi-track master audio."""

    def __init__(self, ffmpeg_bin: str = "ffmpeg"):
        self.ffmpeg_bin = ffmpeg_bin

    def build_remux_cmd(
        self,
        input_video: str,
        dubbed_audio: str,
        output_video: str,
        subtitles_srt: Optional[str] = None,
        audio_delay_ms: int = 0,
    ) -> List[str]:
        """Generate ffmpeg remux command with precise audio sync offset."""
        cmd = [
            self.ffmpeg_bin,
            "-y",
            "-i",
            input_video,
            "-i",
            dubbed_audio,
        ]

        if audio_delay_ms != 0:
            # Add audio delay offset in ms
            delay_sec = audio_delay_ms / 1000.0
            cmd.extend(["-itsoffset", f"{delay_sec:.3f}"])

        cmd.extend([
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
        ])

        if subtitles_srt:
            cmd.extend([
                "-i",
                subtitles_srt,
                "-c:s",
                "mov_text",
                "-map",
                "2:s:0",
            ])

        cmd.append(output_video)
        return cmd
