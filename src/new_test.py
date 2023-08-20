#!/usr/bin/env python

import VL53L1X
import RPi.GPIO as GPIO
import time

#VCC = 18
XSHUT = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(XSHUT,GPIO.OUT)
#GPIO.setup(VCC,GPIO.OUT)
#GPIO.output(VCC,GPIO.HIGH)
GPIO.output(XSHUT,GPIO.LOW)

tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof1.open()
tof1.change_address(new_address = 0x2A)
GPIO.output(XSHUT, GPIO.HIGH)
GPIO.setup(XSHUT,GPIO.IN)
tof1.open()
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof2.open()

#time.sleep(.5)

for i in range(10):
        tof1.start_ranging(3)
        distance_in_mm = tof1.get_distance()
        print('Sensor:1',distance_in_mm)
        tof1.stop_ranging()

        tof2.start_ranging(3)
        distance_in_mm = tof2.get_distance()
        print('Sensor:2',distance_in_mm)
        tof2.stop_ranging()

        GPIO.cleanup()
