import typer
from patwhoami import prep, pred

app = typer.Typer()

app.add_typer(prep.app, name="prep")
app.add_typer(pred.app, name="pred")


if __name__ == "__main__":
    app()
