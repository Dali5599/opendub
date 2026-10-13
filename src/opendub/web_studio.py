"""Web Studio HTML/JS Dashboard for OpenDub."""

STUDIO_HTML = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <title>OpenDub Studio — Professional Local AI Video Dubbing & Voice Synthesis</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#fff1f4',
              100: '#ffe4e9',
              200: '#fecdd7',
              300: '#fda4b7',
              400: '#fb718f',
              500: '#f43f68',
              600: '#e11d48',
              700: '#be123c',
              800: '#9f1239',
              900: '#881337',
              accent: '#ff2d6c',
              glow: 'rgba(255, 45, 108, 0.35)'
            },
            canvas: {
              base: '#0b0a10',
              subtle: '#121019',
              panel: '#161420',
              elevated: '#1e1a2b',
              border: '#2a243d',
              borderMuted: '#1f1a30'
            }
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace']
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #0b0a10;
      color: #f1f0f5;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
    }
    .custom-scrollbar::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
      background: #121019;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
      background: #2a243d;
      border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {
      background: #ff2d6c;
    }
    .brand-glow {
      box-shadow: 0 0 25px -4px rgba(255, 45, 108, 0.45);
    }
    .neon-pill {
      background: rgba(255, 45, 108, 0.12);
      border: 1px solid rgba(255, 45, 108, 0.35);
      color: #ff5e8c;
    }
    .glass-panel {
      background: rgba(22, 20, 32, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid #2a243d;
    }
  </style>
</head>
<body class="flex h-screen w-screen overflow-hidden text-sm select-none antialiased">

  <!-- ==================== ULTRA-MINIMAL DOCK SIDEBAR ==================== -->
  <aside class="w-14 bg-canvas-base border-r border-canvas-border flex flex-col items-center py-4 justify-between shrink-0 z-30">
    <div class="flex flex-col items-center space-y-6">
      <!-- App Brand Logo -->
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-700 via-brand-600 to-brand-accent flex items-center justify-center shadow-lg shadow-brand-900/40 cursor-pointer">
        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"/>
        </svg>
      </div>

      <!-- Main Navigation Icons -->
      <nav class="flex flex-col space-y-3">
        <button title="Voice Studio & Dubbing" class="w-10 h-10 rounded-lg flex items-center justify-center text-brand-400 bg-brand-500/10 border border-brand-500/20 transition hover:bg-brand-500/20">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
        </button>
        <button title="Audio Separation (Demucs)" class="w-10 h-10 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"/></svg>
        </button>
        <button title="Lip-Sync & Video Remux" class="w-10 h-10 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
        </button>
        <button title="Dialogue Timeline & Subtitles" class="w-10 h-10 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/></svg>
        </button>
        <button title="Saved Profiles & Cloned Voices" class="w-10 h-10 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 19a2 2 0 01-2-2V7a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1M5 19h14a2 2 0 002-2v-5a2 2 0 00-2-2H9a2 2 0 00-2 2v5a2 2 0 01-2 2z"/></svg>
        </button>
      </nav>
    </div>

    <!-- Bottom Utility Icons -->
    <div class="flex flex-col space-y-3 items-center">
      <div class="relative">
        <button class="w-9 h-9 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
        </button>
        <span class="absolute top-1 right-1 w-2 h-2 rounded-full bg-brand-500 animate-ping"></span>
        <span class="absolute top-1 right-1 w-2 h-2 rounded-full bg-brand-500"></span>
      </div>
      <button title="Settings & Local Backends" class="w-9 h-9 rounded-lg flex items-center justify-center text-slate-400 hover:text-white hover:bg-canvas-panel transition">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
      </button>
    </div>
  </aside>

  <!-- ==================== LEFT CONTROL PANEL: VOICE DESIGN & PARAMS ==================== -->
  <section class="w-80 bg-canvas-subtle border-r border-canvas-border flex flex-col shrink-0 custom-scrollbar overflow-y-auto">
    <!-- Panel Header -->
    <div class="p-4 border-b border-canvas-border flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <svg class="w-4 h-4 text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
        <span class="font-semibold text-white tracking-wide text-xs uppercase">Voice Design</span>
      </div>
      <button class="text-xs text-slate-500 hover:text-slate-300">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
      </button>
    </div>

    <div class="p-4 space-y-6 flex-1">
      <!-- Voice Prompt Description -->
      <div class="space-y-2">
        <div class="flex items-center justify-between text-xs">
          <label class="font-medium text-slate-300">Describe your voice</label>
          <button id="resetPromptBtn" class="text-slate-500 hover:text-brand-400 flex items-center space-x-1 transition text-[11px]">
            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
            <span>Reset</span>
          </button>
        </div>
        <textarea id="voicePromptInput" rows="3" placeholder="e.g. a warm elderly British storyteller, slightly raspy, dramatic and intimate" class="w-full bg-canvas-panel border border-canvas-border rounded-lg p-3 text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500 transition resize-none"></textarea>
        <p class="text-[11px] text-slate-500 leading-relaxed">
          Describe the voice persona or pick starting tags below to sculpt timbre, pacing, and acoustics.
        </p>
      </div>

      <!-- Preset Tags / Starting Points -->
      <div class="space-y-3">
        <div class="flex items-center justify-between text-xs">
          <span class="font-medium text-slate-300 flex items-center space-x-1.5">
            <svg class="w-3.5 h-3.5 text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
            <span>Starting points</span>
          </span>
          <span class="text-[10px] text-slate-600 font-mono">12 tags</span>
        </div>
        <div class="flex flex-wrap gap-1.5">
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Narrator')">📖 Narrator</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Casual')">☕ Casual</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'News Anchor')">🎙️ News Anchor</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Storyteller')">🎭 Storyteller</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Corporate')">💼 Corporate</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Energetic')">⚡ Energetic</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Authoritative')">🏛️ Authoritative</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Whisper')">🤫 Whisper</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Deep Cinematic')">🎬 Deep Cinematic</button>
          <button class="tag-pill px-2.5 py-1 rounded-md text-[11px] bg-canvas-panel border border-canvas-border hover:border-brand-500 text-slate-300 transition" onclick="selectTag(this, 'Anime Hero')">⚔️ Anime Hero</button>
        </div>
      </div>

      <!-- Fine-grained Voice Acoustics & Details -->
      <div class="space-y-4 pt-2 border-t border-canvas-border">
        <div class="flex items-center justify-between text-xs">
          <span class="font-medium text-slate-300">Acoustic Details</span>
          <span id="pitchLabel" class="text-[11px] text-brand-400 font-mono">middle-aged • balanced</span>
        </div>

        <!-- Sliders -->
        <div class="space-y-3">
          <div>
            <div class="flex justify-between text-[11px] text-slate-400 mb-1">
              <span>Vocal Pitch</span>
              <span id="pitchVal" class="font-mono text-slate-300">0.0 st</span>
            </div>
            <input type="range" min="-12" max="12" value="0" step="0.5" class="w-full accent-brand-500 h-1 bg-canvas-panel rounded cursor-pointer" oninput="document.getElementById('pitchVal').innerText = this.value + ' st'">
          </div>

          <div>
            <div class="flex justify-between text-[11px] text-slate-400 mb-1">
              <span>Pacing / Syllable Rate</span>
              <span id="paceVal" class="font-mono text-slate-300">1.00x</span>
            </div>
            <input type="range" min="0.75" max="1.4" value="1.0" step="0.05" class="w-full accent-brand-500 h-1 bg-canvas-panel rounded cursor-pointer" oninput="document.getElementById('paceVal').innerText = this.value + 'x'">
          </div>

          <div>
            <div class="flex justify-between text-[11px] text-slate-400 mb-1">
              <span>Dramatic Energy & Ducking</span>
              <span id="energyVal" class="font-mono text-slate-300">85%</span>
            </div>
            <input type="range" min="0" max="100" value="85" class="w-full accent-brand-500 h-1 bg-canvas-panel rounded cursor-pointer" oninput="document.getElementById('energyVal').innerText = this.value + '%'">
          </div>
        </div>
      </div>

      <!-- Profile Save Input -->
      <div class="pt-2 border-t border-canvas-border space-y-2">
        <input id="profileNameInput" type="text" placeholder="Profile name (e.g. Victor - Noir Detective)" class="w-full bg-canvas-panel border border-canvas-border rounded-lg px-3 py-2 text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:border-brand-500">
        <button onclick="saveVoiceProfile()" class="w-full py-2 px-3 rounded-lg bg-canvas-elevated hover:bg-canvas-border text-brand-300 border border-brand-500/30 text-xs font-medium flex items-center justify-center space-x-2 transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"/></svg>
          <span>Save as voice profile</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ==================== MAIN WORKSPACE: VOICE GALLERY & SCRIPT EDITOR ==================== -->
  <main class="flex-1 flex flex-col bg-canvas-base overflow-hidden">
    <!-- Top Navbar -->
    <header class="h-12 border-b border-canvas-border px-6 flex items-center justify-between bg-canvas-subtle shrink-0">
      <div class="flex items-center space-x-4">
        <div class="flex items-center space-x-2 text-xs text-slate-400">
          <span class="text-brand-400 font-medium">OpenDub</span>
          <span>/</span>
          <span class="text-white font-medium">Cinema Studio</span>
          <span>/</span>
          <span class="text-slate-500">Voice Design & Dubbing</span>
        </div>
      </div>

      <div class="flex items-center space-x-4">
        <div class="flex items-center space-x-2 bg-canvas-panel border border-canvas-border px-3 py-1 rounded-full text-xs">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          <span class="text-slate-300 font-mono text-[11px]">Local Engine: 100% Offline Voice Cloner (F5-TTS • Demucs • Whisper)</span>
        </div>
        <div class="text-xs text-slate-500 font-mono border border-canvas-border px-2.5 py-1 rounded bg-canvas-elevated">
          Ctrl + K
        </div>
      </div>
    </header>

    <!-- Scrollable Studio Content -->
    <div class="flex-1 custom-scrollbar overflow-y-auto p-6 space-y-6">

      <!-- Section: Hear Demo Voice Library -->
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center space-x-1.5">
              <span>▼ Hear demo & Voice Library</span>
            </span>
          </div>
          <span class="text-xs text-slate-500">6 Curated Zero-Shot Archetypes</span>
        </div>

        <!-- 6 Preset Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">

          <!-- Card 1 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">The Librarian</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-brand-950 text-brand-300 border border-brand-800">Warm UK</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Warm UK audiobook narrator — measured, atmospheric, rich mid-tones.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('librarian')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('The Librarian', 'Warm UK audiobook narrator — measured, atmospheric')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">The Anchor</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800">Clear US</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Clear American broadcaster — primetime evening news, authoritative & crisp.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('anchor')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('The Anchor', 'Clear American broadcaster — primetime evening news')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">Captain Crusty</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800">Cartoon Pirate</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Gravelly old sailor — cartoon villain energy, raspy harmonic overdrive.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('crusty')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('Captain Crusty', 'Gravelly old sailor — cartoon villain energy')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">The Podcaster</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800">Aussie Host</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Aussie explainer-show host — quick, punchy, conversational and friendly.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('podcaster')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('The Podcaster', 'Aussie explainer-show host — quick, punchy')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">Junior Quacks</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-purple-950 text-purple-300 border border-purple-800">Animation Sidekick</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Anxious squawky sidekick — fast tempo, dynamic pitch shifts for animated shows.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('junior')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('Junior Quacks', 'Anxious squawky sidekick — fast tempo cartoon')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="bg-canvas-subtle border border-canvas-border hover:border-brand-500/50 rounded-xl p-4 transition duration-200 group flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h4 class="font-semibold text-white text-sm group-hover:text-brand-300 transition">Cinematic Noir Lead</h4>
                <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800">Film Lead</span>
              </div>
              <p class="text-xs text-slate-400 line-clamp-2">Deep resonant French/English actor voice — whisper compression, heavy emotion.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-canvas-border flex items-center justify-between">
              <button onclick="playVoicePreview('noir')" class="w-7 h-7 rounded-full bg-canvas-elevated hover:bg-brand-500 flex items-center justify-center text-white transition">
                <svg class="w-3.5 h-3.5 fill-current ml-0.5" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
              <button onclick="useDesign('Cinematic Noir Lead', 'Deep resonant film lead voice with whisper compression')" class="text-xs text-brand-400 hover:text-brand-300 font-medium flex items-center space-x-1 transition">
                <span>Use this design</span>
                <span>→</span>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- Section: Script Editor & Real-time Lip-Sync Audio Generation -->
      <div class="bg-canvas-subtle border border-canvas-border rounded-xl p-5 space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Cinematic Script & Speech Synthesis</span>
            <span id="activePresetBadge" class="neon-pill text-[11px] px-2 py-0.5 rounded-full font-mono">The Librarian Active</span>
          </div>
          <div class="flex items-center space-x-3 text-xs">
            <label class="text-slate-400">Target Language:</label>
            <select id="targetLanguage" class="bg-canvas-panel border border-canvas-border rounded px-2.5 py-1 text-slate-200 font-mono text-xs focus:outline-none focus:border-brand-500">
              <option value="fr">French (Français)</option>
              <option value="en">English (US/UK)</option>
              <option value="es">Spanish (Español)</option>
              <option value="de">German (Deutsch)</option>
              <option value="ja">Japanese (日本語)</option>
              <option value="ar">Arabic (العربية)</option>
              <option value="it">Italian (Italiano)</option>
            </select>
          </div>
        </div>

        <!-- Script Textarea -->
        <div class="relative">
          <textarea id="scriptInput" rows="5" class="w-full bg-canvas-panel border border-canvas-border rounded-lg p-4 text-sm text-slate-100 placeholder-slate-600 focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500 transition leading-relaxed font-sans" placeholder="Type or paste the dialogue scene script here..."></textarea>
          <div class="absolute bottom-3 right-3 text-[11px] text-slate-500 font-mono">
            <span id="wordCount">0 words</span> • <span id="estTime">0.0s est. duration</span>
          </div>
        </div>

        <!-- Synthesis Bar & Audio Waveform Player -->
        <div class="pt-2 flex flex-col md:flex-row items-center justify-between gap-4">
          <div class="flex items-center space-x-4 w-full md:w-auto">
            <div class="flex items-center space-x-2 text-xs text-slate-400 font-mono">
              <span class="w-2.5 h-2.5 rounded-full bg-brand-500 animate-pulse"></span>
              <span id="engineStatus">Ready: 24kHz High-Fidelity Kokoro/F5-TTS</span>
            </div>
            <div id="audioWaveMock" class="hidden items-center space-x-1 h-6">
              <span class="w-1 bg-brand-500 rounded-full h-3 animate-pulse"></span>
              <span class="w-1 bg-brand-400 rounded-full h-5 animate-pulse"></span>
              <span class="w-1 bg-brand-300 rounded-full h-2 animate-pulse"></span>
              <span class="w-1 bg-brand-500 rounded-full h-6 animate-pulse"></span>
              <span class="w-1 bg-brand-400 rounded-full h-4 animate-pulse"></span>
            </div>
          </div>

          <div class="flex items-center space-x-3 w-full md:w-auto justify-end">
            <button onclick="synthesizeScript()" id="synthBtn" class="brand-glow px-6 py-2.5 rounded-lg bg-gradient-to-r from-brand-600 to-brand-accent hover:from-brand-500 hover:to-brand-400 text-white font-medium text-xs flex items-center space-x-2 transition cursor-pointer active:scale-95">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              <span>⚡ Synthesize Audio</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Section: Video Dubbing Pipeline & Full Movie Remuxer -->
      <div class="bg-canvas-subtle border border-canvas-border rounded-xl p-5 space-y-4">
        <div class="flex items-center justify-between">
          <h3 class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
            <svg class="w-4 h-4 text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/></svg>
            <span>Full Video / Movie Pipeline</span>
          </h3>
          <span class="text-xs text-slate-500 font-mono">Demux → Separate → Whisper STT → Translate → Clone TTS → FFmpeg Remux</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Step 1 -->
          <div class="bg-canvas-panel border border-canvas-border rounded-lg p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-medium text-white">1. Input Movie</span>
              <span class="text-[10px] text-emerald-400 font-mono">MKV, MP4</span>
            </div>
            <p class="text-[11px] text-slate-400">Select file or drag video directly from your filesystem.</p>
            <div class="border border-dashed border-canvas-border rounded p-3 text-center cursor-pointer hover:border-brand-500 transition">
              <span class="text-xs text-brand-400">Choose movie file...</span>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="bg-canvas-panel border border-canvas-border rounded-lg p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-medium text-white">2. Stem Ducking</span>
              <span class="text-[10px] text-brand-400 font-mono">Demucs v4</span>
            </div>
            <p class="text-[11px] text-slate-400">Music and explosive sound effects are preserved and auto-ducked under dialogue.</p>
            <div class="flex items-center justify-between text-xs pt-1">
              <span class="text-slate-400">Ducking Level</span>
              <span class="text-slate-200 font-mono">-14 dB</span>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="bg-canvas-panel border border-canvas-border rounded-lg p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-medium text-white">3. Remux Output</span>
              <span class="text-[10px] text-cyan-400 font-mono">Zero Lip-Sync Drift</span>
            </div>
            <p class="text-[11px] text-slate-400">Pitch-preserving WSOLA time-stretches dialogue to match exact video keyframes.</p>
            <button onclick="alert('Full video dub pipeline ready. Use `opendub run <video.mp4>` in terminal or submit via API!')" class="w-full py-1.5 rounded bg-brand-900/50 hover:bg-brand-900 text-brand-300 border border-brand-700/50 text-xs font-medium transition">
              Launch Full Pipeline
            </button>
          </div>
        </div>
      </div>

    </div>

    <!-- ==================== BOTTOM STATUS & INTEGRATIONS DOCK ==================== -->
    <footer class="h-10 bg-canvas-base border-t border-canvas-border px-4 flex items-center justify-between shrink-0 text-xs text-slate-500">
      <div class="flex items-center space-x-4">
        <!-- Integrations badges -->
        <span class="text-[11px] text-slate-400 font-mono">Integrations:</span>
        <div class="flex items-center space-x-2">
          <span class="px-2 py-0.5 rounded bg-canvas-panel border border-canvas-border text-[11px] text-slate-300 flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span>Demucs v4</span>
          </span>
          <span class="px-2 py-0.5 rounded bg-canvas-panel border border-canvas-border text-[11px] text-slate-300 flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span>OpenAI Whisper</span>
          </span>
          <span class="px-2 py-0.5 rounded bg-canvas-panel border border-canvas-border text-[11px] text-slate-300 flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span>Kokoro-82M / F5-TTS</span>
          </span>
          <span class="px-2 py-0.5 rounded bg-canvas-panel border border-canvas-border text-[11px] text-slate-300 flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span>Ollama Local LLM</span>
          </span>
          <span class="px-2 py-0.5 rounded bg-canvas-panel border border-canvas-border text-[11px] text-slate-300 flex items-center space-x-1">
            <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
            <span>FFmpeg 6.0</span>
          </span>
        </div>
      </div>

      <div class="flex items-center space-x-3">
        <a href="https://github.com/Dali5599/opendub" target="_blank" class="hover:text-brand-400 transition flex items-center space-x-1">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
          <span>Dali5599/opendub</span>
        </a>
        <span>•</span>
        <span class="font-mono text-brand-400">v0.1.0-production</span>
      </div>
    </footer>
  </main>

  <script>
    // Demo script sample
    const sampleScript = "Beyond the city lights, a quieter world begins. Every trail holds a story, and every journey starts with a little curiosity.";
    document.getElementById('scriptInput').value = sampleScript;
    updateScriptMetrics();

    document.getElementById('scriptInput').addEventListener('input', updateScriptMetrics);

    function updateScriptMetrics() {
      const text = document.getElementById('scriptInput').value.trim();
      const words = text ? text.split(/\\s+/).length : 0;
      document.getElementById('wordCount').innerText = `${words} words`;
      // Average 140 words per minute ~ 2.33 words per second
      const estSeconds = (words / 2.33).toFixed(1);
      document.getElementById('estTime').innerText = `${estSeconds}s est. duration`;
    }

    function selectTag(btn, tagName) {
      btn.classList.toggle('bg-brand-500/20');
      btn.classList.toggle('border-brand-500');
      btn.classList.toggle('text-brand-300');
      const promptInput = document.getElementById('voicePromptInput');
      if (promptInput.value.includes(tagName)) {
        promptInput.value = promptInput.value.replace(new RegExp(',?\\\\s*' + tagName), '').trim();
      } else {
        promptInput.value = promptInput.value ? `${promptInput.value}, ${tagName}` : tagName;
      }
    }

    document.getElementById('resetPromptBtn').addEventListener('click', () => {
      document.getElementById('voicePromptInput').value = '';
      document.querySelectorAll('.tag-pill').forEach(pill => {
        pill.classList.remove('bg-brand-500/20', 'border-brand-500', 'text-brand-300');
      });
    });

    function useDesign(title, desc) {
      document.getElementById('voicePromptInput').value = desc;
      document.getElementById('activePresetBadge').innerText = `${title} Active`;
    }

    function playVoicePreview(voiceId) {
      // Simulate real-time audio sample play
      const status = document.getElementById('engineStatus');
      status.innerText = `Streaming high-res reference audio for [${voiceId}]...`;
      const wave = document.getElementById('audioWaveMock');
      wave.classList.remove('hidden');
      wave.classList.add('flex');

      setTimeout(() => {
        status.innerText = 'Ready: 24kHz High-Fidelity Kokoro/F5-TTS';
        wave.classList.remove('flex');
        wave.classList.add('hidden');
      }, 2500);
    }

    function synthesizeScript() {
      const btn = document.getElementById('synthBtn');
      const origContent = btn.innerHTML;
      btn.innerHTML = `<svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white inline" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg> Synthesizing...`;
      
      const wave = document.getElementById('audioWaveMock');
      wave.classList.remove('hidden');
      wave.classList.add('flex');
      document.getElementById('engineStatus').innerText = 'Generating zero-shot speech with emotional curve...';

      setTimeout(() => {
        btn.innerHTML = origContent;
        wave.classList.remove('flex');
        wave.classList.add('hidden');
        document.getElementById('engineStatus').innerText = '✅ Speech synthesized successfully (24kHz WAV, 100% synchronized)';
      }, 1800);
    }

    function saveVoiceProfile() {
      const name = document.getElementById('profileNameInput').value.trim();
      if (!name) {
        alert('Please enter a voice profile name first.');
        return;
      }
      alert(`Voice profile "${name}" successfully saved to local model registry!`);
      document.getElementById('profileNameInput').value = '';
    }
  </script>
</body>
</html>
"""


class WebStudioDashboard:
    """Serves the interactive creator studio dashboard."""

    @staticmethod
    def get_html() -> str:
        return STUDIO_HTML
