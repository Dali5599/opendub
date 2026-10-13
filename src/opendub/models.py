"""Speech Segment Models and Timeline for OpenDub."""

from typing import List, Optional
from pydantic import BaseModel, Field


class SpeechSegment(BaseModel):
    """Represents a discrete dialogue sentence or phrase in the video."""

    segment_id: int
    speaker_id: str = "SPEAKER_00"
    start_time: float = Field(..., ge=0.0, description="Start timestamp in seconds")
    end_time: float = Field(..., ge=0.0, description="End timestamp in seconds")
    original_text: str = Field(..., description="Transcribed source text")
    translated_text: Optional[str] = Field(None, description="Translated text for dubbing")
    audio_clip_path: Optional[str] = None
    dubbed_audio_path: Optional[str] = None
    confidence: float = 0.95

    @property
    def duration(self) -> float:
        return max(0.0, self.end_time - self.start_time)


class DubbingTimeline(BaseModel):
    """Full chronological timeline of dialogue segments in a media project."""

    media_file: str
    source_language: str = "en"
    target_language: str = "fr"
    total_duration_seconds: float = 0.0
    segments: List[SpeechSegment] = Field(default_factory=list)

    @property
    def speaker_count(self) -> int:
        return len(set(s.speaker_id for s in self.segments))

    def add_segment(self, segment: SpeechSegment) -> None:
        self.segments.append(segment)
        self.segments.sort(key=lambda s: s.start_time)
        if segment.end_time > self.total_duration_seconds:
            self.total_duration_seconds = segment.end_time

    def get_speaker_segments(self, speaker_id: str) -> List[SpeechSegment]:
        return [s for s in self.segments if s.speaker_id == speaker_id]
