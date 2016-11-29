#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Preliminaries - Setup the pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

global p
p = GPIO.PWM(11, 50)

def turnGreen(seconds):
    p.stop()
    GPIO.output(12, GPIO.HIGH)
    p.start(1)
    time.sleep(seconds)
    p.stop()

def turnRed(seconds):
    p.stop()
    GPIO.output(12, GPIO.LOW)
    p.start(100)
    time.sleep(seconds)
    p.stop()

for i in range(2):
    turnGreen(0.5)
    turnRed(0.5)

GPIO.cleanup()
