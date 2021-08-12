import json
import time
import requests
from bs4 import BeautifulSoup

with open("spid.json", "r", encoding="utf-8") as json_file:
    spid_data = json.load(json_file)

time_start = time.time()

playerPriceDB = []

for dic in spid_data[0:10]:
    datas={}
    datas["spid"] = dic["id"]

    url = "http://fifaonline4.nexon.com/datacenter/PlayerPriceGraph"
    html = requests.post(url, data = datas)
    soup = BeautifulSoup(html.text, "lxml")

    # 현재가
    price = soup.select("div > div:nth-child(2) > div > strong")
    # 최고가
    highest_price = soup.select("div:nth-child(2) > div > div > ul > li > strong")
    # 최저가
    lowest_price = soup.select("div:nth-child(2) > div > div > ul > li:nth-child(2) > strong")

    datas["name"] = dic["name"]
    datas["present price"] = price[0].text.strip()
    datas["highest price"] = highest_price[0].text.strip()
    datas["lowest price"] = lowest_price[0].text.strip()
    playerPriceDB.append(datas)

    #print("현재가 : ", price[0].text.strip())
    #print("최고가 : ", highest_price[0].text.strip())
    #print("최저가 : ", lowest_price[0].text.strip())

print(time.time()-time_start)
time_start = time.time()

with open("playerPriceDB.json", "w", encoding="utf-8") as make_file:
    json.dump(playerPriceDB, make_file, ensure_ascii=False, indent="\t")

print(time.time()-time_start)

