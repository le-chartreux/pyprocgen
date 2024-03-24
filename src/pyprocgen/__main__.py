"""Command line interface executable of pyprocgen."""

import typer
from rich import print

app = typer.Typer()


@app.command()
def cli() -> None:
    print("hello world!")


@app.command()
def version() -> None:
    print("2.0.0")
