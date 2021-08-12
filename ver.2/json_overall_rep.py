import json

with open("player_overalls.json", "r") as j:
    player_overalls = json.load(j)

overall_reps = {}

temp = {"101000001" : 104}
print(list(temp.values()))

for data in player_overalls:
    overall = list(data.values())[0]
    if overall > 70 and overall < 113:
        if overall_reps.get(overall) == None:
            overall_reps[overall] = list(data.keys())[0]

#print(sorted(overall_reps.items()))
