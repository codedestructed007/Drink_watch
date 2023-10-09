import sys
import os
from src.logger import logger

from src.exception import CustomException
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str= os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def basic_filteration_in_raw_data(self,testing = False,rows =0.001):
        try:
            if testing == True:
                df = pd.read_csv('notebook/data/smoking.csv')
                random_index_length = len(df) * rows
                random_index = [np.random.randint(0, len(df)-1) for _ in range(int(random_index_length))]
                df = df.iloc[random_index,:]

            else:
                df = pd.read_csv("notebook/data/smoking.csv")

            if df.duplicated().sum() > 0:
                df_length_before = len(df)
                df.drop_duplicates(inplace=True)
                df_length_after  = len(df)
                logger.info('Found some duplicate rows')
                logger.info('{} rows are removed completely'.format(df_length_before - df_length_after))

            return df
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        logger.info('Entered the data Ingestion method of component')
        try:
            # A filter raw dataset
            df  = self.basic_filteration_in_raw_data(testing=True,)
            logger.info('Read the dataset')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logger.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index= False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)
            logger.info('Train and Test datasets are dumped')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)