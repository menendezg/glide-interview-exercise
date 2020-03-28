from glide_api.api.api import ApiBigCorp
from glide_api.resources.businessresource import BusinessResource


class Employee(BusinessResource):
    def get_all(self, limit=100, offset=0, key_words=None):
        api = ApiBigCorp()
        payload = {"limit": limit, "offset": offset}
        employees = api.get(payload)
        if key_words is not None:
            for keys in key_words:
                employees = [
                    self.handle_lists_key(employee, keys) for employee in employees
                ]

        return employees

    def get_employee_by_id(self, offset, limit=1):
        api = ApiBigCorp()
        payload = {"limit": limit, "offset": offset - 1}
        return api.get(payload)[0]
