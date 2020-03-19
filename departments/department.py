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

    def get_department(self, department):
        """
        Get departments with limit and offset
        :param limit: max number of records returned
        :param offset: index at wich to start
        :param superdepartment: superdepartment id
        :return list of departments
        """

        for each in range(self.expand_level):
            department = self.get_all_values(department)
        return department
