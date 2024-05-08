import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os
import sys

class DataIngesionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngesionConfig() 

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("After loading Data Frame information")

            logging.info("Before Creating RAW Data with ARTIFACT Folder")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("After Creating RAW Data with ARTIFACT Folder")

            logging.info("Started Performing Train Test Split")
            train_data,test_data =train_test_split(data,test_size=0.25)
            logging.info("Train Test Split Completed")

            logging.info("Before Creating TRAIN and TEST Data with ARTIFACT Folder")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("AFTER Creating TRAIN and TEST Data with ARTIFACT Folder")

            logging.info("Data Ingestion Completed")

        except Exception as e:
            logging.error("Exception Occured at Data Ingestion Stage")
            raise customexception(e,sys)