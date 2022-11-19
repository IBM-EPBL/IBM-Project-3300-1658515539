from flask import Flask, render_template,request
import numpy,pickle

import requests

API_KEY = "QhoFbRSt_fE2DqkxtoBpww_NplmFAOS11vcwayKLx38h"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

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


    A=[[age,haemoglobin, redbloodcells, specificgravity, albumin, serumcreatinine, hypertension, sodium, bloodpressure, whitebloodcellcount]]

    payload_scoring = {
        "input_data": [{"field": [['age','haemoglobin','redbloodcells','specificgravity','albumin','serumcreatinine','hypertension','sodium','bloodpressure','whitebloodcellcount']], "values": A}]}

    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6ce12547-4be9-450c-af6b-9cefc9b58465/predictions?version=2022-11-17',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})

    print("Scoring response")
    print(response_scoring.json())

    predictions = response_scoring.json()
    pred = predictions['predictions'][0]['values'][0][0]
    print(pred)

    return render_template("result.html", y=pred)




if __name__ == '__main__':
 app.run(debug=True)