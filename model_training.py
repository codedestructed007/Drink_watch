import sys
from src.logger import logger
from src.pipeline.train_pipeline import  TrainPipeline
from src.exception import CustomException


try:
    trainer = TrainPipeline()
    trainer.initialize_training_pipeline()
    logger.info('Model training is successful')
except Exception as e:
    raise CustomException(e,sys)



