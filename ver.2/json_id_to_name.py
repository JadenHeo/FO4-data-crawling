import json

with open("spid.json", "r") as j:
    spid = json.load(j)
id_to_name = {}
for player in spid:
    id_to_name[int(player["id"])] = player["name"]
with open("id_to_name.json", "w", encoding="utf-8") as make_file:
    json.dump(id_to_name, make_file, ensure_ascii=False, indent="\t")