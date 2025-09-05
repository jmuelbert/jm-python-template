# SPDX-License-Identifier: EUPL-1.2
# SPDX-FileCopyrightText: 2023-present Jürgen Mülbert <juergen.muelbert@outlook.de>
#

from typing import Annotated

import typer
from rich.console import Console

console = Console()

sub_app = typer.Typer(help="A sample CLI")


@sub_app.command()
def docs(name: str = typer.Option(..., help="The name of the project")) -> None:
    """Generate docs for a project."""
    console.print(f"Generating docs for {name}")


@sub_app.command(hidden=True)
def hello(
    name: Annotated[str, typer.Argument(..., help="The name of the person to greet")],
    color: Annotated[
        str | None, typer.Option("--color", help="The color of the output")
    ] = None,
) -> None:
    """Some docstring content."""
    _str = f"Hello {name}"

    if color:
        typer.echo(f"[{color}]{_str}[/{color}]")
    else:
        typer.echo(_str)
