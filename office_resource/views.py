from flask import abort, jsonify, request
from glide_api.app import app
from glide_api.office_resource.serializer import Office


@app.route("/offices", methods=["GET"])
def get_offices():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    office = Office()
    return jsonify({"offices": office.get_all(offset, limit)})


@app.route("/offices/<int:office_id>", methods=["GET"])
def get_office_by_id(office_id):
    office_handler = Office()
    office = office_handler.get_item(office_id, office_handler.data)
    if office is None:
        abort(404)
    return jsonify({"office": office})
