"""Command line interface executable of pyprocgen."""

import typer
from rich import print

app = typer.Typer()


@app.command()
def cli() -> None:
    """Generate a map and output it to the command line."""
    print("hello world!")


@app.command()
def version() -> None:
    """Display pyprocgen's version."""
    print("2.0.0")  # todo
