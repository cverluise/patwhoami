import json
import typer
import spacy
from pathlib import Path

app = typer.Typer()


@app.command()
def cats(file: Path, model: Path):
    """

    Arguments:
        file:
        model:

    **Usage:**
        ```shell
        ```

    """
    nlp = spacy.load(model)
    with open(file, "r") as lines:
        for line in lines:
            line = json.loads(line)
            doc = nlp(line["text"].lower())
            line.update(doc.cats)
            typer.echo(json.dumps(line))


if __name__ == "__main__":
    app()
