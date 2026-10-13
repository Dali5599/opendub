# 🎙️🎬 OpenDub — Local AI Video Dubbing & Voice Cloning Studio

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests Passing](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![Offline First](https://img.shields.io/badge/offline--first-100%25-orange.svg)]()

> **The open-source, fully-local alternative to ElevenLabs Dubbing Studio & HeyGen.**  
> Translate any movie, YouTube video, podcast, or reel into **50+ languages** while **cloning each speaker's real voice** and preserving the background music and sound effects.

---

## ✨ Features

- 🎭 **Zero Cloud Lock-in / 100% Local**: Runs completely offline using local models (Whisper, Demucs, Kokoro/F5-TTS, Ollama). Zero monthly subscription fees, zero private data leaks.
- 🎼 **Vocal & Background Separation**: Isolates actor voices from background music and sound effects (SFX) using Demucs/UVR. Explosions, footsteps, and score stay identical.
- 🗣️ **Instant Voice Cloning**: Retains the authentic emotion, timbre, tone, and pacing of the original actor in the target language.
- ⏱️ **Timestamp-Accurate Synchronization**: Automatic subtitle alignment and speech time-stretching to match original video lip movements and scene cuts.
- 🌐 **50+ Languages Supported**: Translate English, Spanish, French, Arabic, Japanese, German, Hindi, Mandarin, and more.
- 🖥️ **CLI & Web Studio UI**: Available as a fast command-line tool for batch automation or an intuitive Web Studio for creators.

---

## ⚡ Quick Start

### Installation

```bash
git clone https://github.com/Dali5599/opendub.git
cd opendub
pip install -e .
```

### Dub a video in 1 command

```bash
# Dub an English video to French with voice cloning
opendub run input.mp4 --target-lang fr --output dubbed_fr.mp4

# Dub with local Ollama translation
opendub run input.mp4 --target-lang es --llm ollama --model qwen2.5-coder:32b

# Extract subtitles with timestamps (SRT / VTT)
opendub transcribe input.mp4 --format srt --output subtitles.srt

# Launch the Web Studio UI
opendub web --port 7860
```

---

## 🗺️ Roadmap & Multi-Phase Architecture

See [`ROADMAP.md`](ROADMAP.md) for live progress across all 4 production phases.

---

## 📜 License

MIT License © 2026 Dali5599 & OpenDub.
