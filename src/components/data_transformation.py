# aim of data-transformation split -->> feature engineering
import sys
from dataclasses import dataclass
import numpy as  np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from sklearn.impute import SimpleImputer
import os
from src.utils import save_object
from sklearn.compose import ColumnTransformer

df = pd.read_csv(r"C:\Users\kanis\Desktop\Breast-Cancer-Prediction\notebook\raw.csv") 

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''This function is responsible for data transformation.
        '''

        try:

            num_features = list(df.columns)
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scalar",StandardScaler)])
            
            logging.info(f"Numerical features: {num_features}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_features)
                ]
            )
            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test file")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "diagnosis"
            num_features = list(df.columns)
            
            # dividing the train dataset into dependent and independent features  
            input_features_train_df = train_df.drop(columns=[target_column_name],axis = 1)
            target_feature_train_df = train_df[target_column_name]
            
            # dividing the test dataset into dependent and independent features  
            input_features_test_df = test_df.drop(columns=[target_column_name],axis = 1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing on training and test dataset")
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr,np.arr(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr,np.arr(target_feature_test_df)
            ]

            logging.info("Saved preprocessing object")
            save_object(
                file_path = DataTransformationConfig.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
