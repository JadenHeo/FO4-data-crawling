from time import strftime, time, localtime, sleep
import json
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_player_price(spid):
    price = {'spid' : spid}
    url = 'https://fifaonline4.nexon.com/datacenter/PlayerPriceGraph'
    price_selector = 'strong'
    CURRENT, MAX, MIN = 0, 1, 2
    for strong in range(1, 11):
        data = {'spid' : spid, 'n1strong' : strong}
        response = requests.post(url, data=data)
        soup = BeautifulSoup(response.text, 'lxml')
        html_prices = [price_html.text.strip()[:-3].replace(',', '') for price_html in soup.select(price_selector)]
        # print(html_prices)
        price[strong] = {'current' : html_prices[CURRENT], 'max' : html_prices[MAX], 'min' : html_prices[MIN]}
        sleep(0.01)
    # print(price)
    return price
        
if __name__ == '__main__':
    with open('spid.json', 'r', encoding='utf-8') as json_file:
        json_data = [spid['id'] for spid in json.load(json_file)]
    
    PROCESS_NUM = 4
    NUM_OF_DATA = len(json_data)
    # len(json_data)

    # 실행 시작 시간 출력
    print(strftime('%Y-%m-%d %H:%M', localtime()))
    print('program started')
    print('multi-process number :', PROCESS_NUM)
    print('target data number : ', NUM_OF_DATA)

    start = time()
    pool = Pool(processes=PROCESS_NUM)
    data = pool.map(get_player_price, json_data[:NUM_OF_DATA])
    print(len(data), 'data collected')
    filename = strftime("%m%d", localtime(time()))
    
    with open(filename+'.json', 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")
    
    print('time duration :', time()-start)