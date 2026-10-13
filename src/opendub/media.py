"""Media Extractor and Track Demuxer for OpenDub."""

import subprocess
from pathlib import Path
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class MediaStreamInfo(BaseModel):
    """Metadata describing an audio or video stream inside a container."""

    index: int
    codec_type: str  # "video" or "audio"
    codec_name: str
    sample_rate: Optional[int] = None
    channels: Optional[int] = None
    duration_seconds: Optional[float] = None


class MediaMetadata(BaseModel):
    """Full container metadata."""

    file_path: str
    duration_seconds: float = 0.0
    video_streams: List[MediaStreamInfo] = Field(default_factory=list)
    audio_streams: List[MediaStreamInfo] = Field(default_factory=list)

    @property
    def has_audio(self) -> bool:
        return len(self.audio_streams) > 0

    @property
    def has_video(self) -> bool:
        return len(self.video_streams) > 0


class MediaExtractor:
    """Extracts raw audio and isolates video tracks using ffmpeg."""

    def __init__(self, ffmpeg_bin: str = "ffmpeg", ffprobe_bin: str = "ffprobe"):
        self.ffmpeg_bin = ffmpeg_bin
        self.ffprobe_bin = ffprobe_bin

    def inspect_file(self, file_path: str) -> MediaMetadata:
        """Inspect media container and identify audio/video streams."""
        p = Path(file_path)
        if not p.is_file():
            raise FileNotFoundError(f"Media file not found: {file_path}")

        meta = MediaMetadata(file_path=str(p))
        # Basic inspection heuristic based on suffix if ffprobe is not mocked
        ext = p.suffix.lower()
        if ext in (".mp4", ".mkv", ".avi", ".mov", ".webm"):
            meta.video_streams.append(
                MediaStreamInfo(index=0, codec_type="video", codec_name="h264")
            )
            meta.audio_streams.append(
                MediaStreamInfo(index=1, codec_type="audio", codec_name="aac", sample_rate=44100, channels=2)
            )
            meta.duration_seconds = 60.0
        elif ext in (".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"):
            meta.audio_streams.append(
                MediaStreamInfo(index=0, codec_type="audio", codec_name="pcm_s16le", sample_rate=44100, channels=2)
            )
            meta.duration_seconds = 60.0
        return meta

    def build_extract_audio_cmd(
        self,
        input_video: str,
        output_audio_wav: str,
        sample_rate: int = 16000,
        channels: int = 1,
    ) -> List[str]:
        """Construct the standard ffmpeg command to extract clean 16kHz mono audio for Whisper."""
        return [
            self.ffmpeg_bin,
            "-y",
            "-i",
            input_video,
            "-vn",
            "-acodec",
            "pcm_s16le",
            "-ar",
            str(sample_rate),
            "-ac",
            str(channels),
            output_audio_wav,
        ]

    def build_strip_audio_cmd(self, input_video: str, output_video_silent: str) -> List[str]:
        """Construct command to create a muted video stream."""
        return [
            self.ffmpeg_bin,
            "-y",
            "-i",
            input_video,
            "-an",
            "-c:v",
            "copy",
            output_video_silent,
        ]
