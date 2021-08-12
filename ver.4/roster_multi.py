import json
from time import time, strftime, localtime
from multiprocessing import Pool
from player_info_update import get_player_info
from dtd_price_update import get_player_price
from download_api_json import download_spid

def dtd_price_update(json_data):
    PROCESS_NUM = 4
    NUM_OF_DATA = len(json_data)
    # len(json_data)

    # 실행 시작 시간 출력
    print('dtd_price_update started')
    print('- start time :', strftime('%Y-%m-%d %H:%M', localtime()))
    print('- multi-process number :', PROCESS_NUM)
    print('- target data number : ', NUM_OF_DATA)

    start = time()
    pool = Pool(processes=PROCESS_NUM)
    data = pool.map(get_player_price, json_data[:NUM_OF_DATA])
    print(len(data), 'data collected')
    filename = strftime("%m%d", localtime(time()))
    
    with open(filename+'.json', 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")
    
    print('- time duration :', time()-start)

def player_info_update(json_data):
    PROCESS_NUM = 4
    NUM_OF_DATA = len(json_data)

    # 실행 시작 시간 출력
    print('player_info_update started')
    print('- start time :', strftime('%Y-%m-%d %H:%M', localtime()))
    print('- multi-process number :', PROCESS_NUM)
    print('- target data number : ', NUM_OF_DATA)

    start = time()
    pool = Pool(processes=PROCESS_NUM)
    data = pool.map(get_player_info, json_data[:NUM_OF_DATA])
    # print(data)
    print(len(data), 'data collected')

    with open("roster_multi.json", 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")
    
    print('- time duration :', time()-start)


if __name__ == '__main__':
    with open('spid.json', 'r', encoding='utf-8') as json_file:
        json_data = [spid['id'] for spid in json.load(json_file)]
    
    PRICE_UPDATE = True
    PLAYER_UPDATE = False

    if PRICE_UPDATE: dtd_price_update(json_data)
    if PLAYER_UPDATE: player_info_update(json_data)