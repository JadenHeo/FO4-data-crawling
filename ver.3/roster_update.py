# 하위폴더 json_files 참조 경로 추가
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
sys.path.insert(0, "d:\\WORK\\git_repos\\fo4_data_crawling\\Project_revised2\\json_files")
# D:\WORK\git_repos\fo4_data_crawling\Project_revised2\json_files
# 기본 모듈 import
import time
import requests
from multiprocessing import Pool
from multiprocessing import freeze_support
# 커스텀 모듈 import
from json_files.json_io import write_json
from task_manager import task_run

# open API 문서로 부터 업데이트 필요
# spid.json 업데이트
def make_spid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
    data = requests.get(url).json()
    write_json("spid", data)
# seasonid.json 업데이트
def make_seasonid():
    url = "https://static.api.nexon.co.kr/fifaonline4/latest/seasonid.json"
    data = requests.get(url).json()
    write_json("seasonid", data)
# 업데이트 실행
make_spid()
make_seasonid()

# 향후 작업들은 spid.json으로부터 만들어지는 IDs list 객체를 기준으로 작업되므로 업데이트 이후 import함
from json_files.data import IDs
from json_files.id_to_ovr import id_to_ovr
#from json_files.prices import make_prices

# 멀티프로세싱 task 정의
def task(num):
    # 나중에 불려진 후의 시간에서 빼주기 위해 시작 시간 저장
    now = time.time()
    # 실행횟수 num이 1~총 데이터 길이 를 벗어나면 총 길이로 바꿔줌
    if num not in range(1,len(IDs)):
        num = len(IDs)
    # 4중 멀티프로세싱
    pool = Pool(processes=8)
    temp = pool.map(id_to_ovr, IDs[:num])
    data = {list(x.keys())[0]:int(list(x.values())[0]) for x in temp}
    write_json("id_to_ovr", data)
    #print(data)
    # 수집된 데이터 개수 num, 멀티프로세싱 시작 전 시간 now 를 튜플로 반환
    return num, now

# task 실행
if __name__=='__main__':
    freeze_support()
    task_run(task(10))
