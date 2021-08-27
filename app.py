import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# Create a variable and an instance of Flask


@app.route("/")
def hello():
    return "Hello World... again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# During development we want debug=True to see any potential errors appear
# This will be updated to debug=False when deploying site and submitted project
