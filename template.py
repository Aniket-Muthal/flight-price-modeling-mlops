"""
template.py
-----------

Project Scaffold Generator for Flight Price Prediction Pipeline

This script generates the folder and module structure for a flight price modeling ML project.
It creates all required directories and placeholder Python files, 
ready for incremental development of the pipeline components.

Usage:
------
Simply run the script at the project root:

    python template.py

It will create:
- Folders for source code, configs, notebooks, and pipelines
- Empty Python modules for later development
- Project-level files like main.py, inference.py, README.md, environment.yaml, requirements.txt
"""


## -------------------------------------------------------------------------------------------------------------------- ##
from pathlib import Path


## -------------------------------------------------------------------------------------------------------------------- ##
## -----------------------------------------------Project Structure---------------------------------------------------- ##
## -------------------------------------------------------------------------------------------------------------------- ##

PROJECT_NAME = "flight_price_predictor"

folders = [
    "configs",
    "notebooks/helpers",
    f"src/{PROJECT_NAME}/core",
    f"src/{PROJECT_NAME}/utils",
    f"src/{PROJECT_NAME}/config",
    f"src/{PROJECT_NAME}/components",
    f"src/{PROJECT_NAME}/transformers",
    f"src/{PROJECT_NAME}/pipeline",
]

placeholder_files = {
    "configs": ["training-config.yaml", "inference-config.yaml", "schema-raw.yaml", "params.yaml"],
    "notebooks/helpers": ["data_io_utilities.py", "data_diagnostics.py", "eda_helpers.py"],
    "notebooks": [".gitkeep"],
    f"src/{PROJECT_NAME}": ["__init__.py"],
    f"src/{PROJECT_NAME}/core": ["__init__.py", "constants.py", "logging_setup.py", "exception.py"],
    f"src/{PROJECT_NAME}/utils": ["__init__.py", "data_io.py"],
    f"src/{PROJECT_NAME}/config": ["__init__.py", "entity_config.py", "configuration.py"],
    f"src/{PROJECT_NAME}/components": ["__init__.py", "data_ingestion.py", "data_validation.py", "data_cleaning.py",
                                      "data_transformation.py", "model_trainer.py", "model_evaluation.py"],
    f"src/{PROJECT_NAME}/transformers": ["__init__.py"],
    f"src/{PROJECT_NAME}/pipeline": ["__init__.py", "inference_pipeline.py"],
    "": [
        "app.py",
        "setup.py",
        ".gitignore",
        "LICENSE",
        "README.md",
        "environment-dev.yaml",
        "environment-prod.yaml",
        "requirements.txt",
        "pyproject.toml",
        "dvc.yaml"
        ]
}

for folder in folders:
    path = Path(folder)
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created folder: {path}")

for folder, files in placeholder_files.items():
    for filename in files:
        path = Path(folder) / filename if folder else Path(filename)
        if not path.exists():
            path.touch()
            print(f"Created placeholder file: {path}")

print("\nProject scaffold created successfully!")
print("Next steps:")
print("1. Start notebook experimentation")
print("2. Add modular scripts to src")
print("3. Orchestrate and evaluate entire ML pipeline")
print("4. Document project flow")


## -------------------------------------------------------------------------------------------------------------------- ##