from glide_api.resources.businessresource import BusinessResource
from glide_api.utils import json_reader


class Department(BusinessResource):
    def __init__(self):
        self.data = json_reader(
            file='departments.json', folder='department_resource/data'
        )

    def get_all(self, offset=0, limit=100, expand_number=None):
        """
        Return list of items.
        :param data: data to search
        :param offset: number to start
        :param limit: limit number to get
        :param expand_numer: number to iterate to get relationships
        """
        items = self.data[offset:(offset + limit)]
        if expand_number:
            for each in range(expand_number):
                items = self.handle_relationship(
                    items, 'superdepartment', self.data)
        return items
