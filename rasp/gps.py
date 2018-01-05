#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import serial
from pynmea import nmea

ser = serial.Serial('/dev/ttyAMA0', 9600)
gpgga = nmea.GPGGA()

gpsLat = -1
gpsLong = -1

data = ser.readline()
if (data.startswith('$GPGGA')):
    gpgga.parse(data)
    gpggaLat = gpgga.latitude
    gpggaLong = gpgga.longitude
    # 受信できていない場合は空欄が返される
    if gpggaLat is not '':
        # GPSのNMEAフォーマットから変換する
        gpsLat = float(gpggaLat[0:1]) + float(gpggaLat[1:]) / 60
        gpsLong = float(gpggaLong[0:2]) + float(gpggaLong[2:]) / 60

print("Lat :" + str(gpsLat))
print("Long:" + str(gpsLong))


def get_gps_lat():
    return gpsLat


def get_gps_long():
    return gpsLong
