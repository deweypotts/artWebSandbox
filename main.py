from flask import Flask, redirect, url_for, request, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/home") # 
def home():
    return render_template("home.html")

@app.route("/login") # 
def login():
    return "This is the login page!" #



if __name__ == "__main__":
    app.run(debug=True)