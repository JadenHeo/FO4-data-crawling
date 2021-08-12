import json
import logging

with open('0803.json', 'r', encoding='utf-8') as json_file:
    json_data = [spid['spid'] for spid in json.load(json_file)]

print(len(json_data))