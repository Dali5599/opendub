"""Speaker Diarization and Voice Clustering for OpenDub."""

from typing import Dict, List, Set
from opendub.models import SpeechSegment


class SpeakerDiarizationEngine:
    """Clusters voice embeddings and assigns consistent speaker tags across full movies."""

    def __init__(self, min_speakers: int = 1, max_speakers: int = 10):
        self.min_speakers = min_speakers
        self.max_speakers = max_speakers

    def assign_speakers_by_cluster(
        self,
        segments: List[SpeechSegment],
        cluster_labels: List[int],
    ) -> List[SpeechSegment]:
        """Map clustering results to standardized SPEAKER_XX identifiers."""
        if len(segments) != len(cluster_labels):
            raise ValueError("Segments count and cluster labels count must match")

        updated = []
        for seg, label in zip(segments, cluster_labels):
            seg_copy = seg.model_copy()
            seg_copy.speaker_id = f"SPEAKER_{label:02d}"
            updated.append(seg_copy)
        return updated

    def detect_distinct_speakers(self, segments: List[SpeechSegment]) -> Set[str]:
        """Get set of all unique speakers identified in timeline."""
        return set(s.speaker_id for s in segments)

    def group_dialogue_by_speaker(self, segments: List[SpeechSegment]) -> Dict[str, List[SpeechSegment]]:
        """Group dialogue sentences by speaker for voice cloning extraction."""
        grouped: Dict[str, List[SpeechSegment]] = {}
        for s in segments:
            grouped.setdefault(s.speaker_id, []).append(s)
        return grouped
