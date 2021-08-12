import json

with open("player_prices_01_05.json", "r") as j:
    player_prices = json.load(j)
with open("player_overalls.json", "r") as j:
    player_overalls = json.load(j)

temp = {}
for player in player_overalls:
    temp[int(list(player.keys())[0])] = list(player.values())[0]
#print(len(temp))

for player in player_prices:
    player["overall"] = temp[player["id"]]

with open("player_prices_temp.json", "w", encoding="utf-8") as make_file:
    json.dump(player_prices, make_file, ensure_ascii=False, indent="\t")