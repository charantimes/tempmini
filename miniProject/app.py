from flask import Flask, request, render_template
from lib import analyze
import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/help")
def Help():
    return render_template("Help.html")

@app.route("/analyze", methods = ("GET", "POST"))
def ana():
    if request.method == 'POST':
        message = request.form.get('text')
        report = analyze(
            message
        )
        
        print(message, report)
        return render_template("Analayze.html", report = report, piechart_path = "static/images/report.jpg")
   
    return render_template("Analayze.html")

if __name__ == "__main__":
    app.run(debug = True)