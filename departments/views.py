from flask import (abort, jsonify)
from glide_api.app import app
from glide_api.utils import json_reader

departments = json_reader(file="departments.json", folder='departments/data')


@app.route("/departments")
def get_departments():
    return jsonify({"departments": departments})


@app.route("/departments/<int:department_id>", methods=["GET"])
def get_department(departament_id):
    department = [
        department for department in departments if
        departments["id"] == departament_id
    ]
    if len(department) == 0:
        abort(404)
    return jsonify({"departament": department[0]})
