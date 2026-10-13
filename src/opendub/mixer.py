"""Audio Mixer and Ducking Engine for OpenDub."""

from typing import List


class AudioMixer:
    """Blends dubbed dialogue with isolated background music and sound effects (SFX) with sidechain ducking."""

    @classmethod
    def build_ducking_filter_graph(
        cls,
        speech_input_idx: int = 0,
        music_input_idx: int = 1,
        ducking_attenuation_db: float = -12.0,
    ) -> str:
        """Generate ffmpeg sidechaincompress / volume ducking filter so music ducks under speech."""
        return (
            f"[{music_input_idx}:a][{speech_input_idx}:a]"
            f"sidechaincompress=threshold=0.1:ratio=4:attack=20:release=300[ducked_bg];"
            f"[{speech_input_idx}:a][ducked_bg]amix=inputs=2:duration=first:dropout_transition=2"
        )

    @classmethod
    def build_full_mix_cmd(
        cls,
        dubbed_vocals_wav: str,
        accompaniment_wav: str,
        output_master_audio: str,
    ) -> List[str]:
        """Generate ffmpeg command to blend newly cloned voices with pristine original music & effects."""
        filter_graph = cls.build_ducking_filter_graph(speech_input_idx=0, music_input_idx=1)
        return [
            "ffmpeg",
            "-y",
            "-i",
            dubbed_vocals_wav,
            "-i",
            accompaniment_wav,
            "-filter_complex",
            filter_graph,
            output_master_audio,
        ]
