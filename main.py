import typer

import data_session
import instruments
import users

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(instruments.app, name="instruments")
app.add_typer(data_session.app, name="data-session")

if __name__ == "__main__":
    app()

