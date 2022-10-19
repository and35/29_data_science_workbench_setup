# {{ cookiecutter.project_name }} 

By: {{ cookiecutter.project_author_name }}.

Version: {{ cookiecutter.project_version }}

{{ cookiecutter.project_description }}

## Prerequisites

- python >=3.x
## activate venv
after the template was created you should activate your venv, try: 
- source “venv/Scripts/activate”
- “venv/Scripts/activate”
i can't make the python version variable for the venv
then install the libs being into the venv:
- pip install -r requirements.txt

## Project organization

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
created by and3
