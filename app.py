from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("ipl_ridge.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/result", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
    	bat_team = int(request.form['bat_team'])
    	bowl_team = int(request.form['bowl_team'])
    	runs = int(request.form['runs'])
    	wickets = int(request.form['wickets'])
    	overs = int(request.form['overs'])
    	runs_last_5 = int(request.form['runs_last_5'])
    	wickets_last_5 = int(request.form['wickets_last_5'])
    	prediction = model.predict([[bat_team,bowl_team,runs,wickets,overs,runs_last_5,wickets_last_5]])
    	output = round(prediction[0])
    	return render_template('index.html',prediction=output)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


