
import os
import sys
import pandas as pd

from dataclasses import dataclass
from src.utils import  save_object


from sklearn.preprocessing import LabelEncoder

from src.exception import CustomException
from src.logger import logger



@dataclass
class DataTransformationCofig:
    labelEncoder_obj_file_path =os.path.join('artifacts','label_encoder.pkl')
    transformed_train_df_file_path = os.path.join('artifacts/Transformed_datasets','train_df.csv')
    transformed_test_df_file_path = os.path.join('artifacts/Transformed_datasets','test_df.csv')
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationCofig()

    def remove_columns(self,df):
        try:
            df.drop(['height'],axis=1,inplace = True)

            df.drop(['hear_right','waistline','tot_chole','hemoglobin'],axis=1,inplace=True)

            df.drop(['SBP'],axis=1,inplace=True)
            print(type(df))
            return df
        except Exception as e:
            raise CustomException(e,sys)

    def remove_outliers(self, df):
        try:
            # Remove rows where 'weight' >= 120
            df.drop(df[df['weight'] >= 120].index,inplace = True)

            # Remove rows where 'sight_right' >= 2
            logger.info('Removing Outliers process start--')

            df.drop(df['sight_left'].loc[df['sight_left'] >=2].index ,inplace =True)

            df.drop(df['sight_right'].loc[df['sight_right'] >=2].index,inplace = True)

            df.drop(df['DBP'].loc[df['DBP'] > 120].index, inplace=True)

            df.drop(df['BLDS'].loc[df['BLDS'] > 350].index, inplace =True)

            max_value = df['LDL_chole'].loc[df['LDL_chole'].values.max()]

            df.drop(df['LDL_chole'].loc[df['LDL_chole'] == max_value].index, inplace = True)

            df.drop(df['HDL_chole'].loc[df['HDL_chole'] == max_value].index, inplace = True)

            df.drop(df.nlargest(4,'triglyceride').index,inplace = True)

            df.drop(df['serum_creatinine'].loc[df['serum_creatinine'] >=8].index, inplace = True)


            df.drop(df['serum_creatinine'].loc[df['serum_creatinine'] >=8].index, inplace = True)

            df.drop(df['gamma_GTP'].loc[df['gamma_GTP'] > 600].index ,inplace = True)

            logger.info('Outliers have been removed completely')
            return df


        except Exception as e:
            raise CustomException(e,sys)

    def label_encoding(self, df, column_1st = 'sex',column_2nd = 'DRK_YN'):
        try:
            encoder = LabelEncoder()
            df[column_1st] = encoder.fit_transform(df[column_1st])
            df[column_2nd] = encoder.fit_transform(df[column_2nd])

            save_object(
                file_path = self.data_transformation_config.labelEncoder_obj_file_path,
                obj = encoder
            )


            return df


        except Exception as e:
            raise CustomException(e,sys)

    def data_transformation(self, train_path,test_path):
        try:

            train_df = pd.read_csv(train_path)
            logger.info('Train data loaded successfully')
            print(type(train_df))
            # remove columns in train dataset
            train_df = self.remove_columns(train_df)
            logger.info('Columns are removed successfully')
            # remove outliers for train dataset


            train_df = self.remove_outliers(train_df)
            logger.info('Trainset has been filtered with Outliers')
            # label encoding on train dataset


            train_df = self.label_encoding(train_df)
            logger.info('Encoding finished on train dataset successfully')

            test_df = pd.read_csv(test_path)
            logger.info('Test data loaded sucessfully')
            # remove columns in test dataset
            test_df = self.remove_columns(test_df)
            logger.info('Columns are removed successfully')
            #remove outliers for test dataset
            test_df = self.remove_outliers(test_df)
            logger.info('Testset has been filtered with Outliers')
            #label encoding on test dataset
            test_df = self.label_encoding(test_df)
            logger.info('Encoding finished on test dataset successfully ')

            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_df_file_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_test_df_file_path),exist_ok=True)

            train_df.to_csv(self.data_transformation_config.transformed_train_df_file_path,index=False,header=True)
            test_df.to_csv(self.data_transformation_config.transformed_test_df_file_path,index=False,header = True)

        except Exception as e:
            raise CustomException(e,sys)








