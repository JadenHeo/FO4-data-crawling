import json
from json_io import read_json

# 선수 ID 들로 이루어진 list
IDs = list(map(lambda x: int(x["id"]), read_json("spid")))
#print(len(IDs))

# 선수 id를 key값, name을 value로 갖는 dict
ID_TO_NAME = {x["id"]:x["name"] for x in read_json("spid")}

# 선수 id를 key값, overall을 value로 갖는 dict
ID_TO_OVR = {int(key):val for key,val in read_json("id_to_ovr").items()}
#print(len(ID_TO_OVR))

# 클래스 id를 key값, 클래스 name을 value로 갖는 dict
# dict comprehension, 긴 classname을 " (" 로 나눈 후, 앞 문자열에서 공백을 replace로 없앤 후 value에 넣어줌
CLASSID_TO_NAME = {x["seasonId"]:x["className"].split(" (")[0].replace(" ", "") for x in read_json("seasonid")}

# 선수 오버롤 (+1 기준 최소 42 ~ 최대 112) 별로 대표하는 선수 1명의 ID를 반환하는 dict
# CLASSID 300, 506 인 20Live, 20PLA 시즌은 계속 오버롤이 변하므로 대표선수에서 제외
OVR_REP = {val:key for key,val in ID_TO_OVR.items() if int(int(key)/1000000)!=506 and int(int(key)/1000000)!=300}

# 선수 강화 레벨 별 능력치 증가량 list
STRONG_CONS = [0, 1, 2, 4, 6, 8, 11, 15, 19, 24]

