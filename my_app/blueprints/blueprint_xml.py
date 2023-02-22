from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_xml = Blueprint(name="blueprint_xml", import_name=__name__)


# add view function to the blueprint
@blueprint_xml.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_xml."}
    return jsonify(output)

