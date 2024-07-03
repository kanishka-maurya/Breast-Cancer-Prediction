from src.logger import logging
import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
try:
    data_ingestion = DataIngestion()
    data_ingestion.initiate_DataIngestion()
except Exception as e:
    raise CustomException(e,sys)