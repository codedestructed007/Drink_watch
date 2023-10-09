from flask import Flask , render_template
from datetime import  datetime

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    render_template('templates/html pages/home.html', current_time =datetime.utcnow().date())
