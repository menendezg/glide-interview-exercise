from flask import abort, jsonify, request

from glide_api.app import app
from glide_api.utils import json_reader

departments = json_reader(file="departments.json", folder="departments/data")


class Department:
    def get_super_department(self, departments, _id):
        for each in departments:
            if each["superdepartment"] == _id:
                return each

    def get_departments(self, limit=100, offset=0, superdepartment=None):

        """
        Get departments with limit and offset
        :param limit: max number of records returned
        :param offset: index at wich to start
        :param superdepartment: superdepartment id
        :return list of departments
        """
        if superdepartment is not None:
            for department in departments:
                if department["superdepartment"] is not None:
                    # problem detected here.

                    # i'm mutating the list. If I mutating the list
                    # this are increasing the amount of superdepartments
                    # I should create another list and that list
                    # and that new list pass to the function

                    # possible way to resolve
                    # len of superdepartment keyword sent
                    # after make range with that number
                    # to make a recursive function itereate n times.
                    _id_super_department = department["superdepartment"]
                    department["superdepartment"] = self.get_super_department(
                        departments, _id_super_department
                    )

        return departments[offset: (offset + limit)]


@app.route("/departments")
def get_departments():
    offset = int(request.args.get("offset", "0"))
    limit = int(request.args.get("limit", "100"))
    super_department = request.args.get("expand", "")

    department = Department()
    return jsonify(
        {"departments": department.get_departments(limit, offset, super_department)}
    )


@app.route("/departments/<int:department_id>", methods=["GET"])
def get_department(departament_id):
    department = [
        department for department in departments if departments["id"] == departament_id
    ]
    if len(department) == 0:
        abort(404)
    return jsonify({"departament": department[0]})
