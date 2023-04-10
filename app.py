from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('knn_on_dbscan.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        input_value = float(request.form['input_value'])
        rpm=float(request.form['rpm'])
        time_gap=float(request.form['time_gap'])
        
        prediction=model.predict([[input_value,rpm,time_gap]])
        # output=round(prediction[0],2)
        if prediction==0:
            return render_template('index.html',prediction_text="Drone is Fit")
        else:
            return render_template('index.html',prediction_text="Drone will crash{}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

