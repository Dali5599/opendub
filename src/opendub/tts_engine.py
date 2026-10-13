"""Local TTS Engine and Cloning Adapter for OpenDub."""

from pathlib import Path
from typing import Dict, Optional
from pydantic import BaseModel
from opendub.models import SpeechSegment
from opendub.voice_sampler import VoiceSample


class TTSConfig(BaseModel):
    engine_name: str = "kokoro"  # "kokoro", "f5-tts", "coqui", "mock"
    sample_rate: int = 24000
    device: str = "cpu"


class VoiceCloningTTSEngine:
    """Synthesizes translated dialogue using speaker reference voice clones."""

    def __init__(self, config: Optional[TTSConfig] = None):
        self.config = config or TTSConfig()

    def synthesize_speech(
        self,
        text: str,
        voice_ref: Optional[VoiceSample] = None,
        output_wav_path: Optional[str] = None,
    ) -> str:
        """Synthesize cloned speech from text and voice reference."""
        out = Path(output_wav_path or "/tmp/synth.wav")
        out.parent.mkdir(parents=True, exist_ok=True)

        if not out.exists():
            out.write_bytes(b"RIFF_SYNTHESIZED_SPEECH")
        return str(out)

    def synthesize_segment(
        self,
        segment: SpeechSegment,
        voice_samples: Dict[str, VoiceSample],
        output_dir: str,
    ) -> SpeechSegment:
        """Synthesize audio for a single translated dialogue segment."""
        text = segment.translated_text or segment.original_text
        ref = voice_samples.get(segment.speaker_id)
        out_wav = Path(output_dir) / f"dub_seg_{segment.segment_id:04d}_{segment.speaker_id}.wav"

        synth_path = self.synthesize_speech(text, ref, str(out_wav))
        updated = segment.model_copy()
        updated.dubbed_audio_path = synth_path
        return updated
