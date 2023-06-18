import os

from flask import Flask
from pe_on_flask.api import api
from pe_on_flask.api.config import config

config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)
app.config.from_object(config[config_name])
# blueprintをアプリケーションに登録
app.register_blueprint(api)
