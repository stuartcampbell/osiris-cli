from typing import Optional

import typer

import data_session
import instruments
import users

__version__ = 0.1

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(instruments.app, name="instruments")
app.add_typer(data_session.app, name="data-session")


def version_callback(value: bool):
    if value:
        typer.echo(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


@app.command()
def main(
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        ),
):
    pass


if __name__ == "__main__":
    typer.run(main)