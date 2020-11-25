from flask import Flask, redirect, url_for, request, render_template, request, session, flash
from datetime import timedelta
import sqlite3


# SQlite commands and database def
CREATE_EVENTS_TABLE = "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, eventName TEXT, artistName TEXT, date TEXT);"
ADD_EVENT = "INSERT INTO events (eventName, artistName, date) VALUES(?,?,?);"
GET_ALL_EVENTS = "SELECT * FROM events;"

def connect():
    return sqlite3.connect("events.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_EVENTS_TABLE)

def add_event(connection, eventName, artistName, date):
    with connection:
        return connection.execute(ADD_EVENT, (eventName, artistName, date))

def get_all_events(connection):
    with connection:
        return connection.execute(GET_ALL_EVENTS).fetchall()

# Website pages
app = Flask(__name__)
app.secret_key = "this_is_a_super_secret_key"

@app.route("/") # 
def home():
    return render_template("home.html")
    
@app.route("/schedule", methods = ["GET"]) # 
def schedule():
    return render_template("schedule.html")

@app.route("/createevent", methods=["POST", "GET"]) # 
def createEvent():
    if request.method == "POST":
        connection = connect()
        create_tables(connection)
        add_event(connection, request.form["eventName"], request.form["artistName"], request.form["date"])
        
        flash("Your event has been created!")
    
        return redirect(url_for("createEvent"))
    else:
        return render_template("createevent.html")

@app.route("/logout") # 
def logout():
    return render_template("logout.html")

@app.route("/login") # 
def login():
    return render_template("login.html")

@app.route("/test") # 
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)