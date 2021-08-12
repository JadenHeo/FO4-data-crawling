import json
import requests
import time
from bs4 import BeautifulSoup

with open("spid.json", "r") as j:
    json_datas = json.load(j)

now = time.time()
url = "http://fifaonline4.nexon.com/datacenter/PlayerList"
datas = {}
datas["strPlayerName"] = "호나"
html = requests.post(url, data = datas)
soup = BeautifulSoup(html.text, "lxml")
print(time.time()-now)
temp1 = "div.info_top > input"
print(len(soup.select(temp1)))
"""
for a in soup.select(temp1):
    print(a["name"][6:])
"""
spid = soup.select(temp1)[0]["name"][6:]
temp2 = "div.td.td_ar_bp.bp_"+spid+">span"
print(time.time()-now)

print(soup.select(temp2))