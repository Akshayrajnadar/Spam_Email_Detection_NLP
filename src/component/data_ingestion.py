import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.component.data_transformation import DataTransformation
from src.component.data_transformation import DataTransformationConfig

from src.component.model_training import ModelTrainerConfig
from src.component.model_training import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):

        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    pass