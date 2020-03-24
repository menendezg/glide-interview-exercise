import json
import os


def file_reader(file_path):
    with open(file_path, "r") as f:
        return f.read()


def get_path(folder):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), folder))


def json_reader(file, folder):
    """
    Load json file anywhere in the project
    :param file: the file to load.
    :param folder:  the folder where live the file
    :return: Dict object
    """
    return json.loads(file_reader(os.path.join(get_path(folder), file)))
