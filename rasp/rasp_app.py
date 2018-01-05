import requests
import time
from requests import *
import json
from rasp import gps

url = "http://localhost:8000/gps"

test = {
    "Latitude":"35.627599 N",
    "Longitude": "139.339755 E"
}

header = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=UTF-8"
}

while True:
    try:
        gps_lat = str(gps.get_gps_lat())
        gps_long = str(gps.get_gps_long())
        gps = {
            "Latitude": gps_lat,
            "Longitude": gps_long
        }
        # test のとこをgpsにする
        # urlを本番のurlにする
        requests.get(url, timeout=5)
        requests.post(url, data=json.dumps(test), headers=header)
        print("connected")
    except requests.exceptions.ConnectionError:
        print("no network")
    except requests.exceptions.ReadTimeout:
        print("timeout")
    time.sleep(1)
