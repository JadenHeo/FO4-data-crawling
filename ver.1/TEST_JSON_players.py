import time
from getPlayerBasicInfo import getPlayerBasicInfo
from functions import getHTMLfromSpid, read_json, write_json, get_testdata
from selectors import selector
from multiprocessing import Pool
"""
test_case_number = 10

test_data = get_testdata(test_case_number)

time_start = time.time()

def work(dic):
    return getPlayerBasicInfo(getHTMLfromSpid(dic["id"]))

if __name__=='__main__':
    pool = Pool(processes = 4)
    db = pool.map(work, test_data)
    print(len(db))
    write_json(db, "players_test")
    print(time.time()-time_start)
"""
datas = read_json("spid")
season_datas = read_json("seasons")
season = int(datas[0]["id"] / 1000000)
each_season_player = [{"spid" : datas[0]["id"], "season" : season_datas[0]["season"]}]
count = 1
for data in datas:
    temp = int(data["id"] / 1000000)
    if temp != season:
        each_season_player.append({"spid" : data["id"], "season" : season_datas[count]["season"]})
        season = temp
        count += 1
#print(each_season_player)

output = read_json("players_test")

count = 0
for player in output:
    if player["team"] == "":
        count += 1
        s = int(player["spid"] / 1000000)
        print(s)


print(count)