import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

from json_io import write_json
from data import IDs

def make_prices(id):
    data={}
    url = "http://fifaonline4.nexon.com/datacenter/PlayerPriceGraph"
    price = []
    for strong in range(1,11):
        data["spid"] = id
        data["n1strong"] = strong
        # 가끔 정보를 퍼올 때 0BP 로 나오는 경우들이 있어서, 0이 아닌 값이 저장될 때 까지 반복시행
        price_now = 0
        while price_now == 0:
            soup = BeautifulSoup(requests.post(url, data = data).text, "lxml")
            # "--- BP" string이 나오는 tag 찾아서 soup.select, strip으로 양쪽 공백 없애주고, [:-3]으로 " BP" 없애주고,
            # replace로 , 없애줘서 숫자만 뽑아낸 후 int형으로 변환
            price_now = int(soup.select("div > div:nth-child(2) > div > strong")[0].text.strip()[:-3].replace(",",""))
            #print(price_now)
        price.append(price_now)
    return {"id" : id, "price" : price}

# make_prices 함수가 제대로 작동하는지 본 코드에서 직접 체크
if __name__=="__main__":
    now = time.time()
    pool = Pool(4)
    datas = pool.map(make_prices, IDs[:3])
    print(time.time()-now)
    print(datas)