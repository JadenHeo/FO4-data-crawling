import requests
from bs4 import BeautifulSoup
from data import OVR_REP, CLASSID_TO_NAME, ID_TO_NAME, ID_TO_OVR, STRONG_CONS
from price_for_ovr import price_for_ovr
from json_io import read_json

def task():
    target_id = OVR_REP[98]
    target_strong = 4
    target_ovr = ID_TO_OVR[target_id] + STRONG_CONS[target_strong-1]
    print("========== 강화 대상 선수 ==========")
    print(CLASSID_TO_NAME[int(target_id/1000000)], ID_TO_NAME[target_id], "+", target_strong, "오버롤 :", target_ovr)

    prices = read_json("0213_2203")
    price_ovr_data = price_for_ovr(prices, target_ovr-5, target_ovr+10)
    #print(price_ovr_data)

    for i in range(target_ovr-5, target_ovr+10):
        material_id = OVR_REP[i]
        material_strong = 1
        material_ovr = ID_TO_OVR[material_id] + STRONG_CONS[material_strong-1]
        data = {}
        data["n8SpId"] = target_id
        data["n1Strong"] = target_strong
        data["strCalinfo"] = str(material_id)+"|"+str(material_strong)
        url = "http://fifaonline4.nexon.com/datacenter/PlayerGrowCal"
        soup = BeautifulSoup(requests.post(url, data = data).text, "lxml")
        probability = float(soup.select("div.tit > span")[0].text[:-1])
        print("========== 강화 재료 선수 ==========")
        print(CLASSID_TO_NAME[int(material_id/1000000)], ID_TO_NAME[material_id], "+", material_strong, "오버롤 :", material_ovr)
        print("강화부스트 확률 :", probability, "%")
        print("강화부스트 100% 가격 :", round(price_ovr_data[material_ovr] / probability * 100, 4))
        if probability > 100:
            break
    