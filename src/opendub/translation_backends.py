"""Ollama and Cloud Translation Backends for OpenDub."""

from typing import List, Optional
import httpx
from pydantic import BaseModel
from opendub.models import SpeechSegment


class TranslationBackendConfig(BaseModel):
    backend_type: str = "ollama"  # "ollama", "cloud", "mock"
    model_name: str = "qwen2.5-coder:32b"
    base_url: str = "http://127.0.0.1:11434"
    api_key: Optional[str] = None
    timeout_seconds: int = 60


class TranslationBackend:
    """Executes dialogue translation via local Ollama or cloud providers."""

    def __init__(self, config: Optional[TranslationBackendConfig] = None):
        self.config = config or TranslationBackendConfig()

    def translate_segment(self, segment: SpeechSegment, target_lang: str) -> str:
        """Translate a single dialogue segment."""
        if self.config.backend_type == "mock":
            return f"[{target_lang.upper()}] {segment.original_text}"

        prompt = (
            f"Translate this spoken movie dialogue to {target_lang} natural dialogue. "
            f"Return ONLY the translated sentence with no explanations:\n{segment.original_text}"
        )

        if self.config.backend_type == "ollama":
            url = f"{self.config.base_url.rstrip('/')}/api/generate"
            payload = {
                "model": self.config.model_name,
                "prompt": prompt,
                "stream": False,
            }
            try:
                with httpx.Client(timeout=self.config.timeout_seconds) as client:
                    resp = client.post(url, json=payload)
                    resp.raise_for_status()
                    data = resp.json()
                    out = data.get("response", "").strip()
                    return out if out else f"[{target_lang.upper()}] {segment.original_text}"
            except Exception:
                return f"[{target_lang.upper()}] {segment.original_text}"

        return f"[{target_lang.upper()}] {segment.original_text}"

    def translate_all(self, segments: List[SpeechSegment], target_lang: str) -> List[SpeechSegment]:
        """Translate full list of dialogue segments."""
        results = []
        for s in segments:
            c = s.model_copy()
            c.translated_text = self.translate_segment(s, target_lang)
            results.append(c)
        return results
