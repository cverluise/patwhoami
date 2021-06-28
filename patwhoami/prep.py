import pandas as pd
import typer

# import json
from patwhoami.lib import CATS
from pathlib import Path
from spacy.tokens import DocBin
from spacy.training import Example
import spacy
import random
import math

app = typer.Typer()


@app.command()
def split_train_test(
    file: Path, train: Path, test: Path, split_ratio: float = 0.2, random_seed: int = 42
) -> None:
    """
    Split the training data (in `file`) into two files: train and test.

    Arguments:
        file: training data file path (CSV)
        train: train data file destination
        test: test data file destination
        split_ratio: train-test split ratio
        random_seed: random seed (for split reproducibility)

    **Usage:**
        ```shell
        patwhoami prep split-train-test data/training.csv data/train.csv data/test.csv
        ```
    """
    df = pd.read_csv(file)
    nb_examples = len(df)
    random.seed(random_seed)

    test_sample = random.sample(
        range(nb_examples), math.ceil(nb_examples * split_ratio)
    )
    train_sample = list(set(range(nb_examples)) - set(test_sample))

    df.iloc[test_sample].to_csv(test, index=False)
    df.iloc[train_sample].to_csv(train, index=False)


@app.command()
def to_spacy(file: Path, dest: Path, language: str = "xx") -> None:
    """
    Return a CSV training data (text, cat, country_code) as a spaCy 3 file which can be ingested directly

    Arguments:
        file: training data file path (csv)
        dest: destination file path (.spacy)
        language: spacy 2 letter code language (xx for multi-language)

    **Usage:**
        ```shell
        patwhoami prep to-spacy data/train.csv data/train.spacy
        ```

    !!! note "spaCy training data"
        [Annotation format for creating training examples](https://spacy.io/api/data-formats#training)
    """
    df = pd.read_csv(file)
    nlp = spacy.blank(language)
    examples = []
    doc_bin = DocBin()

    for i, row in df.iterrows():
        # print(i)
        row = row.to_dict()
        cats = CATS.copy()
        cats.update({row["cat"]: 1})
        doc = nlp(row["text"])
        gold_dict = {"cats": cats}
        examples += [Example.from_dict(doc, gold_dict)]

        # row.update({"cats": cats})
        # typer.echo(json.dumps(row))

    [doc_bin.add(example.reference) for example in examples]
    doc_bin.to_disk(dest)


if __name__ == "__main__":
    app()
