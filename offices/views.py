from flask import abort, jsonify, request
from glide_api.app import app
from glide_api.utils import json_reader

# we load data in memory
offices = json_reader(file="offices.json", folder="offices/data")


class Office:
    @staticmethod
    def get_offices(limit=100, offset=0):
        return offices[offset: (offset + limit)]


@app.route("/offices", methods=["GET"])
def get_offices():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    office = Office()
    return jsonify({"offices": office.get_offices(limit, offset)})


@app.route("/offices/<int:office_id>", methods=["GET"])
def get_office_by_id(office_id):
    office = [office for office in offices if office["id"] == office_id]
    if len(office) == 0:
        abort(404)
    return jsonify({"office": office[0]})
