
from flask import abort, jsonify, request
from glide_api.app import app
from glide_api.department_resource.serializer import Department


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
    expand = request.args.get("expand", None)

    if expand:
        expand_level = len(expand.split('.'))
        department = Department()
        departments = department.get_all(offset, limit, expand_level)
    else:
        department = Department()
        departments = department.get_all(offset, limit)

    return jsonify({"departments": departments})


@app.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    # TODO: RECHECK PLEASE THE WAY IM HANDLING THE VARIABLES
    expand = request.args.get("expand", None)
    department = Department()
    item = department.get_item(department_id, department.data)
    if expand:
        expand = expand.split('.')
        expand_level = len(expand)
        department = Department()
        for each in range(expand_level):
            item = department.handle_relationship(
                item, expand[0], department.data)

    if item is None:
        abort(404)

    return jsonify({'departament': item})
