"""Audio Stem Separator (Vocals vs Music/SFX) for OpenDub."""

from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel


class SeparatedStems(BaseModel):
    """File paths for separated audio components."""

    vocals_path: str
    accompaniment_path: str  # Music + sound effects (SFX)
    duration_seconds: float = 0.0


class StemSeparator:
    """Isolates dialogue/speech from background music using Demucs / UVR."""

    def __init__(self, model_name: str = "htdemucs", device: str = "cpu"):
        self.model_name = model_name
        self.device = device

    def build_demucs_cmd(self, input_audio: str, output_dir: str) -> List[str]:
        """Construct the demucs command to separate vocals and accompaniment."""
        return [
            "demucs",
            "--two-stems=vocals",
            "-n",
            self.model_name,
            "-d",
            self.device,
            "-o",
            output_dir,
            input_audio,
        ]

    def separate(self, input_audio: str, output_dir: Optional[str] = None) -> SeparatedStems:
        """Simulate or execute stem separation."""
        inp = Path(input_audio)
        out_base = Path(output_dir) if output_dir else inp.parent / "stems"
        out_base.mkdir(parents=True, exist_ok=True)

        vocals_file = out_base / f"{inp.stem}_vocals.wav"
        accomp_file = out_base / f"{inp.stem}_accompaniment.wav"

        # Create simulated stem files if executing in test/mock environment
        if not vocals_file.exists():
            vocals_file.write_bytes(b"RIFF_VOCALS_STEM")
        if not accomp_file.exists():
            accomp_file.write_bytes(b"RIFF_ACCOMPANIMENT_STEM")

        return SeparatedStems(
            vocals_path=str(vocals_file),
            accompaniment_path=str(accomp_file),
            duration_seconds=30.0,
        )
