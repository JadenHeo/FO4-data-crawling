import time
import requests
from bs4 import BeautifulSoup
from selectors import selector
from functions import getValue, getPosition, getFootValue, getPositionOveralls, getClubHistory, getStat

def getPlayerBasicInfo(PlayerInfo):
    player = {}
    
    # id
    player["spid"] = int(PlayerInfo.select("html > body > div > main > input")[0]["value"])
    # name
    player["name"] = getValue(PlayerInfo.select(selector["name"]))
    # pay
    player["pay"] = int(getValue(PlayerInfo.select(selector["pay"])))
    # position
    player["position"] = getPosition(PlayerInfo.select(selector["position"]))
    # live up
    player["live up"] = getValue(PlayerInfo.select(selector["live up"]))
    # birth
    birth = getValue(PlayerInfo.select(selector["birth"]))
    player["birth"] = int(birth[0:4] + birth[5:7] + birth[8:10])
    # height
    player["height"] = int(getValue(PlayerInfo.select(selector["height"]))[:-2])
    # weight
    player["weight"] = int(getValue(PlayerInfo.select(selector["weight"]))[:-2])
    # physical
    player["physical"] = getValue(PlayerInfo.select(selector["physical"]))
    # skill
    player["skill"] = len(getValue(PlayerInfo.select(selector["skill"])))
    # foot
    player["foot"] = getFootValue(PlayerInfo.select(selector["foot"]))
    # main foot
    player["main foot"] = getValue(PlayerInfo.select(selector["foot"] + " > strong"))[0]
    # class
    player["class"] = getValue(PlayerInfo.select(selector["class"]))
    # team
    player["team"] = getValue(PlayerInfo.select(selector["team"]))
    # nation
    nation = getValue(PlayerInfo.select(selector["nation"]))
    if "," in nation:
        nation = nation[:-6]
    player["nation"] = nation
    # speciality
    speciality = getValue(PlayerInfo.select(selector["speciality"]))
    if type(speciality) == str:
        speciality = [speciality]
    player["speciality"] = speciality
    # position overalls
    player["position overalls"] = getPositionOveralls(PlayerInfo.select(selector["position_overalls"]))
    # club history
    player["club_history"] = getClubHistory(PlayerInfo.select(selector["club_history"]))

    # player stat
    player["stat"] = getStat(PlayerInfo)

    #print(player)
    return player

#clubhistory
    
    