from flask import Flask , render_template , request
from datetime import  datetime

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return  render_template('home.html', current_time =datetime.utcnow().date())


@app.route('/predict', methods=['POST'])
def Predict():
    if request.method == 'POST':
        # Access the submitted form data using the 'name' attributes
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
    print(f"Age: {age}, Weight: {weight}, Sight Left: {sight_left}, Sight Right: {sight_right}")

    return render_template('prediction.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True,port = 5050)