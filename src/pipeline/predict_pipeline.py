from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import  DataIngestion
from src.utils import load_object
temp = ModelTrainer
temp.mo
class PredictPineline:
    def __init__(self):

    def predict(self, features):
        # features will be feeded in model
        #load the model
        # will be required path of model
        load_object()











from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import  DataIngestion
ingestion = DataIngestion()
ingestion.initiate_data_ingestion()
transformation_object = DataTransformation()
transformation_object.data_transformation('artifacts/train.csv','artifacts/train.csv')
#
trainer = ModelTrainer()

best_model_score , model =trainer.initiate_model_training("artifacts/Transformed_datasets/train_df.csv","artifacts/Transformed_datasets/test_df.csv")


