import typer

app = typer.Typer()


@app.command()
def list():
    typer.echo(f"Listing all instruments.")


@app.command()
def show(name: str):
    typer.echo(f"Showing details for instrument: {name}")
