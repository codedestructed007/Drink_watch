import pandas as pd

from src.utils import load_object
import sys

from src.logger import logger


class PredictPineline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            model_and_parameters= load_object(file_path=model_path)
            model , best_params= model_and_parameters['model_name'] , model_and_parameters['best_parameter']
            hyper_tuned_model = model.set_params(**best_params)
            prediction = hyper_tuned_model.predict(features)
            return prediction
        except Exception as e:
            raise RecursionError(e,sys)

class CustomData:
    def __init__(self,
                 sex : int,
                 age : int,
                 weight : int,
                 sight_left : float,
                 sight_right : float,
                 hear_left : float,
                 DBP : float,
                 BLDS : float,
                 HDL_chole : float,
                 LDL_chole : float,
                 triglyceride : float,
                 urine_protein : float,
                 serum_creatinine : float,
                 SGOT_AST : float,
                 SGOT_ALT : float,
                 # gamma_GTP : float,
                 SMK_stat_type_cd : float):
        self.sex =sex
        self.age = age
        self.weight = weight
        self.sight_left = sight_left
        self.sight_right = sight_right
        self.hear_left = hear_left
        self.DBP = DBP
        self.BLDS = BLDS
        self.HDL_chole = HDL_chole
        self.LDL_chole = LDL_chole
        self.triglyceride = triglyceride
        self.urine_protein = urine_protein
        self.serum_creatinine = serum_creatinine
        self.SGOT_AST = SGOT_AST
        self.SGOT_ALT = SGOT_ALT
        self.SMK_stat_type_cd = SMK_stat_type_cd
    def get_data_as_dataFrame(self):
        try:
            feautres_dict = {
                'sex' : [self.sex],
                'age' : [self.age],
                'weight' : [self.weight],
                'sight_left' : [self.sight_left],
                'sight_right' : [self.sight_right],
                'hear_left' : [self.hear_left],
                'DBP' : [self.DBP],
                'BLDS' : [self.BLDS],
                'HDL_chole' : [self.HDL_chole],
                'LDL_chole' : [self.LDL_chole],
                'triglyceride' : [self.triglyceride],
                'urine_protein' : [self.urine_protein],
                'serum_creatinine' : [self.serum_creatinine],
                'SGOT_AST' : [self.SGOT_AST],
                'SGOT_ALT' : [self.SGOT_ALT],

                'SMK_stat_type_cd' : [self.SMK_stat_type_cd]
            }
            logger.info('DataFrame for input has been prepared')
            return pd.DataFrame(feautres_dict)
        except Exception as e:
            raise CustomData(e,sys)







