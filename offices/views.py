from flask import abort, jsonify
from glide_api.app import app
from glide_api.utils import json_reader

offices = json_reader(file="offices.json", folder="offices/data")


@app.route("/offices", methods=["GET"])
def get_offices():
    return jsonify({"offices": offices})


@app.route("/offices/<int:office_id>", methods=["GET"])
def get_office_by_id(office_id):
    office = [office for office in offices if office["id"] == office_id]
    if len(office) == 0:
        abort(404)
    return jsonify({"office": office[0]})
