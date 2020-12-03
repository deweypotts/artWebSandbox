from flask import Flask, redirect, url_for, request, render_template, request, session, flash, jsonify
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
    connection = connect()
    create_tables(connection)
    events = get_all_events(connection)
    output = {}
    for event in events:
        output[event[0]] = {
            "name": event[1],
            "artist": event[2],
            "date": event[3]
        }
    # for event in events:
    #     print (f"Event Name: {event[1]} Artist: {event[2]} Date: {event[3]}")
    return render_template("schedule.html", context=output)


@app.route("/api/schedule", methods=["GET"])  #
def api_schedule():
    connection = connect()
    create_tables(connection)
    events = get_all_events(connection)
    output = {}
    for event in events:
        output[event[0]] = {
            "name": event[1],
            "artist": event[2],
            "date": event[3]
        }
    print(output)
   #         print(f"Event Name: {event[1]} Artist: {event[2]} Date: {event[3]}")
    return jsonify(output)



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

@app.route("/api/createevent", methods=["POST"])
def api_create_event():
    connection = connect()
    input = request.json
    add_event(connection, input['name'], input['artist'], input['date'])

    return jsonify({'OK': '200'})

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
    app.run(debug=True, port=5050)