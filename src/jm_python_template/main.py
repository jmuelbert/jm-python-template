# SPDX-FileCopyrightText: 2025-present Jürgen Mülbert <jmuelbert@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

import logging
from typing import Annotated

import typer
from rich.console import Console

from jm_python_template.__about__ import __version__
from jm_python_template.app import sub_app

console = Console()

logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


app = typer.Typer(
    name="cli",
    help="Demo CLI",
    rich_markup_mode="rich",
    pretty_exceptions_show_locals=False,
)

app.add_typer(
    sub_app,
    help="Run sub-app in CLI mode (run tests).",
)


def version_callback(*, value: bool) -> None:
    """
    Print the version and exit.

    Args:
        value (bool): Whether to print the version.

    Returns:
        None
    """
    if value:
        console.print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit


@app.command()
def comma(
    name: Annotated[str, typer.Option()] = "World",
    _version: Annotated[
        bool | None, typer.Option("--version", callback=version_callback)
    ] = None,
) -> None:
    """
    Main function of the application.

    Args:
        name (str): The name to greet.
        _version (Optional[bool]): Whether to print the version.

    Returns:
        None
    """
    logger.info("Hello, World! %s", name)


if __name__ == "__main__":
    app()
