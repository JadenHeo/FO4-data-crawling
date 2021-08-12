import json


def read_json(filename):
    with open("./json_files/" + filename + ".json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data

def write_json(filename, data):
    with open("./json_files/" + filename+".json", "w", encoding="utf-8") as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")