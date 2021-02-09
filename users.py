from typing import Optional

import typer

app = typer.Typer()


@app.command()
def create(user_name: Optional[str] = typer.Argument(None) ):
    if not user_name:
        user_name = typer.prompt("What's your name?")
    typer.echo(f"Creating user: {user_name}")


@app.command()
def delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")
