from glide_api.utils import json_reader


class Department():
    DATA = json_reader(
        file='departments.json', folder='department_resource/data')
