import requests
from bs4 import BeautifulSoup

from json_io import write_json

def make_spid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
    datas = requests.get(url).json()
    write_json("spid", datas)

def make_seasonid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/seasonid.json"
    datas = requests.get(url).json()
    write_json("seasonid", datas)