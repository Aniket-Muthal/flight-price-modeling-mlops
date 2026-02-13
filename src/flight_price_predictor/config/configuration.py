from pathlib import Path
from flight_price_predictor.utils.data_io import load_yaml, create_directories
from flight_price_predictor.core.constants import *
from flight_price_predictor.core.exception import CustomException
from flight_price_predictor.core.logging_setup import get_logger
from flight_price_predictor.config.entity_config import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_path=TRAINING_CONFIG_PATH):
        self.config_path = config_path

        self.config = load_yaml(self.config_path)

        create_directories([
            Path(self.config.data_ingestion.raw_data_path)
        ])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            raw_data_path=Path(config.raw_data_path)
        )

        return data_ingestion_config