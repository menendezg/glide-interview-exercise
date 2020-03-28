import requests
from glide_api.app import app


class ApiBigCorp:
    """
    Handle requests between controller and the api.
    """

    def __init__(self):
        self.url = (app.config['URL_DATA_SOURCE'])
        self.payload = {"limit": 10, "offset": 0}

    def get(self, params):
        r = requests.get(self.url, params=params)
        return r.json()
