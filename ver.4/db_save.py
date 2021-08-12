from pymongo import MongoClient, collection
import json
from time import time, strftime, localtime

client = MongoClient('localhost', 27017)
# print(client.list_database_names())

# dtd price info update to DB
def dtd_price_update(date):
    with open(date+'.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    db = client['fo4_dtd_price_info']
    collection = db[date]
    collection.insert(data)

def players_update():
    with open('roster_multi.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    db = client['fo4_database']
    collection = db['players_info']
    collection.insert(data)

cur_date = strftime("%m%d", localtime(time()))
# dtd_price_update(cur_date)

# players_update()

dtd_price_update('0730')