import json

with open("spid.json", "r") as j:
    spid = json.load(j)

with open("player_prices_temp.json", "r") as j:
    player_prices = json.load(j)

with open("id_to_name.json", "r") as j:
    id_to_name = json.load(j)