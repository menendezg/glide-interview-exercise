from flask import jsonify, request
from glide_api.app import app
from glide_api.employee_resource.serializer import Employee
from glide_api.utils import get_keywords


@app.route("/employees", methods=["GET"])
def get_employee():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    expand_params = request.args.getlist('expand')
    key_words = get_keywords(expand_params)

    employee = Employee()

    employees = employee.get_employee(limit, offset, key_words)
    return jsonify(employees)


@app.route("/employees/<int:office_id>", methods=["GET"])
def get_employee_by_id(office_id):
    employee = Employee()
    return jsonify(employee.get_employee_by_id(office_id))
