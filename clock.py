#!/usr/bin/python3

import time
import datetime
import pytz
import random
import ht1632c
import fonts
import RPi.GPIO as GPIO

CS0_PIN = 20        # Wire to CS pin on board0
CS1_PIN = 21        # Wire to CS pin on board0 & board1
WR_PIN = 19         # Wire to WR pin on board0 & board1
DATA_PIN = 16       # Wire to DATA pin on board0 & board1
SQW_PIN = 12        # DS3231 SQW output

def main_sqw():
    LED = ht1632c.Driver(WR_PIN, DATA_PIN, CS0_PIN, CS1_PIN, Font=fonts.ClockFont)
    LED.POST()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SQW_PIN, GPIO.IN)
    # rising edge:  2018-11-18 18:42:28.006868
    # falling edge: 2018-11-18 18:42:28.506827
    # rising edge:  2018-11-18 18:42:29.006830
    # falling edge: 2018-11-18 18:42:29.506852
    while True:
        e = GPIO.wait_for_edge(SQW_PIN, GPIO.RISING, timeout=2000)
        if e is None:
            continue
        now = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)
        LED.DisplayString("%s:%s:%s" % (hour, minute, second), 8)

def main_no_sqw():
    LED = ht1632c.Driver(WR_PIN, DATA_PIN, CS0_PIN, CS1_PIN, Font=fonts.ClockFont)
    LED.POST()
    previous_second = -1
    while True:
        now = datetime.datetime.now(tz=pytz.timezone('America/New_York'))
        if now.second == previous_second:
            time.sleep(0.05)
            continue
        previous_second = now.second
        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)
        LED.DisplayString("%s:%s:%s" % (hour, minute, second), 8)

if __name__ == '__main__':
    main_sqw()



