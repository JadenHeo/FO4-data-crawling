import requests
from bs4 import BeautifulSoup

spid = "230234396"
url = "http://fifaonline4.inven.co.kr/dataninfo/player/?code=" + spid
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

name = soup.select("#fifaonline4Db > div.fifa4.db_player_info.clearfix > div.fifa4.left > div > div.fifa4.tooltip_title > p")[0].text
print(name)
