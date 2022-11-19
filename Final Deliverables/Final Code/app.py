
from flask import Flask, render_template, request, redirect, url_for
import numpy,pickle


app = Flask(__name__)




@app.route('/')
def index():
    return render_template("home.html")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/predict')
def predict():
    return render_template("prediction.html")
@app.route('/result',methods=['POST','GET'])
def result():
    age = float(request.form['age'])
    haemoglobin = float(request.form['haemoglobin'])
    redbloodcells = int(request.form['redbloodcells'])
    specificgravity = float(request.form['specificgravity'])
    albumin = float(request.form['albumin'])
    serumcreatinine = float(request.form['serumcreatinine'])
    hypertension = int(request.form['hypertension'])
    sodium= float(request.form['sodium'])
    bloodpressure = float(request.form['bloodpressure'])
    whitebloodcellcount = float(request.form['whitebloodcellcount'])


    x = numpy.array([age,haemoglobin, redbloodcells, specificgravity, albumin, serumcreatinine, hypertension, sodium, bloodpressure, whitebloodcellcount]).reshape(1, -1)

    model = pickle.load(open(r'F:\ML Kidney Disease\Chronic Kidney Disease\models\EDCKDML.pkl', 'rb'))
    Y_pred = model.predict(x)

    return render_template("result.html", y=Y_pred)



if __name__ == '__main__':
 app.run(debug=True)