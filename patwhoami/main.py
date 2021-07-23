import typer
from patwhoami import prep, pred, evaluate

app = typer.Typer()

app.add_typer(prep.app, name="prep")
app.add_typer(pred.app, name="pred")
app.add_typer(evaluate.app, name="eval")


if __name__ == "__main__":
    app()
