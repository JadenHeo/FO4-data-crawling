import requests
from bs4 import BeautifulSoup
from time import time

# 주어진 list를 split_number의 수만큼 나눠서 리턴
# 멀티 프로세싱/스레딩 환경에서 사용할 가능성
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

start = time()
player = {'spid' : 101000001}
url = 'http://fifaonline4.nexon.com/DataCenter/PlayerInfo'
response = requests.get(url, params=player)
temp = BeautifulSoup(response.text, 'lxml')
# print(temp)
print(time()-start)

with open("single_page.html", "wb") as make_file:
    make_file.write(response.content)