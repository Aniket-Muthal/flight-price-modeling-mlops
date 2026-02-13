import os
import sys
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from flight_price_predictor.core.constants import *
from flight_price_predictor.core.logging_setup import get_logger
from flight_price_predictor.core.exception import CustomException
from flight_price_predictor.config.configuration import ConfigurationManager
from flight_price_predictor.config.entity_config import DataIngestionConfig


logger = get_logger(
    name=DATA_INGESTION_LOGGER,
    log_file_path=LOGS_DIR/DATA_INGESTION_LOG_FILE
)

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def _get_db_engine(self):
        """
        Returns a SQLAlchemy engine connected to configured database.
        """
        try:
            return create_engine(
                f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            )
        
        except Exception as e:
            raise CustomException(e, sys)
    
    def load_data_from_db(self):
        try:
            logger.info("Looking for DB engine...")
            engine = self._get_db_engine()
            logger.info("DB connection established")
            query = "SELECT * FROM flight_prices"
            logger.info("Reading data from DB...")
            df = pd.read_sql(sql=query, con=engine)
            logger.info("Data loaded")
            logger.info("Saving snapshot of raw data...")
            file_path = Path(self.config.raw_data_path / RAW_FILE)
            df.to_csv(file_path, index=False)
            logger.info("Snapshot of raw data saved")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.load_data_from_db()