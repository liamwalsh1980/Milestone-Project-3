import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# MongoDB stores its data in a JSON like format called BSON
# In order to find documents from MongoDB later, to render ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# During development we want debug=True to see any potential errors appear
# This will be updated to debug=False when deploying site and submitted project
