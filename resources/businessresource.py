from glide_api.api.api import ApiBigCorp
from glide_api.department_resource.model import Department
from glide_api.office_resource.model import Office


class BusinessResource():
    def __init__(self):
        self.api = ApiBigCorp()

    def get_all(self, handler_class, offset=0, limit=100, key_words=None):
        """
        Return list of items.
        :param offset: number to start
        :param limit: limit number to get
        :param key_words: list of keywords to expand
        """
        items = handler_class.DATA[offset:(offset + limit)]
        if key_words:
            for keys in key_words:
                items = [self.handle_lists_key(item, keys) for item in items]

        return items

    def get_item(self, _id, values):
        return next(iter([item for item in values if item["id"] == _id]), None)

    def get_data(self, p_key, value):
        if p_key == 'manager':
            payload = {'limit': 1, 'offset': value - 1}
            item = self.api.get(payload)[0]
        else:
            item = self.get_item(value, self.get_data_set(p_key))
        return item

    def get_relationship(self, value, key, data_set):
        """
        Look into al relationships given a dict, or list of dicts and a key.
        :param value: dict, or list of dicts
        :param key: key required to search
        :return: new dict or list of dict with the data replaced in the key
        """
        if isinstance(value, dict):
            value = value.copy()
            relationship = value.get(key, None)
            if relationship is None:
                return value
            if isinstance(relationship, dict):
                value[key] = self.handle_relationship(
                    relationship, key, data_set)
            if isinstance(relationship, int):
                value[key] = self.get_item(relationship, data_set)
                return value

    def get_data_set(self, key):
        resources = {
            'department': Department.DATA,
            'superdepartment': Department.DATA,
            'office': Office.DATA,
        }
        return resources[key]

    def handle_lists_key(self, value, keys):
        """
        Look into al relationships given a dict, or list of dicts and a key.
        :param value: dict, or list of dicts
        :param keys: key required to search
        :return: new dict or list of dict with the data replaced in the key
        """
        keywords = keys[:]
        p_key = keywords.pop(0)  # get the first key
        if isinstance(value, dict):
            value = value.copy()
            for k, v in value.items():
                if k == p_key:
                    if v is None:
                        continue
                    if isinstance(v, int):
                        value[p_key] = self.get_data(p_key, v)
                        # data_set = self.get_data(p_key)
                        # value[p_key] = self.get_item(v, data_set)
                        # if p_key == 'manager':
                        #     api = ApiBigCorp()
                        #     payload = {'limit': 1, 'offset': v - 1}
                        #     value[p_key] = api.get(payload)[0]

                        while keywords:
                            related_key = keywords.pop(0)
                            data_set = self.get_data_set(related_key)
                            value[p_key] = self.get_relationship(
                                value[p_key],
                                related_key,
                                data_set
                            )
                        return value
        if isinstance(value, list):
            return [self.handle_manager_relationship(item, keys) for item in
                    value]
        if isinstance(value, int):
            return self.get_item(value)
        return value
