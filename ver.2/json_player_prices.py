import json
import requests
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

def make_price_int(price):
    price = price[:-3]
    price = "".join(price.split(","))
    return int(price)

""" 날짜별로 받아오기
datas={}
datas["spid"] = "221181458"
datas["n1strong"] = "1"
url = "http://fifaonline4.nexon.com/datacenter/PlayerPriceGraph"

now = time.time()
for i in range(1,11):
    datas["n1strong"] = i
    html = requests.post(url, data = datas)
    soup = BeautifulSoup(html.text, "lxml")
    txt = soup.script.get_text()
    
    #print(len(txt))
    txt = txt.replace("\n", "")
    txt = txt.replace("\r", "")
    txt = txt.replace(" ", "")
    #print(len(txt))
    #print(txt.find("value"))
    idx = txt.find("value") + 7
    idx2 = txt.find("varoption") - 3
    txt = txt[idx:idx2] + "]"
    #print(txt)
    txt = json.loads(txt)
    #print(i)
    #print(txt)
    
print(time.time()-now)
"""
with open("spid.json", "r") as j:
    json_datas = json.load(j)
#print(len(json_datas))


def work_single(num):
    datas={}
    url = "http://fifaonline4.nexon.com/datacenter/PlayerPriceGraph"
    
    for player in json_datas[:num]:
        for i in range(1,11):
            datas["spid"] = player["id"]
            datas["n1strong"] = i
            html = requests.post(url, data = datas)
            soup = BeautifulSoup(html.text, "lxml")
            #print(soup)
            #price_now = soup.select("div > div:nth-child(2) > div > strong")[0].text.strip()
            #print(price_now)

def work_multi(player):
    datas={}
    url = "http://fifaonline4.nexon.com/datacenter/PlayerPriceGraph"
    prices = []
    for i in range(1,11):
        datas["spid"] = player["id"]
        datas["n1strong"] = i
        price_now = 0
        while price_now == 0:
            html = requests.post(url, data = datas)
            soup = BeautifulSoup(html.text, "lxml")
            #print(soup)
            price_now = make_price_int(soup.select("div > div:nth-child(2) > div > strong")[0].text.strip())
            #print(price_now)
            #print(player["id"], "  +", i, "   ", price_now, "BP")
        prices.append(price_now)
    return {"id" : player["id"], "price" : prices}


if __name__ == "__main__":
    now = time.time()
    pool = Pool(4)
    player_prices = pool.map(work_multi, json_datas)
    print(time.time()-now)
    
    with open("player_prices_01_05.json", "w", encoding="utf-8") as make_file:
        json.dump(player_prices, make_file, ensure_ascii=False, indent="\t")

    now = time.time()
    #work_single(300)
    #print(time.time()-now)