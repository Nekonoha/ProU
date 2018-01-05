from bottle import *
import webbrowser
import json
from datetime import datetime

google_map_url = "https://www.google.co.jp/maps/place/"

gps_log = []
Log_max = 3
counter = 0
API_KEY = "AIzaSyDnEiTyKwf-hV3y1Fuqm3E-O0lRSpaP2DQ"

@route("/static/<name>")
def static(name):
    return static_file(name, root="static/stylesheet")

@route('/index')
def index():
    return template("index", latitude=gps_log[0][0], longitude=gps_log[0][1], API_KEY=API_KEY)


@post("/gps")
def gps():
    global counter
    counter += 1

    content_type = request.get_header("Content-Type")
    gps_json = request.json
    now = datetime.now()

    # TODO: APIにつっこむ
    # webbrowser.open(google_map_url + gps_json["Latitude"] + "," + gps_json["Longitude"] + "/data=!5m1!1e1")
    # とりあえず交通情報と一緒にピンを表示するやつを開いている

    # 直近のGPSを保存　
    if len(gps_log) < Log_max:
        gps_log.append([gps_json["Latitude"], gps_json["Longitude"], now])
    else:
        gps_log.pop(0)
        gps_log.append([gps_json["Latitude"], gps_json["Longitude"], now])

    print(gps_log)

    return gps


if __name__ == "__main__":
    print(__name__)
    run(host="localhost", port=8000)
