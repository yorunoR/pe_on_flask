from flask import Blueprint, jsonify, request
from pe_on_flask.api import executor

api = Blueprint("api", __name__)


@api.get("/")
def ping():
    return jsonify({"ping": "pong"}), 200


@api.post("/execute")
def execute():
    return executor.execute(request)
