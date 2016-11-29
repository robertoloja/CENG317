#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys


def displayNumber(num):

    # These are the 7-segment display GPIO pins. 
    A = 26
    B = 20
    C = 21
    D = 19
    E = 16
    F = 13
    G = 6

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

    # Setup the pins
    for segment in numbers[8]: # as the 8 digit uses all segments
        GPIO.setup(segment, GPIO.OUT, initial=GPIO.HIGH)

    # blank every segment
    for segment in numbers[8]:
        GPIO.output(segment, GPIO.HIGH)

    #display the number on the seven segment display
    for segment in numbers[num]:
        GPIO.output(segment, GPIO.LOW)
