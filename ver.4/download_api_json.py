import requests
import json

def download_spid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
    datas = requests.get(url).json()
    with open("spid.json", "w", encoding="utf-8") as make_file:
        json.dump(datas, make_file, ensure_ascii=False, indent="\t")

def download_seasonid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/seasonid.json"
    datas = requests.get(url).json()
    with open("seasonid.json", "w", encoding="utf-8") as make_file:
        json.dump(datas, make_file, ensure_ascii=False, indent="\t")