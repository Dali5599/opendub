# OpenDub Roadmap & Production Pipeline

## Phase 1 : Core Media & Audio Demuxing Engine
- [x] 01. Implement Media Extractor and Track Demuxer in src/opendub/media.py
- [x] 02. Implement Audio Stem Separator (Vocals vs Music/SFX) in src/opendub/stems.py
- [x] 03. Implement Speech Segment Models and Timeline in src/opendub/models.py
- [x] 04. Implement Subtitle Generator (SRT & VTT) in src/opendub/subtitles.py
- [x] 05. Implement Audio Time Stretcher and Pitch Preserver in src/opendub/timestretch.py

## Phase 2 : Transcription, Diarization & Translation Engine
- [x] 06. Implement Local Speech-to-Text Whisper Client in src/opendub/transcription.py
- [x] 07. Implement Speaker Diarization and Voice Clustering in src/opendub/diarization.py
- [x] 08. Implement Multi-Language Translator with Token Budgeting in src/opendub/translator.py
- [x] 09. Implement Dialogue Timing Adjuster and Syllable Counter in src/opendub/timing.py
- [x] 10. Implement Ollama & Cloud Translation Backends in src/opendub/translation_backends.py

## Phase 3 : Voice Cloning & Text-to-Speech Synthesis
- [ ] 11. Implement Voice Reference Sampler and Audio Normalizer in src/opendub/voice_sampler.py
- [ ] 12. Implement Local TTS Engine and Cloning Adapter in src/opendub/tts_engine.py
- [ ] 13. Implement Emotion and Expressive Tone Preserver in src/opendub/emotion.py
- [ ] 14. Implement Audio Mixer and Ducking Engine in src/opendub/mixer.py
- [ ] 15. Implement End-to-End Dubbing Orchestrator Pipeline in src/opendub/pipeline.py

## Phase 4 : Video Remuxing, Web Studio UI & CLI
- [ ] 16. Implement Video Remuxer with Lip-Sync Drift Compensation in src/opendub/remuxer.py
- [ ] 17. Implement Dubbing Preset and Configuration Manager in src/opendub/config.py
- [ ] 18. Implement Web Studio HTML/JS Dashboard in src/opendub/web_studio.py
- [ ] 19. Implement REST and Background Task Dispatcher in src/opendub/api.py
- [ ] 20. Implement Complete CLI Commands (run, transcribe, web, presets) in src/opendub/cli.py
