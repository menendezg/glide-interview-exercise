from flask import (abort, jsonify, request)
from glide_api.app import app
from glide_api.utils import json_reader

departments = json_reader(file="departments.json", folder="departments/data")


class Department:
    @staticmethod
    def get_departments(limit=100, offset=0):
        """
        Get departments with limit and offset
        :param limit: max number of records returned
        :param offset: index at wich to start
        :return list of departments
        """
        return departments[offset: (offset + limit)]


@app.route("/departments")
def get_departments():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    department = Department()
    return jsonify({"offices": department.get_departments(limit, offset)})
    return jsonify({"departments": departments})


@app.route("/departments/<int:department_id>", methods=["GET"])
def get_department(departament_id):
    department = [
        department for department in departments if departments["id"] == departament_id
    ]
    if len(department) == 0:
        abort(404)
    return jsonify({"departament": department[0]})
