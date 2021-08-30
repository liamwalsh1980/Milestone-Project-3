import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# MongoDB stores its data in a JSON like format called BSON
# In order to find documents from MongoDB later, to render ObjectId
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# Create a variable and an instance of Flask

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Configuration to grab the database name
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Configure the actual connection string which is the Mongo URI
app.secret_key = os.environ.get("SECRET_KEY")
# Graps the secret_key

mongo = PyMongo(app)
# An instance of PyMongo using a Constructor method to add 'app' from above


@app.route("/")
@app.route("/index")
def index():
    index = mongo.db.films.find()
    return render_template("index.html", index=index)


@app.route("/get_films")
def get_films():
    films = mongo.db.films.find()
    # The first 'films' is the template films.html
    # The second 'films is the variable name above
    return render_template("films.html", films=films)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username already exists a message is displayed to the user
        if existing_user:
            flash("Username already exists, please try again")
            # Takes the user back to the signup form to try again
            return redirect(url_for("signup"))

        # Else statement using a dictionary
        signup = {
            # Username in parentheses is from the name attr in signup template
            "username": request.form.get("username").lower(),
            # Password in parentheses is from the name attr in signup template
            # Werkzeug security helper used below
            "password": generate_password_hash(request.form.get("password"))
        }
        # Calling the function using the insert_one method
        mongo.db.users.insert_one(signup)

        # Put the new user into 'session' cookie
        session['user'] = request.form.get("username").lower()
        flash("Signup is successful, Welcome to FilmZone")
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# During development we want debug=True to see any potential errors appear
# This will be updated to debug=False when deploying site and submitted project
