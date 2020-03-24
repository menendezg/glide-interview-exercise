from glide_api.resources.businessresource import BusinessResource
from glide_api.utils import json_reader


class Office(BusinessResource):
    def __init__(self):
        self.data = json_reader(file="offices.json",
                                folder="office_resource/data")
