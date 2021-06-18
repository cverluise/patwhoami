import typer
from patwhoami import prep

app = typer.Typer()

app.add_typer(prep.app, name="prep")


if __name__ == "__main__":
    app()
