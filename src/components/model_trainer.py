import os
import sys
import pandas as pd
import  numpy as np
import warnings
warnings.filterwarnings('ignore')


from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import  LogisticRegression
from sklearn.ensemble import  AdaBoostClassifier , RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import  GridSearchCV



from src.utils import  model_evaluation
from dataclasses import dataclass
from src.logger import logger
from src.exception import CustomException


from src.utils import  save_object

@dataclass
class ModelTrainerConfig:
    model_file_obj_path =os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,transformed_train_df_path:str, transformed_test_df_path:str) -> dict:
        try:

            train_df  = pd.read_csv(transformed_train_df_path)
            test_df = pd.read_csv(transformed_test_df_path)

            logger.info('Transformed Train and Test datasets are loaded successfully')
            # Splitting the train and test dataset
            X_train,y_train = train_df.iloc[:,:-1], train_df.iloc[:,-1]
            X_test, y_test = test_df.iloc[:,:-1] , test_df.iloc[:,-1]
            logger.info('Splitting in input and output dataset is successful')

            classifiers = {
                'SVC': SVC(),
                'DecisionTreeClassifier': DecisionTreeClassifier(),
                'AdaBoostClassifier': AdaBoostClassifier(),
                'RandomForestClassifier': RandomForestClassifier(),
                'KNeighborsClassifier': KNeighborsClassifier(),
                'LogisticRegression': LogisticRegression(max_iter=1000),
                'XGBClassifier' : XGBClassifier()
            }

            parameters = {
                'SVC' : {
                    'C' : [0.7 , 1.0 , 1.3],
                    'kernel' : ['linear','poly','rbf'],
                    'gamma' : ['scale','auto']
                },
                'DecisionTreeClassifier' : {
                    'criterion' : ['gini','entropy'],
                    'splitter' : ['best','random'],
                    'max_depth' : [1,3,5,8]
                },
                'AdaBoostClassifier' : {
                    'estimator' : [50,80,100,120],
                    'learning_rate' : [0.7 , 1.0 , 1.3],
                    'algorithm' : ['SAMME','SAMME.R']
                },
                'RandomForestClassifier' : {
                    'n_estimators' : [80,100,120],
                    'criterion' : ['gini','entropy','log_loss'],
                    'max_depth' : [3,5,7,8,None]
                },
                'KNeighborsClassifier' : {
                    'n_neighbors' : [2,3,5,6,7],
                    'weights' : ['uniform','distance'],
                    'algorithm' : ['auto','ball_tree','kd_tree']
                },
                'LogisticRegression' : {
                    'penalty' : ['l1','l2','elasticnet'],
                    'C' : [0.6,0.9,1,1.3],

                },
                'XGBClassifier' : {
                    'n_estimators' : [1,2,4,6],
                    'max_depth' : [1,3,4,5],
                    'learning_rate' : [0.7 , 1.0, 1.3]
                }
            }
            try:
                model_report: dict = model_evaluation(X_train = X_train,X_test = X_test,y_train = y_train,y_test=y_test,models = classifiers, parameters = parameters)
                logger.info('All models are successfully implemented')

                # Best model score value

                # Here best_score is accuracy_score not R2_score

                best_score = max(sorted(model_report.values()))
                index_of_mse = list(model_report.values()).index(best_score)

                best_model_name = list(model_report.keys())[index_of_mse]

                model = classifiers[best_model_name]
                logger.info('Best model is generated')

                ## Now we have the best model ,Now apply Hypertuning on best parameter
                params = parameters[best_model_name]
                clf = GridSearchCV(model , params, scoring='accuracy',cv= 5)
                clf.fit(X_train,y_train)
                best_parameters = clf.best_params_

                model_best_parameters = {
                    'model_name' : model,
                    'best_parameter' : best_parameters
                }

                logger.info('Best model has been saved')
            except Exception as e:
                raise CustomException(e,sys)

            # Saving best model
            save_object(
                file_path=self.model_trainer_config.model_file_obj_path,
                obj=model_best_parameters
            )


            return best_score , best_model_name


        except Exception as e:
            raise CustomException(e,sys)


