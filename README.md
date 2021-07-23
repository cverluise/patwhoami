# patWhoami

A python library to classify patent assignees into research agents and others. Bonus: classify research agents into sub-groups: University, National research agency and Hospital.

## Usage

```python
import spacy
nlp = spacy.load("models/default_cnn/model-best")

for text in ["Centre national de la recherche scientifique",
             "Harvard University",
             "Aymann Mhammedi",
             "GdF Suez",
             "Max Planck Institute",
             "New York Hospital",
             "Klinikum an der Isar",
             "Boston College",
             "Deutsches Zentrum für Luft und Raumfahrt",
             "China Academy of Science"]:
    doc = nlp(text.lower())
    cat_pred, score_pred = sorted([[k, v] for k, v in doc.cats.items()], key=lambda x: x[1], reverse=True)[0]
    print(doc.text, ":", cat_pred, round(score_pred, 2))

>>>
centre national de la recherche scientifique : RES_INSTITUTE 1.0
harvard university : UNIVERSITY 1.0
aymann mhammedi : OTHER 1.0
gdf suez : OTHER 1.0
max planck institute : RES_INSTITUTE 1.0
new york hospital : HOSPITAL 1.0
klinikum an der isar : HOSPITAL 0.97
boston college : UNIVERSITY 1.0
deutsches zentrum für luft und raumfahrt : OTHER 0.3
china academy of science : RES_INSTITUTE 0.74
````

## patwhoami X HuggingFace hub

- View the model: https://huggingface.co/cverluise/xx_cat_pateexx_md. NB: texcat inference API not yet supported for spacy models
- Install the model: `pip install https://huggingface.co/cverluise/xx_cat_pateexx_md/resolve/main/xx_cat_pateexx_md-any-py3-none-any.whl`
