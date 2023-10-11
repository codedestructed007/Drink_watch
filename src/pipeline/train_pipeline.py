
import sys
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import  DataIngestion
from src.exception import  CustomException
class TrainPipeline:
    def __init__(self):
        pass

    def initialize_training_pipeline(self):
        try:
            ingestion = DataIngestion()
            ingestion.initiate_data_ingestion()
            transformation_object = DataTransformation()
            transformation_object.data_transformation('artifacts/train.csv','artifacts/train.csv')
            trainer = ModelTrainer()
            _,_,=trainer.initiate_model_training('artifacts/Transformed_datasets/train_df.csv','artifacts/Transformed_datasets/test_df.csv')


        except Exception as e:
            raise CustomException(e,sys)

#%%
