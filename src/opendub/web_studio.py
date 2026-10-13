"""Web Studio HTML/JS Dashboard for OpenDub."""

STUDIO_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>OpenDub Studio — Local AI Video Dubbing</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
  <header class="border-b border-slate-800 px-6 py-4 flex items-center justify-between">
    <div class="flex items-center space-x-3">
      <span class="text-2xl">🎙️🎬</span>
      <h1 class="text-xl font-bold bg-gradient-to-r from-cyan-400 to-violet-500 bg-clip-text text-transparent">
        OpenDub Studio
      </h1>
      <span class="text-xs bg-cyan-950 border border-cyan-800 text-cyan-400 px-2 py-0.5 rounded-full font-mono">
        100% Offline Local
      </span>
    </div>
    <div class="flex items-center space-x-4 text-sm text-slate-400">
      <span>Models: Whisper • Demucs • Kokoro • Ollama</span>
    </div>
  </header>

  <main class="max-w-6xl mx-auto px-6 py-8 grid grid-cols-1 md:grid-cols-3 gap-8">
    <div class="md:col-span-1 bg-slate-900 border border-slate-800 rounded-xl p-6">
      <h2 class="text-lg font-semibold mb-4 text-cyan-400">1. Media Source</h2>
      <div class="border-2 border-dashed border-slate-700 rounded-lg p-6 text-center cursor-pointer hover:border-cyan-500 transition">
        <p class="text-sm text-slate-400">Drop movie / video (MP4, MKV)</p>
        <span class="text-xs text-slate-500 mt-2 block">or paste local path</span>
      </div>

      <h2 class="text-lg font-semibold mt-6 mb-4 text-cyan-400">2. Target Language</h2>
      <select id="targetLang" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200">
        <option value="fr">French (Français)</option>
        <option value="es">Spanish (Español)</option>
        <option value="de">German (Deutsch)</option>
        <option value="ar">Arabic (العربية)</option>
        <option value="ja">Japanese (日本語)</option>
        <option value="it">Italian (Italiano)</option>
      </select>

      <button id="startBtn" class="w-full mt-6 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-medium py-3 rounded-lg shadow-lg shadow-cyan-950 transition">
        🚀 Start Local Dubbing
      </button>
    </div>

    <div class="md:col-span-2 bg-slate-900 border border-slate-800 rounded-xl p-6 flex flex-col justify-between">
      <div>
        <h2 class="text-lg font-semibold mb-4 text-cyan-400">3. Live Studio Timeline</h2>
        <div class="space-y-3 font-mono text-xs">
          <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex justify-between">
            <span class="text-slate-400">Track 01: Dialogue Stem</span>
            <span class="text-emerald-400">Ready</span>
          </div>
          <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex justify-between">
            <span class="text-slate-400">Track 02: Music & SFX</span>
            <span class="text-emerald-400">Preserved (Ducking Active)</span>
          </div>
          <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex justify-between">
            <span class="text-slate-400">Voice Cloner</span>
            <span class="text-cyan-400">Kokoro / F5-TTS Ready</span>
          </div>
        </div>
      </div>

      <div class="mt-8 border-t border-slate-800 pt-4 flex justify-between items-center text-sm text-slate-500">
        <span>OpenDub v0.1.0 • Built with Requin</span>
        <a href="https://github.com/Dali5599/opendub" class="text-cyan-400 hover:underline">GitHub Repository</a>
      </div>
    </div>
  </main>
</body>
</html>
"""


class WebStudioDashboard:
    """Serves the interactive creator studio dashboard."""

    @staticmethod
    def get_html() -> str:
        return STUDIO_HTML
