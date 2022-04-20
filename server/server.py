from flask import Flask, request
from server import model

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Server is online and true"


@app.route("/<id>", methods=["GET"])
def get_id(id):
    print("request: ", request)
    return model.risk_model(id)
