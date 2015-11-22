import atexit
import urllib2
import math
import datetime
import time
import os
import sys
import threading
import subprocess
import re
import Adafruit_BBIO.GPIO as GPIO

pumpPin = 'P8_26'
startHour = 8
stopHour = 20
startMin = 1
stopMin = 26

def mapVals(val, inMin, inMax, outMin, outMax):
    toRet = float(outMin + float(outMax - outMin) * float(float(val - inMin) / float(inMax - inMin)))
    # if (toRet > outMax):
    #     toRet = outMax
    # if (toRet < outMin):
    #     toRet = outMin
    return clamp(toRet, outMin, outMax)

def clamp(val, min, max):
    if (val < min):
        val = min
    if (val > max):
        val = max
    return val

def goodHour(h):
    if h>=startHour and h<=stopHour:
        return True
    else:
        return False

def goodMin(m):
    if m>=startMin and m<=stopMin:
        return True
    else:
        return False

def handleTime():
    t = datetime.datetime.today()
    if goodMin(t.minute) and goodHour(t.hour):
        GPIO.output(pumpPin, GPIO.LOW)
        print 'time is %s hour %s min, should be LOW' % (t.hour, t.minute)
    else:
        GPIO.output(pumpPin, GPIO.HIGH)
        print 'time is %s hour %s min, should be HIGH' % (t.hour, t.minute)

GPIO.setup(pumpPin, GPIO.OUT)
GPIO.output(pumpPin, GPIO.HIGH)

while True:
    handleTime()
    time.sleep(30)