from flask import abort, jsonify, request

from glide_api.app import app
from glide_api.utils import json_reader


class Department:
    def __init__(self, expand_level=None):
        self.departments = json_reader(
            file='departments.json', folder='departments/data'
        )
        self.expand_level = expand_level

    def get_super_department(self, _id):
        for dep in self.departments:
            if dep['id'] == _id:
                return dep

    def get_all_values(self, departments):
        """
        Recursively search for ids of superdepartments
        """
        if isinstance(departments, dict):
            departments = departments.copy()
            super_department = departments['superdepartment']
            if super_department is None:
                return departments
            if isinstance(super_department, dict):
                departments['superdepartment'] = self.get_all_values(
                    super_department
                )

            if isinstance(super_department, int):
                departments['superdepartment'] = self.get_super_department(
                    super_department
                )
                return departments
        if isinstance(departments, list):
            return [self.get_all_values(item) for item in departments]
        if isinstance(departments, int):
            return self.get_super_department(departments)
        return departments

    def get_departments(self, limit=100, offset=0):
        """
        Get departments with limit and offset
        :param limit: max number of records returned
        :param offset: index at wich to start
        :param superdepartment: superdepartment id
        :return list of departments
        """
        filter_departments = self.departments[offset: (offset + limit)]
        if self.expand_level:
            for each in range(self.expand_level):
                filter_departments = self.get_all_values(filter_departments)
        return filter_departments


@app.route('/departments')
def get_departments():
    offset = int(request.args.get('offset', '0'))
    limit = int(request.args.get('limit', '100'))

    # TODO: should check if really I received expand and superdepartment
    # TODO: Clean this shit logic of expand level code
    expand = request.args.get("expand", None)
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

    department = Department()
    departments = [
        item for item in department.departments
        if item['id'] == department_id
    ]
    
    #TODO: make this code could use the function to gather all 
    #TODO: the items related
    
    if len(departments) == 0:
        abort(404)
    return jsonify({'departament': departments[0]})
