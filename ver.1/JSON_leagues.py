from functions import write_json
import requests
from bs4 import BeautifulSoup

# 국가 정보 가져오기
url = "http://fifaonline4.nexon.com/datacenter"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
s = soup.select("#form1 > div.search_panel > div.search_input_detail > div.search_input_detail_club > div.wrap_club.selector_wrap > div > ul > li > a")
#print(len(s))

url = "http://fifaonline4.nexon.com/datacenter"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
s = soup.select("#form1 > div.search_panel > div.search_input_detail > div.search_input_detail_club > div.wrap_league.selector_wrap > div > ul > li > a")
leagues = {}
for league in s:
    leagues[league.text] = league["data-no"]
print(leagues)
