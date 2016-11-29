#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

# These are the 7-segment display GPIO pins. 
A = 26
B = 21
C = 5
D = 6
E = 13
F = 19
G = 11

# This dictionary has the segments that describe each digits.
numbers = {1 : [B, C],
           2 : [A, B, G, E, D],
           3 : [A, B, D, C, G],
           4 : [F, G, B, C],
           5 : [A, F, G, C, D],
           6 : [A, F, G, C, D, E],
           7 : [A, B, C],
           8 : [A, B, C, D, E, F, G],
           9 : [A, B, C, F, G],
           0 : [A, B, C, D, E, F]}

def displayNumber(num):

    # Setup the pins
    for segment in numbers[8]: # as the 8 digit uses all segments
        GPIO.setup(segment, GPIO.OUT, initial=GPIO.HIGH)

    # display the number on the seven segment display
    for segment in numbers[num]:
        GPIO.output(segment, GPIO.LOW)


def startup():

    GPIO.setmode(GPIO.BCM)

    for segment in numbers[8]: # as the 8 digit uses all segments
        GPIO.setup(segment, GPIO.OUT, initial=GPIO.HIGH)

    for i in range(2):
        for segment in numbers[0]:
            GPIO.setup(segment, GPIO.OUT, initial=GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(segment, GPIO.HIGH)

    GPIO.cleanup()
