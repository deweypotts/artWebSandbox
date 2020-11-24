from flask import Flask, redirect, url_for, request, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/") # 
def home():
    return render_template("home.html")

@app.route("/home") # 
def login():
    return render_template("home.html")
    
@app.route("/schedule") # 
def logout():
    return render_template("schedule.html")

@app.route("/logout") # 
def logout():
    return render_template("logout.html")

@app.route("/login") # 
def logout():
    return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True)