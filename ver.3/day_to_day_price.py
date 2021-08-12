# 하위폴더 json_files 참조 경로 추가
import sys
sys.path.insert(0, "/Users/heo/Documents/VSCProject/Project2/json_files")
# 기본 모듈 import
import time
import requests
from multiprocessing import Pool
# 커스텀 모듈 import
from json_files.data import IDs
from json_files.prices import make_prices
from json_files.json_io import write_json
from task_manager import task_run

# 멀티프로세싱 task 정의
def task(num):
    # 나중에 불려진 후의 시간에서 빼주기 위해 시작 시간 저장
    now = time.time()
    # 파일명에 넣을 "월일_시분" 포멧 string 생성
    filename = time.strftime("%m%d_%H%M", time.localtime(now))

    # 실행횟수 num이 1~총 데이터 길이 를 벗어나면 총 길이로 바꿔줌
    if num not in range(1,len(IDs)):
        num = len(IDs)
    # 4중 멀티프로세싱
    pool = Pool(4)
    data = pool.map(make_prices, IDs[:num])
    
    write_json(filename, data)
    #print(data)
    # 수집된 데이터 개수 num, 멀티프로세싱 시작 전 시간 now 를 튜플로 반환
    return num, now

# task 실행
task_run(task(0))

