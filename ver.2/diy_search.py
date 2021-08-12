import json

with open("player_prices.json", "r") as j:
    player_prices = json.load(j)

with open("spid.json", "r") as j:
    spid = json.load(j)

id_to_name = {}
for player in spid:
    id_to_name[player["id"]] = player["name"]
season_id = {"live" : 300, "nhd" : 201, "tb" : 206, "tt" : 207, "gr" : 210, "tc" : 214, "coc" : 217, "hot" : 216, "tkl" : 225, "lh" : 234, "vtr" : 231}
card = [["live", 8, 30], ["nhd", 8, 30], ["tb", 8, 50], ["tt", 7, 50], ["gr", 7, 50], ["tc", 7, 100], ["coc", 7, 100], ["hot", 6, 100], ["tkl", 5, 50], ["lh", 5, 100], ["vtr", 5, 100]]
season_name = "gr"
top = 50
strong = 7

for i in range(len(card)):
    season_players = []
    for player in player_prices:
        if int(player["id"]/1000000) == season_id[card[i][0]]:
            temp = {"name" : id_to_name[player["id"]], "price" : player["price"][card[i][1]-1]/10000}
            season_players.append(temp)
    result = sorted(season_players, key=lambda x: -x["price"])[:card[i][2]]
    print("==============================================================", card[i][0], "==============================================================")
    print(result)



# top50 1/175
# 1~5:1, 6~10:2, 11~50:4

# top100 1/887
# 1~3:1, 4~10:2, 11~20:5, 21~50:8, 51~90:12, 91~100:10

#live 30 8
#nhd 30 8
#tb 50 8
#tt 50 7
#gr 50 7
#tc 100 7
#coc 100 7
#hot 100 6
#tkl 50 5
#lh 100 5
#vtr 100 5