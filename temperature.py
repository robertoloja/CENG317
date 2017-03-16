#!/usr/bin/python
import Adafruit_DHT
import time
from subprocess import call

sensor = Adafruit_DHT.DHT11

'''
pin1 = 10
pin2 = 25
pin3 = 20
pin4 = 21
'''

pins = [10, 25, 20, 21]
readings = [[None, None]] * 4

for i in range(0, len(readings)):
    while readings[i][0] is None and readings[i][1] is None:
        readings[i][0], readings[i][1] = Adafruit_DHT.read(sensor, pins[i])
        time.sleep(0.1)
    print i, ": Temp =", readings[i][0], ", Humidity =", readings[i][1]

'''
humidity1, temperature1 = Adafruit_DHT.read(sensor, pin1)
humidity2, temperature2 = Adafruit_DHT.read(sensor, pin2)
humidity3, temperature3 = Adafruit_DHT.read(sensor, pin3)
humidity4, temperature4 = Adafruit_DHT.read(sensor, pin4)

if humidity1 is not None and temperature1 is not None:
    #print('1st: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature1, humidity1))
    temp_list.append(temperature1)
    hum_list.append(humidity1)
else:
    #print('Failed to get first readings. Try again!')
    fail = 1
if humidity2 is not None and temperature2 is not None:
    #print('2nd: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature2, humidity2))
    temp_list.append(temperature2)
    hum_list.append(humidity2)
else:
    #print('Failed to get second readings. Try again!')
    fail = 1

if humidity3 is not None and temperature3 is not None:
    #print('3rd: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature3, humidity3))
    temp_list.append(temperature3)
    hum_list.append(humidity3)
else:
    #print('Failed to get third readings. Try again!')
    fail = 1

if humidity4 is not None and temperature4 is not None:
    #print('4th: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature4, humidity4))
    temp_list.append(temperature4)
    hum_list.append(humidity4)
else:
    #print('Failed to get fourth readings. Try again!')
    fail = 1

if fail != 1:
    temp = (temp_list[0] + temp_list[1] + temp_list[2] + temp_list[3])/4
    hum = (hum_list[0] + hum_list[1] + hum_list[2] + hum_list[3])/4
    print('{0:0.1f},{1:0.1f}'.format(temp, hum))
'''
