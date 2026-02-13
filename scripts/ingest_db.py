"""
ingest_db.py

This scripts simulates ETL workflow of data engineering.
It is responsible for:
- Loading database credentials from environment variables.
- Creating a MySQL database f it doesn't exist.
- Reading structured CSV files from a configured local directory.
- Ingesting data into specified database table using SQLAlchemy.

It is independent of ML pipeline logic and focusses purely on data storage
and persistence.

"""

## -------------------------------------------------------------------------------------- ##
## Imports
## -------------------------------------------------------------------------------------- ##
import os
import yaml
import pandas as pd
from pathlib import Path
from box import ConfigBox
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

## -------------------------------------------------------------------------------------- ##
## Load environment variables
## -------------------------------------------------------------------------------------- ##
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

## -------------------------------------------------------------------------------------- ##
## Load config
## -------------------------------------------------------------------------------------- ##
CONFIG_PATH = Path("configs/data-source.yaml")

with open(CONFIG_PATH, "r") as f:
    config_content = ConfigBox(yaml.safe_load(f))


## -------------------------------------------------------------------------------------- ##
## Database utilities
## -------------------------------------------------------------------------------------- ##
def create_database() -> None:
    """
    Creates the target MySQL database if it does not already exist.
    """
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    )
    with engine.begin() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))


def get_db_engine():
    """
    Returns a SQLAlchemy engine connected to configured database.
    """
    return create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


## -------------------------------------------------------------------------------------- ##
## Ingestion
## -------------------------------------------------------------------------------------- ##
def ingest_db(config: ConfigBox) -> None:
    """
    Reads CSV files from the configured directory and replaces data into
    the specified database table.

    Parameters
    ----------
    config: ConfigBox
        Configuration containing database tabe name and data directory.

    """
    engine = get_db_engine()
    table_name = config.database.table_name
    data_dir = Path(config.database.data_dir)

    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            df = pd.read_csv(data_dir / file)
            df.to_sql(
                name=table_name,
                con=engine,
                if_exists="replace",
                index=False
            )


## -------------------------------------------------------------------------------------- ##
## Entry point
## -------------------------------------------------------------------------------------- ##
if __name__ == "__main__":
    create_database()
    ingest_db(config=config_content)

## -------------------------------------------------------------------------------------- ##