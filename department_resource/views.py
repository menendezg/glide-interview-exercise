from flask import abort, jsonify, request
from glide_api.app import app
from glide_api.department_resource.model import Department
from glide_api.resources.businessresource import BusinessResource
from glide_api.utils import get_keywords


@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message']})


def invalid_keyword(key_words):
    valid_keys = ['superdepartment']
    for keys in key_words:
        for key in keys:
            if key in valid_keys:
                continue
            else:
                return True


@app.route('/departments', methods=['GET'])
def get_departments():
    offset = int(request.args.get('offset', '0'))
    limit = int(request.args.get('limit', '100'))
    key_words = get_keywords(request.args.getlist("expand", None))
    if invalid_keyword(key_words):
        abort(404, 'check your keywords to expand')
    handler = BusinessResource()
    departments = handler.get_all(Department, offset, limit, key_words)
    return jsonify(departments)


@app.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    key_words = get_keywords(request.args.getlist("expand", None))
    if invalid_keyword(key_words):
        abort(404, 'check your keywords to expand')
    handler = BusinessResource()
    item = handler.get_item(department_id, Department.DATA)
    if key_words:
        for keys in key_words:
            item = handler.handle_lists_key(item, keys)

    if item is None:
        abort(404)

    return jsonify(item)
