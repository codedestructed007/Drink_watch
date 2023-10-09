from flask import Flask , render_template , request
from datetime import  datetime
from src.pipeline.predict_pipeline import CustomData, PredictPineline
app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return  render_template('home.html', current_time =datetime.utcnow().date())


@app.route('/predict', methods=['POST'])
def Predict():
    # If method is 'POST'
    if request.method == 'POST':

        # Access the submitted form data using the 'name' attributes
        sex = request.form.get('sex')
        age = request.form.get('age')
        weight = request.form.get('weight')
        sight_left = request.form.get('sight_left')
        sight_right = request.form.get('sight_right')
        hear_left = request.form.get('hear_left')
        DBP = request.form.get('DBP')
        BLDS = request.form.get('BLDS')
        HDL_chole = request.form.get('HDL_chole')
        LDL_chole = request.form.get('LDL_chole')
        triglyceride = request.form.get('triglyceride')
        urine_protein = request.form.get('urine_protein')
        serum_creatinine = request.form.get('serum_creatinine')
        SGOT_AST = request.form.get('SGOT_AST')
        SGOT_ALT = request.form.get('SGOT_ALT')
        gamma_GTP = request.form.get('gamma_GTP')
        SMK_stat_type_cd = request.form.get('SMK_stat_type_cd')
        data = CustomData(sex,age,weight,sight_left,sight_right,hear_left,DBP,BLDS,HDL_chole,LDL_chole,triglyceride, urine_protein, serum_creatinine, SGOT_AST, SGOT_ALT, gamma_GTP, SMK_stat_type_cd)
        User_input = data.get_data_as_dataFrame()
        # Initiating PredictPipeline
        predict_pipeline =PredictPineline()

        prediction = predict_pipeline.predict(User_input)
        result = {
            'prediction' : prediction
        }
        return  render_template('result.html',result=result)
    # With other methods
    else:
        return render_template('home.html',)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True,port = 5050)