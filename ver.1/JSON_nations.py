from functions import write_json
import requests
from bs4 import BeautifulSoup

# 국가 정보 가져오기
url = "http://fifaonline4.nexon.com/datacenter"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
s = soup.select("#form1 > div.search_panel > div.search_input_detail > div.search_input_detail_nation > div.wrap_nationality.selector_wrap > div > ul > li > a")

Europe = []
Africa = []
South_America = []
Asia = []
Oceania = []
North_America = []

for country in s:
    if country["data-no"] == "2":
        Europe.append(country.text)
    elif country["data-no"] == "3":
        Africa.append(country.text)
    elif country["data-no"] == "4":
        South_America.append(country.text)
    elif country["data-no"] == "5":
        Asia.append(country.text)
    elif country["data-no"] == "6":
        Oceania.append(country.text)
    elif country["data-no"] == "7":
        North_America.append(country.text)

All = Europe + Africa + South_America + Asia + Oceania + North_America
All.sort()

Europe.sort()
Africa.sort()
South_America.sort()
Asia.sort()
Oceania.sort()
North_America.sort()

nations = {"All" : All, "Europe" : Europe, "Africa" : Africa, "South America" : South_America, "Asia" : Asia, "Oceania" : Oceania, "North America" : North_America}

write_json(nations, "nations")