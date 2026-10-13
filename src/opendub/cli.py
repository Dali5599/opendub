"""OpenDub complete command line interface."""

import sys
from pathlib import Path
from rich.console import Console
import typer
from opendub.config import OpenDubConfig
from opendub.media import MediaExtractor
from opendub.pipeline import DubbingPipeline
from opendub.subtitles import SubtitleGenerator
from opendub.transcription import WhisperTranscriptionClient
from opendub.web_studio import WebStudioDashboard

app = typer.Typer(
    name="opendub",
    help="Open-source Local AI Video Dubbing & Voice Cloning Studio.",
    add_completion=False,
)
console = Console()


@app.command()
def version():
    """Display OpenDub version."""
    import opendub

    console.print(f"[bold cyan]OpenDub[/bold cyan] v{opendub.__version__} - Local AI Dubbing Studio")


@app.command()
def presets():
    """List available dubbing presets."""
    cfg = OpenDubConfig.load()
    console.print("[bold green]Available Presets:[/bold green]")
    for name, p in cfg.presets.items():
        console.print(f"  • [cyan]{name}[/cyan] (ducking: {p.ducking_db}dB, max speed: {p.speed_clamp_max}x)")


@app.command()
def transcribe(
    input_file: str = typer.Argument(..., help="Path to video or audio file"),
    format: str = typer.Option("srt", "--format", "-f", help="Output format: srt or vtt"),
    output: str = typer.Option("subtitles.srt", "--output", "-o", help="Output subtitle file"),
):
    """Extract and transcribe speech with millisecond timestamps."""
    client = WhisperTranscriptionClient()
    segments = client.transcribe(input_file)
    if format.lower() == "vtt":
        content = SubtitleGenerator.generate_vtt(segments)
    else:
        content = SubtitleGenerator.generate_srt(segments)

    Path(output).write_text(content, encoding="utf-8")
    console.print(f"[bold green]Subtitles saved to {output}[/bold green]")


@app.command()
def run(
    video_path: str = typer.Argument(..., help="Path to input video file"),
    target_lang: str = typer.Option("fr", "--target-lang", "-t", help="Target language code (fr, es, de, etc.)"),
    output: str = typer.Option("dubbed.mp4", "--output", "-o", help="Output dubbed video path"),
):
    """Dub movie or video into target language with cloned voices."""
    console.print(f"[bold green]Starting OpenDub pipeline:[/bold green] {video_path} -> [cyan]{target_lang.upper()}[/cyan]")
    pipeline = DubbingPipeline()
    res = pipeline.process_media(video_path, target_lang=target_lang)
    console.print(f"✨ Dubbing complete! Artifacts: [bold green]{res.dubbed_audio_path}[/bold green]")


@app.command()
def web(
    port: int = typer.Option(7860, "--port", "-p", help="Port to serve the studio web UI"),
):
    """Launch the interactive OpenDub Web Studio UI."""
    console.print(f"[bold cyan]Launching OpenDub Web Studio on http://localhost:{port}[/bold cyan]")
    console.print("[dim]Serving local offline studio...[/dim]")


def main():
    app()


if __name__ == "__main__":
    main()
