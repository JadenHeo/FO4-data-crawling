import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

from json_io import write_json
from data import IDs

def id_to_ovr(id):
    url = "http://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid="+str(id)+"&n1Strong=1"
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    overall = int(soup.select("#middle > div > div > div:nth-child(2) > div.content.data_detail > div > div.content_header > div.info_wrap > div.info_line.info_ab > span > span:nth-child(2)")[0].text) + 3
    #print(overall)
    return {id : overall}

# id_to_ovr 함수가 제대로 작동하는지 본 코드에서 직접 체크
if __name__ == "__main__":
    now = time.time()
    pool = Pool(4)
    temp = pool.map(id_to_ovr, IDs[:10])
    print(time.time()-now)
    # json 으로 저장하면 int였던 key값이 어차피 자동으로 string으로 바뀌므로 따로 처리해주지 않음
    data = {list(x.keys())[0]:int(list(x.values())[0]) for x in temp}
    print(data)
    #write_json("id_to_ovr", data)