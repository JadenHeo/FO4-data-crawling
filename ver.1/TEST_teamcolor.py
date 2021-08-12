import json
import requests
from bs4 import BeautifulSoup
from selectors import selector
from functions import getHTMLfromSpid

spid = "234181458"
PlayerInfo = getHTMLfromSpid(spid)

# 팀컬러 세부 정보 가져오기. 팀컬러 이름, 설명, 능력치 증가 등등이 가져와짐.
# 추가적으로 모든 클럽의 이름, 국가 이름등의 목록이 다 뜨는듯...? 이것도 저장해놔야할 것 같다.
url = "http://fifaonline4.nexon.com/datacenter/TeamColorDetail"
header = {"X-Requested-With" : "XMLHttpRequest"}
param = {"teamcolorid": "2005"}
html = requests.get(url, headers=header, params=param)
soup = BeautifulSoup(html.text, "lxml")
#print(soup)


# 해당 팀컬러에 속하는 선수들 목록 가져오기. 불러와본 바로는 최대 100명까지 밖에 못가져오는 것 같다.
url = "http://fifaonline4.nexon.com/DataCenter/TeamColorPlayerList"
header = {"X-Requested-With" : "XMLHttpRequest"}
param = {"teamcolorid": "30007"}
html = requests.get(url, headers=header, params=param)
soup = BeautifulSoup(html.text, "lxml")
#print(soup)

