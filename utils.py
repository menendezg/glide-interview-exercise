import os
import json


def file_reader(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_path(folder):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), folder))


def json_reader(file, folder='data'):
    return json.loads(file_reader(os.path.join(get_path(folder), file)))
