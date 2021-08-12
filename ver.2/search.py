import json
from jsonfiles import id_to_name, player_prices

strong_constant = [0, 1, 2, 4, 6, 8, 11, 15, 19, 24]

for target_overall in range(95, 110):
    result = []
    
    for strong in range(5):
        temp = target_overall - strong_constant[strong]
        for player in player_prices:
            if player["overall"] == temp:
                result.append([player["id"], id_to_name[str(player["id"])], "+"+str(strong+1), player["price"][strong]/10000])
    result = sorted(result, key=lambda x: x[3])
    print("OVR", target_overall, " 재료 적정가 : ", result[5][3])
    #print(sorted(result, key=lambda x: x[3]))