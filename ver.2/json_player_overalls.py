import json
import requests
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

with open("spid.json", "r") as j:
    json_datas = json.load(j)

def work(player):
    url = "http://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid="+str(player["id"])+"&n1Strong=1"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    overall = int(soup.select("#middle > div > div > div:nth-child(2) > div.content.data_detail > div > div.content_header > div.info_wrap > div.info_line.info_ab > span > span:nth-child(2)")[0].text) + 3
    #print(overall)
    return {player["id"] : overall}

if __name__ == "__main__":
    now = time.time()
    pool = Pool(4)
    player_overalls = pool.map(work, json_datas)
    print(time.time()-now)

    with open("player_overalls.json", "w", encoding="utf-8") as make_file:
        json.dump(player_overalls, make_file, ensure_ascii=False, indent="\t")