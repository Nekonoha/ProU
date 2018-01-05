import requests
import time
from requests import *
import json

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
        requests.get(url, timeout=5)
        requests.post(url, data=json.dumps(test), headers=header)
        print("connected")
    except requests.exceptions.ConnectionError:
        print("no network")
    except requests.exceptions.ReadTimeout:
        print("timeout")
    time.sleep(1)
