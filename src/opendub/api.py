"""REST and Background Task Dispatcher for OpenDub."""

from typing import Dict
from pydantic import BaseModel
from opendub.pipeline import DubbingJobResult, DubbingPipeline


class DubbingRequest(BaseModel):
    video_path: str
    target_lang: str = "fr"
    preset: str = "cinema"


class DubbingApiDispatcher:
    """Handles async job scheduling and tracking for OpenDub."""

    def __init__(self, pipeline: DubbingPipeline = None):
        self.pipeline = pipeline or DubbingPipeline()
        self.active_jobs: Dict[str, str] = {}

    def submit_job(self, request: DubbingRequest) -> str:
        """Enqueue job and return unique ticket ID."""
        ticket = f"ticket_{abs(hash(request.video_path + request.target_lang)) % 100000:05d}"
        self.active_jobs[ticket] = "PENDING"
        return ticket

    def run_synchronous_job(self, request: DubbingRequest) -> DubbingJobResult:
        """Run job immediately."""
        return self.pipeline.process_media(
            media_path=request.video_path,
            target_lang=request.target_lang,
        )
