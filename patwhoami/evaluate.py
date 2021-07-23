import json
import pandas as pd
from glob import glob
import typer

app = typer.Typer()


@app.command()
def spacy_model(path: str):
    """
    Print the performance of the model(s) (evaluated on the test set) to std out. Restricted to `cats_f_per_type`

    Arguments:
        path: spacy models meta.json path (wildcard enabled)

    **Usage:**
        ```shell
        patwhoami eval spacy-model models/*/model-best/meta.json
        ```
    """
    files = glob(path)

    for file in files:
        with open(file, "r") as meta:
            meta = json.loads(meta.read())
            df = pd.DataFrame.from_dict(
                meta.get("performance").get("cats_f_per_type")
            ).round(2)
            typer.echo(f"# {file}")
            typer.echo(df.to_markdown() + "\n")


if __name__ == "__main__":
    app()
