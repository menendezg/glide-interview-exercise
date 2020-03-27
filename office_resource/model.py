from glide_api.utils import json_reader


class Office():
    DATA = json_reader(file="offices.json",
                       folder="office_resource/data")
