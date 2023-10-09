import sys
import os

import pandas as pd

import dill


from sklearn.metrics import r2_score ,mean_squared_error , accuracy_score
from src.exception import  CustomException
from src.logger import  logger



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            dill.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as obj:
            return dill.load(obj)
    except Exception as e:
        raise CustomException(e,sys)


def model_evaluation(X_train,X_test,y_train,y_test,models:dict,parameters , load_result_into_csv:bool = True):
    try:
        path = os.path.join('artifacts','Result.csv')
        result_df = pd.DataFrame(columns = ['Algorithm','Test_Accuracy','MSE'])
        report = {}
        for obj, algos in (models.items()):
            algos.fit(X_train,y_train)
            y_test_pred = algos.predict(X_test)
            y_train_pred = algos.predict(X_train)
            train_score = accuracy_score(y_train,y_train_pred)
            test_score = accuracy_score(y_test,y_test_pred)
            MSE = mean_squared_error(y_test,y_test_pred)
            logger.info(' Algorithm - {}\nAccuracy - {}'.format(algos,test_score))
            report[obj] = test_score
            if load_result_into_csv:
                result_df.loc[len(result_df)] = [algos,test_score, MSE]


        # Create a path before dump the .csv file
        os.makedirs(os.path.dirname(path),exist_ok=True)
        result_df.to_csv(path , index=False,header=True)
        logger.info('Result.csv has been Dumped - {}'.format(path))
        return report

    except Exception as e:
        raise CustomException(e,sys)
