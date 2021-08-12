import time
from threading import Thread
import json
import requests
from pprint import pprint

def parse(json1):
    data = json1['data']
    # data_id
    return data

def gogo(page_idx, results):
    url = 'https://data.mafra.go.kr/opendata/data/open/getDataListPage.do'
    data = requests.post(url, data={
        'cur_page':page_idx,
        'rows':10
    })
    res = parse(data.json())
    results[page_idx] = res
    print('thread {} finished'.format(page_idx))

total_pages = 107 + 1 # index는 0번부터 page는 1번부터

# global에 variable을 생성 해준다
threads = [None] * total_pages
results = [None] * total_pages

start = time.time()

for i in range(1, total_pages):
    threads[i] = Thread(target=gogo, args=(i, results))
    threads[i].start()
    print('thread {} started'.format(i))

for i in range(1, total_pages):
    threads[i].join()
# time.sleep(total_pages / 3)
'''
for i in range(1, total_pages):
    gogo(i, results)
'''
cnt = 0
result_total = []
for result in results:
    cnt += 1
    # print(cnt, end='')
    if result != None:
        #print(len(result), result)
        result_total += result
print(len(result_total[1]))
print(time.time()-start)

with open("test.json", "w", encoding="utf-8") as make_file:
    json.dump(results, make_file, ensure_ascii=False, indent="\t")

# json_save(result_total, 'mafra_total_data.json')