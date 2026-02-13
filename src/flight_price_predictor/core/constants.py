"""
config.py
---------

Centralized project configuration and file paths.

This module serves as a single source of truth for configuration values
used across training, evaluation, and deployment workflows.
"""


#------------------------------------------------------------------------------#
from pathlib import Path

#------------------------------------------------------------------------------#
#------------------------------PROJECT ROOT------------------------------------#
#------------------------------------------------------------------------------#

PROJECT_ROOT = Path(__file__).resolve().parents[3]

#------------------------------------------------------------------------------#
#----------------------------------PATHS---------------------------------------#
#------------------------------------------------------------------------------#
LOGS_DIR    = PROJECT_ROOT / "logs"
CONFIGS_DIR = PROJECT_ROOT / "configs"
SCHEMA_DIR  = CONFIGS_DIR / "schema"

TRAINING_CONFIG_PATH = CONFIGS_DIR / "training-config.yaml"
INFERENCE_CONFIG_PATH = CONFIGS_DIR / "inference-config.yaml"
PARAMS_PATH = CONFIGS_DIR / "params.yaml"

RAW_SCHEMA_PATH       = SCHEMA_DIR / "schema-raw.yaml"
# CLEANED_SCHEMA_PATH   = SCHEMA_DIR / "schema_cleaned.yaml"
# PROCESSED_SCHEMA_PATH = SCHEMA_DIR / "schema_processed.yaml"
# VALID_VALUES_PATH     = SCHEMA_DIR / "valid_values.yaml"

#------------------------------------------------------------------------------#
#------------------------------FILE NAMES--------------------------------------#
#------------------------------------------------------------------------------#
RAW_FILE = "flight_price.csv"

CLEAN_TRAIN_FILE = "cleaned_train.csv"
CLEAN_TEST_FILE  = "cleaned_test.csv"

CLEAN_IMPUTED_TRAIN_FILE = "cleaned_imputed_train.csv"
CLEAN_IMPUTED_TEST_FILE  = "cleaned_imputed_test.csv"

TRANSFORMED_TRAIN_FILE = "transformed_train.csv"
TRANSFORMED_TEST_FILE  = "transformed_test.csv"

INFERENCE_FILE = "test.csv"
PREDICTION_FILE = "predictions.csv"
#------------------------------------------------------------------------------#
#-------------------------------ARTIFACTS--------------------------------------#
#------------------------------------------------------------------------------#
MODEL_FILE                = "model.pkl"
PIPELINE_FILE             = "inference_pipeline.pkl"
FEATURE_CLEANER_FILE      = "feature_cleaner.pkl"
FEATURE_PREPROCESSOR_FILE = "feature_preprocessor.pkl"
METRICS_FILE              = "evaluated_results.json"

VALIDATION_STATUS_FILE    = "validation_status.txt"
VALIDATION_REPORT_FILE    = "validation_report.json"

#------------------------------------------------------------------------------#
#----------------------LOGGER NAMES & LOG FILE NAMES---------------------------#
#------------------------------------------------------------------------------#
TRAINING_PIPELINE_LOGGER   = "Pipeline"
TRAINING_PIPELINE_LOG_FILE = "training_pipeline.log"

INFERENCE_PIPELINE_LOGGER = "Inference Pipeline"
INFERENCE_PIPELINE_LOG_FILE = "inference_pipeline.log"

DATA_INGESTION_LOGGER   = "Data Ingestion"
DATA_INGESTION_LOG_FILE = "data_ingestion.log"

DATA_VALIDATION_LOGGER   = "Data Validation"
DATA_VALIDATION_LOG_FILE = "data_validation.log"

DATA_CLEANING_LOGGER   = "Data Cleaning"
DATA_CLEANING_LOG_FILE = "data_cleaning.log"

DATA_TRANSFORMATION_LOGGER   = "Data Transformation"
DATA_TRANSFORMATION_LOG_FILE = "data_transformation.log"

MODEL_TRAINER_LOGGER   = "Model Trainer"
MODEL_TRAINER_LOG_FILE = "model_trainer.log"

MODEL_EVALUATION_LOGGER   = "Model Evaluation"
MODEL_EVALUATION_LOG_FILE = "model_evaluation.log"

#------------------------------------------------------------------------------#
#------------------------------TARGET COLUMN-----------------------------------#
#------------------------------------------------------------------------------#
TARGET_COLUMN = "price"

#------------------------------------------------------------------------------#