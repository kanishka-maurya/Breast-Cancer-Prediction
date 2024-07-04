from src.logger import logging
import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

try:
    data_ingestion = DataIngestion()
    train_data_path,test_data_path = data_ingestion.initiate_DataIngestion()
    #data_transformation_config = DataTransformationConfig()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path,test_data_path)
except Exception as e:
    raise CustomException(e,sys)

