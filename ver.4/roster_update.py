import download_api_json
import time
import requests
import json
from player_info import player_info
import threading

# download_api_json.download_spid()
# download_api_json.download_seasonid()

url = "https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
spid = requests.get(url).json()

thread_number = 10
players_number = 10
players = [None] * players_number
threads = []


def work(thread_index, players_index, single_spid):
    print('thread number', thread_index, 'started')
    # for single_spid in [target_id for i, target_id in enumerate(spid[:players_number]) if i % thread_number == thread_index]:
    players[players_index] = player_info(single_spid)   
    print('thread number', thread_index, 'ended')

if __name__ == '__main__':
    start = time.time()
    for i in range(thread_number):
        threads.append(threading.Thread(target=work, args=(i, i, spid[i]['id'])))
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(len(players))
    with open('hi.json', 'w', encoding='utf-8') as make_file:
        json.dump(players, make_file, ensure_ascii=False, indent="\t")
    for player, single_id in zip(players, spid[:players_number]):
        print(player['spid'], single_id['name'])
    print(time.time() - start)