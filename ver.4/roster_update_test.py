import download_api_json
import time
import requests
from bs4 import BeautifulSoup
import json
from player_info import player_info, processed_data
from selectors import css_selector
import threading

# download_api_json.download_spid()
# download_api_json.download_seasonid()

def only_data(spid):
    player = {'spid' : spid}
    url = 'http://fifaonline4.nexon.com/DataCenter/PlayerInfo'
    # params = {'spid' : spid}
    response = requests.get(url, params=player)
    return response.text

def list_split(input, split_number):
    single_len = len(input) // split_number
    start = 0
    end = single_len
    output = []
    for i in range(split_number):
        if i == split_number - 1:
            output.append(input[start:])
        else:
            output.append(input[start:end])
        start = end
        end += single_len
    return output

thread_number = 16
players_number = 100
players = [None] * players_number
players_ = [None] * players_number
threads = [None] * thread_number

url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
spid = requests.get(url).json()
splited_spid = list_split(spid[:players_number], thread_number)


def work(thread_index, players_index, single_spid):
    print('thread number', thread_index, 'started')
    # for single_spid in [target_id for i, target_id in enumerate(spid[:players_number]) if i % thread_number == thread_index]:
    players[players_index] = only_data(single_spid)   
    print('thread number', thread_index, 'ended')

def work_multi(thread_index):
    print('thread number', thread_index, 'started')
    temp = splited_spid[thread_index]
    # for single_spid in [target_id for i, target_id in enumerate(spid[:players_number]) if i % thread_number == thread_index]:
    for i in range(len(temp)):
        players_[thread_index * (players_number // thread_number) + i] = only_data(temp[i]['id'])   
    print('thread number', thread_index, 'ended')

if __name__ == '__main__':
    
    start = time.time()
    for i in range(players_number):
        work(i, i, spid[i]['id'])
    print(time.time() - start)
    # print(len(players))
    # for player, single_id in zip(players, spid[:players_number]):
        # print(player['name'], single_id['name'])
    
    start = time.time()
    for i in range(thread_number):
        threads[i] = threading.Thread(target=work_multi, args=(i,))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)