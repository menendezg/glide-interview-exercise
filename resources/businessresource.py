class BusinessResource():

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
                items = self.handle_relationship(items, self.data)
        return items

    def get_item(self, _id, values):
        return next(iter([item for item in values if item["id"] == _id]), None)

    def handle_relationship(self, value, key, data_set):
        """
        Look into al relationships given a dict, or list of dicts and a key.
        :param value: dict, or list of dicts
        :param key: key required to search
        :return: new dict or list of dict with the data replaced in the key
        """
        if isinstance(value, dict):
            value = value.copy()
            relationship = value[key]
            if relationship is None:
                return value
            if isinstance(relationship, dict):
                value[key] = self.handle_relationship(
                    relationship, key, data_set)
            if isinstance(relationship, int):
                value[key] = self.get_item(relationship, data_set)
                return value
        if isinstance(value, list):
            return [self.handle_relationship(item, key, data_set)
                    for item in value]
        if isinstance(value, int):
            return self.get_item(value)
        return value
