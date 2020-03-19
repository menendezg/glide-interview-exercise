"""
Before sent the exercise I should check this validate function to something
more reusable.

"""

from flask import abort, jsonify, request

from glide_api.app import app
from glide_api.departments.department import Department


def validate_param(value, _type):
    if type(value) == _type:
        return value


def validate_given_word(value, word):
    if word in value:
        return value


@app.route('/departments', methods=['GET'])
def get_departments():
    offset = validate_param(int(request.args.get('offset', '0')), int)
    limit = validate_param(int(request.args.get('limit', '100')), int)
    expand = validate_given_word(validate_param(request.args.get("expand",
                                                                 None), str),
                                 'superdepartment')
    if expand:
        expand_level = len(expand.split('.'))
        department = Department(expand_level)
    else:
        department = Department()
    return jsonify({"departments":
                    department.get_departments(
                        limit,
                        offset)})


@app.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    expand = request.args.get("expand", None)
    department = Department()
    departments = [
        item for item in department.departments
        if item['id'] == department_id
    ]
    if len(departments) == 0:
        abort(404)
    if expand:
        expand_level = len(expand.split('.'))
        department = Department(expand_level)
        return jsonify({'departament': department.get_department(departments[0])})

    return jsonify({'departament': departments[0]})
