from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_json = Blueprint(name="blueprint_json", import_name=__name__)


# add view function to the blueprint
@blueprint_json.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_json."}
    return jsonify(output)
