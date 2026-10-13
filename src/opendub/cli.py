"""OpenDub command line interface."""

import typer
from rich.console import Console

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
def run(
    video_path: str = typer.Argument(..., help="Path to input video file"),
    target_lang: str = typer.Option("fr", "--target-lang", "-t", help="Target language code (fr, es, de, ar, etc.)"),
    output: str = typer.Option("output.mp4", "--output", "-o", help="Output dubbed video path"),
):
    """Dub video into target language with cloned voices."""
    console.print(f"[bold green]Starting OpenDub pipeline[/bold green] on {video_path} -> {target_lang}")


def main():
    app()


if __name__ == "__main__":
    main()
