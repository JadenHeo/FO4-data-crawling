from pymongo import MongoClient
from functions import read_json

client = MongoClient('localhost', 27017)

data = read_json("players")

# 넣고자 하는 db 이름을 client에 기입
testdb = client["testdb"]
# 해당 db 안에 collection 이름 생성, 그안에 import
collection = testdb["PLAYERS"]

work = collection.insert(data)