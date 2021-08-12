from json_io import read_json
from data import ID_TO_NAME, ID_TO_OVR, STRONG_CONS, CLASSID_TO_NAME

def price_for_ovr(prices, ovr_min, ovr_max):
    temp = {}
    for target_overall in range(ovr_min, ovr_max):
        result = []
        for strong in range(5):
            ovr_temp = target_overall - STRONG_CONS[strong]
            for player in prices:
                #print(type(player["id"]), player["id"])
                if ID_TO_OVR[player["id"]] == ovr_temp:
                    result.append([CLASSID_TO_NAME[int(player["id"]/1000000)] , ID_TO_NAME[player["id"]], "+"+str(strong+1), player["price"][strong]/10000])
        result = sorted(result, key=lambda x: x[3])
        temp[target_overall] = result[5][3]
        if __name__ == "__main__":
            print("OVR", target_overall, " 재료 적정가 : ", result[5][3])
            # 가격 경향성을 보기 위해 하위 10명의 선수까지 출력
            print(result[:10])
            # 게임 내 멀티서치가 가능한지 체크하기 위해 하위 30개의 선수 문자열로 출력
            #print(", ".join([x[1] for x in result[:30]]))
    return temp

if __name__ == "__main__":
    # 읽어올 가격정보 json 파일
    prices = read_json("0213_2203")
    # 가격대 구할 최저, 최고 ovr 설정
    price_for_ovr(prices, 95, 105)