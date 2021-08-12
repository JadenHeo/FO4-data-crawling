from functions import read_json, write_json
import requests
from bs4 import BeautifulSoup

# 선수 spid를 받아서 
def getPlayerSeason(s):
    url = "http://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid={spid}&n1Strong=1".format(spid = s)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")

    className = soup.select("#middle > div > div > div:nth-child(2) > div.content.data_detail > div > div.content_header > div.info_wrap > div.info_line.info_name > div.season > img")
    #print(className[0])
    #print(type(className[0]))
    length = len(className[0]["src"])
    # src에 있는 png파일 주소에서 필요없는 거 빼고 시즌 이름만 가져옴
    # ex.) http://s.nx.com/s2/game/fo4/obt/externalAssets/season/PLC.png 에서 왼쪽 54개 빼고 오른쪽에 .png 제거한 후 PLC로 만들어서 return
    return className[0]["src"][54:length-4]

spid_data = read_json("spid")

# spid_data 타입 확인 ; list형 변수
#print(type(spid_data))
# spid_data 길이 확인 ; 38423
#print(len(spid_data))
# spid_data list변수의 첫번째 변수 타입확인 ; dictionary
#print(type(spid_data[0]))


# spid.json에 첫번째 선수의 시즌 id(spid의 첫 3자리)를 seasonID에 저장
seasonID = int(spid_data[0]["id"]/1000000)
# 선수 시즌 정보를 저장할 seasons는 list형 변수로 dictionary(시즌id, 시즌이름)을 저장할 것
seasons = [{"id":seasonID, "season":getPlayerSeason(spid_data[0]["id"])}]

# spid.json을 읽으면서 spid의 첫 3자리, 즉 시즌id가 달라질때마다 seasons에 append로 저장
for i in range(len(spid_data)):
    temp = int(spid_data[i]["id"]/1000000)
    if temp != seasonID:
        seasonID = temp
        seasons.append({"id":seasonID, "season":getPlayerSeason(spid_data[i]["id"])})

#print(seasons)
#print(len(seasons))

# 다 만들어진 seasons list변수를 seasons.json파일로 출력
write_json(seasons, "seasons")