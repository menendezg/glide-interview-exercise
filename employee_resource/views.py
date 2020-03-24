from flask import abort, jsonify, request
from glide_api.api.api import ApiBigCorp
from glide_api.app import app
from glide_api.departments.department import Department
from glide_api.utils import json_reader

# https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit=10&offset=0
# we load data in memory
# offices = json_reader(file="offices.json", folder="offices/data")


class Employee:
    def __init__(self, expand_level=None):
        self.departments = json_reader(
            file='departments.json', folder='departments/data'
        )
        self.expand_level = expand_level

    def get_super_department(self, _id):
        for dep in self.departments:
            if dep['id'] == _id:
                return dep

    def get_all_values(self, value, key):
        """
        Recursively search for ids of superdepartments
        """
        if isinstance(value, dict):
            value = value.copy()
            super_department = value[key]
            if super_department is None:
                return value
            if isinstance(super_department, dict):
                value[key] = self.get_all_values(
                    super_department
                )

            if isinstance(super_department, int):
                value[key] = self.get_super_department(
                    super_department
                )
                return value
        if isinstance(value, list):
            return [self.get_all_values(item, key) for item in value]
        if isinstance(value, int):
            return self.get_super_department(value)
        return value

    def get_employee(self, limit=100, offset=0):
        api = ApiBigCorp()
        payload = {'limit': limit,
                   'offset': offset}

        r = api.get(payload)
        # in r i Have the list with json objects.
        # i have to trowh this in the departments to get all departments
        for each in range(self.expand_level):
            r = self.get_all_values(r, 'department')
        return r


@app.route("/employees", methods=["GET"])
def get_employee():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    employee = Employee(1)
    return jsonify({"employee": employee.get_employee(limit, offset)})


# @app.route("/employees/<int:office_id>", methods=["GET"])
# def get_office_by_id(office_id):
#     office = [office for office in offices if office["id"] == office_id]
#     if len(office) == 0:
#         abort(404)
#     return jsonify({"office": office[0]})
