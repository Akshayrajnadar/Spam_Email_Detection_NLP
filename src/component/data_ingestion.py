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