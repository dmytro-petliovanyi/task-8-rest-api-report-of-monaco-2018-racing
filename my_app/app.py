from flask import Flask, jsonify
import sys

# load modules
from my_app.blueprints.blueprint_json import blueprint_json
from my_app.blueprints.blueprint_xml import blueprint_xml

# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_json, url_prefix="/api/v1/path_for_blueprint_json")
app.register_blueprint(blueprint_xml, url_prefix="/api/v1/path_for_blueprint_xml")
