from flask import abort, jsonify, request
from glide_api.app import app
from glide_api.office_resource.model import Office
from glide_api.resources.businessresource import BusinessResource


@app.route("/offices", methods=["GET"])
def get_offices():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    handler = BusinessResource()
    return jsonify({"offices": handler.get_all(Office, offset, limit)})


@app.route("/offices/<int:office_id>", methods=["GET"])
def get_office_by_id(office_id):
    handler = BusinessResource()
    office = handler.get_item(office_id, Office.DATA)
    if office is None:
        abort(404)
    return jsonify({"office": office})
