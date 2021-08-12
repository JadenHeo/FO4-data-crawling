import json
import requests
import time
from bs4 import BeautifulSoup
from json_overall_rep import overall_reps

datas = {}
datas["n8SpId"] = 502232656
datas["n1Strong"] = 5
datas["strCalinfo"] = "201001605|1"
url = "http://fifaonline4.nexon.com/datacenter/PlayerGrowCal"
html = requests.post(url, data = datas)
soup = BeautifulSoup(html.text, "lxml")

a = {"a" : {"b" : 1}}
print(a["a"]["b"])

