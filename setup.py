"""
setup.py
--------

Packaging configuration for the Flight Price Prediction MLOps pipeline.

This script defines metadata and packaging instructions required
to install the project as a Python package using setuptools.

The package follows a src-layout structure, where all source code
lives under the `src/` directory.
"""


## -------------------------------------------------------------------------------------------------------------------- ##
from setuptools import setup, find_packages


## -------------------------------------------------------------------------------------------------------------------- ##
setup(
    name="flight_price_predictor",
    version="0.1.0",
    author="Aniket Muthal",
    author_email="aniketmuthal93@gmail.com",
    description="Flight Price Prediction ML Pipeline",
    url="https://github.com/Aniket-Muthal/flight-price-modeling-mlops",
    packages=find_packages(where="src"),     # Discover packages under src/
    package_dir={"": "src"},                  # Root package directory
    python_requires=">=3.11",
    include_package_data=True,                # Include non-Python files (from MANIFEST.in)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    # Optional extras for dev and prod packages
    extras_require={
        "dev": [
            "notebook",
            "ipykernel",
            "seaborn",
            "xgboost",
            "statsmodels",
            "scipy",
        ],
        "prod-extras": [
            "dvc[gdrive]",
            "mlflow",
            "streamlit",
            "gdown",
        ],
    },
)


## -------------------------------------------------------------------------------------------------------------------- ##