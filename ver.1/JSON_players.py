import time
from getPlayerBasicInfo import getPlayerBasicInfo
from functions import getHTMLfromSpid, read_json, write_json
from multiprocessing import Pool

spid_data = read_json("spid")

time_start = time.time()

def work(dic):
    return getPlayerBasicInfo(getHTMLfromSpid(dic["id"]))

if __name__=='__main__':
    pool = Pool(processes = 4)
    db = pool.map(work, spid_data)
    print(len(db))
    write_json(db, "players")
    print(time.time()-time_start)