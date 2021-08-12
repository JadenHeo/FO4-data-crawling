import requests
from bs4 import BeautifulSoup
from selectors import selector
from functions import getHTMLfromSpid, getValue

spid = "101000001"
soup = getHTMLfromSpid(spid)
t = soup.select(selector["live up"])

print(t)