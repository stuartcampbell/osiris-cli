import typer

app = typer.Typer()


@app.command()
def create(data_session: str):
    typer.echo(f"Creating data session: {data_session}")

@app.command()
def delete(data_session: str):
    typer.echo(f"Deleting data session: {data_session}")

@app.command()
def list():
    typer.echo(f"Listing data sessions.")

@app.command()
def show(data_session: str):
    typer.echo(f"Showing info on data sessions. {data_session}")

