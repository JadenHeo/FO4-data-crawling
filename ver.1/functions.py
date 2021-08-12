import json
import requests
from selectors import selector, position_overalls
from bs4 import BeautifulSoup

def read_json(title):
    with open(title + ".json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def write_json(object, title):
    with open(title+".json", "w", encoding="utf-8") as make_file:
        json.dump(object, make_file, ensure_ascii=False, indent="\t")

def get_testdata(test_case_number):
    temp = read_json("spid")
    data = []
    for dic in temp[0:test_case_number]:
        data.append(dic)
    return data

def getHTMLfromSpid(spid):
    url = "http://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid={id}&n1Strong=1".format(id = spid)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    return soup

def getValue(html):
    if len(html) == 1:
        return html[0].text.strip()
    elif len(html) == 0:
        return 0
    else:
        output = []
        for i in html:
            output.append(i.text.strip())
        return output
    
def getPosition(html):
    output = []
    for i in html:
        output.append(i.text.strip())
    return output

def getFootValue(html):
    temp = html[0].text.strip()
    return [int(temp[1]), int(temp[6])]


def getPositionOveralls(html):
    output = {}
    position = 0
    for i in html:
        output[position_overalls[position]] = int(i.text.strip()) + 3
        position += 1
    return output

def getClubHistory(html):
    output = []
    for i in range(int(len(html)/3)):
        history = {}
        history["year"] = html[3*i+0].text.strip()
        history["club"] = html[3*i+1].text.strip()
        history['loan'] = html[3*i+2].text.strip()
        output.append(history)
    return output

def getStat(html):
    output = {}
    for i in range(5):
        for j in range(7):
            b = html.select(selector["stat"] + " > ul:nth-child({col}) > li:nth-child({row}) > div".format(col=i+2, row=j+1))
            if i!=4 or j!=6:    
                output[b[0].text] = int(b[1].text) + 3
    return output