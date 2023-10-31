import json


def json_load(path: str):
    f = open(path, "r")

    data = json.loads(f.read())

    f.close()
    return data
