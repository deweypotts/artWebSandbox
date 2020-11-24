from flask import Flask, redirect, url_for, request, render_template, request, session, flash
from datetime import timedelta
import sqlite3

#define connection and cursor
connection = sqlite3.connect('concert_schedule.db')

#cursor
c = connection.cursor()

# create table, only need to create once, so commenting out
# c.execute("""CREATE TABLE concert_schedule (
#     artistName text,
#     date text,
#     cost integer
#     )""")

c.execute("INSERT INTO concert_schedule VALUES('Jack Johnson', 'Nov 24th, 2021', '70')")
c.execute("INSERT INTO concert_schedule VALUES('The White Stripes', 'Oct 12th, 2020', '90')")

c.execute("SELECT * FROM concert_schedule WHERE artistName='The White Stripes'")

connection.commit()

c.execute("SELECT * FROM concert_schedule WHERE artistName='The White Stripes'")

connection.commit()

print(c.fetchmany(3))

connection.close()

# app = Flask(__name__)

# @app.route("/home") # 
# def home():
#     return render_template("home.html")
    
# @app.route("/schedule") # 
# def schedule():
#     return render_template("schedule.html")

# @app.route("/logout") # 
# def logout():
#     return render_template("logout.html")

# @app.route("/login") # 
# def login():
#     return render_template("login.html")





# if __name__ == "__main__":
#     app.run(debug=True)