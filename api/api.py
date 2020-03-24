import requests


class ApiBigCorp():
    """
    Handle requests between controller and the api.
    """

    def __init__(self):
        self.url = 'https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees'
        self.payload = {
            'limit': 10,
            'offset': 0
        }

    def get(self, params):
        r = requests.get(self.url, params=params)
        return r.json()
