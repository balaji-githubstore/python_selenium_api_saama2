import json


def get_json_from_file(file_path):
    file = open(file=file_path)
    json_body = json.load(file)
    return json_body
