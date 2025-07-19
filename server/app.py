existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

app = Flask(__name__)

#Setting up ‘/’ route for the base URL
@app.route("/")
def index():
    return "Welcome to Flatiron Cars"

#Setting up '/model' route
@app.route("/<string:model>")
def carmodel(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"
    