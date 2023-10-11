import os
from flask import Flask , render_template , request , redirect ,url_for
import csv
import sys
from datetime import  datetime
from src.pipeline.predict_pipeline import CustomData, PredictPineline
from src.exception import  CustomException
from src.utils import load_object
from src.logger import logger
app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return  render_template('home.html', current_time =datetime.utcnow().date())


@app.route('/predict', methods=['POST'])
def Predict():
    try:
    # If method is 'POST'
        if request.method == 'POST':

            # Access the submitted form data using the 'name' attributes
            sex = request.form.get('sex')
            if sex.lower().startswith('m'):
                sex = 1
            else:
                sex = 0
            try:
                age = int(request.form.get('age'))
                weight = int(request.form.get('weight'))
            except Exception as e:
                raise CustomException(e,sys)

            try:

                sight_left = float(request.form.get('sight_left'))
                sight_right = float(request.form.get('sight_right'))
                hear_left = float(request.form.get('hear_left'))
                DBP = float(request.form.get('DBP'))
                BLDS = float(request.form.get('BLDS'))
                HDL_chole = float(request.form.get('HDL_chole'))
                LDL_chole = float(request.form.get('LDL_chole'))
                triglyceride = float(request.form.get('triglyceride'))
                urine_protein = float(request.form.get('urine_protein'))
                serum_creatinine = float(request.form.get('serum_creatinine'))
                SGOT_AST = float(request.form.get('SGOT_AST'))
                SGOT_ALT = float(request.form.get('SGOT_ALT'))
                SMK_stat_type_cd = float(request.form.get('SMK_stat_type_cd'))


            except Exception as e:
                raise CustomException(e,sys)


            data = CustomData(sex,age,weight,sight_left,sight_right,hear_left,DBP,BLDS,HDL_chole,LDL_chole,triglyceride, urine_protein, serum_creatinine, SGOT_AST, SGOT_ALT, SMK_stat_type_cd)
            User_input = data.get_data_as_dataFrame()
            logger.info('Dataframe has been created successfully')
            # Initiating PredictPipeline
            predict_pipeline =PredictPineline()

            prediction = predict_pipeline.predict(User_input)

            # Getting in integer
            prediction = prediction[0]
            print(prediction)
            return  render_template('result.html',prediction=prediction)
        # With other methods
        else:
            return render_template('home.html',)
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/train')
def train_model():
    os.system('python model_training.py')
    csv_data = []
    with open('artifacts/Result.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_data.append(row)
    return render_template('score.html', csv_data = csv_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True,port = 5050)
