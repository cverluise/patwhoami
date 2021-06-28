# RECIPE

## Prep data for training

```shell
patwhoami prep split-train-test data/training.csv data/train.csv data/test.csv
patwhoami prep to-spacy data/test.csv data/test.spacy
patwhoami prep to-spacy data/train.csv data/train.spacy
```

## Train model

```shell
spacy train configs/default_cnn.cfg  --paths.train data/train.spacy --paths.dev data/test.spacy -o models/default_cnn
spacy train configs/default_bow.cfg  --paths.train data/train.spacy --paths.dev data/test.spacy -o models/default_bow
```

## Pred

```shell
patwhoami pred cats data/irl.jsonl models/default_cnn/model-best >> data/irl_pred.jsonl
```

## Active training

```shell
patwhoami prep active-training data/irl_pred.jsonl data/active_training.jsonl
```
