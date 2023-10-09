import sys
import os

import pandas as pd
import numpy as np
import dill

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
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


def model_evaluation(X_train,X_test,y_train,y_test,models:dict,parameters):
    try:
        report = {}
        for obj, algos in (models.items()):

            clf = GridSearchCV(estimator= algos , param_grid= parameters[obj], scoring='accuracy',cv=5)
            clf.fit(X_train,y_train)
            best_params = clf.best_params_
            algos.set_params(**best_params)
            logger.info('Best parameters-{}\nset successfully in {}'.format(best_params,algos))
            algos.fit(X_train,y_train)
            y_test_pred = algos.predict(X_test)
            test_model_score = r2_score(y_test,y_test_pred)
            logger.info('{} shows {} r2 score'.format(algos,test_model_score))
            report[obj] = test_model_score
        return report

    except Exception as e:
        raise CustomException(e,sys)
