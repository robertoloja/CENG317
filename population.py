#!/usr/bin/python
import RPi.GPIO as GPIO
import threading
import time

'''
Each gate is modelled as a Finite State Machine, with seven possible states,
outlined by the following dictionary. The states are based on presumed
direction of motion and sensor readings. E.g. EGRESS_1_0 means that a bee has
started leaving the hive, and tripped only the inner sensor, while INGRESS_0_1
means that a bee has started entering the hive and tripped only the outter one.
The population count is incremented only when a gate has progressed through all
ingress stages and returned to the idle state. Population is decremented once
a gate has progressed through every egress stage and returned to idle, but only
if the population count was previously greater than 0.
'''

states = {
    'IDLE': 0,
    'EGRESS_1_0': 1,
    'EGRESS_1_1': 2,
    'EGRESS_0_1': 3,
    'INGRESS_0_1': 4,
    'INGRESS_1_1': 5,
    'INGRESS_1_0': 6
}

# Put all related data into one data structure. Constants are capitalized.
gates = [
    {'IN': 16, 'OUT': 18, 'state': states['IDLE']},
    {'IN': 11, 'OUT': 13, 'state': states['IDLE']},
    {'IN': 12, 'OUT': 15, 'state': states['IDLE']},
    {'IN': 29, 'OUT': 31, 'state': states['IDLE']},
    {'IN': 33, 'OUT': 35, 'state': states['IDLE']}
]

GPIO.setmode(GPIO.BOARD)

# This list comprehension puts every gate's 'IN' and 'OUT' into one big list...
pins = [x['IN'] for x in gates] + [x['OUT'] for x in gates]

# ...so we can setup every pin by just iterating over that list.
for pin in pins:
    GPIO.setup(pin, GPIO.IN)

count = 0


# This function will store the count into Mongo every 60 seconds
def storeCount():
    threading.Timer(10, storeCount).start()
    print(count)


storeCount()

while True:
    for gate in gates:
        inSensor = not GPIO.input(gate['IN'])  # Compensating for active low
        outSensor = not GPIO.input(gate['OUT'])

        if gate['state'] is states['IDLE']:
            if inSensor:
                gate['state'] = states['EGRESS_1_0']

            elif outSensor:
                gate['state'] = states['INGRESS_0_1']

        elif gate['state'] is states['EGRESS_1_0']:
            if outSensor:
                gate['state'] = states['EGRESS_1_1']

            elif not inSensor:
                gate['state'] = states['IDLE']

        elif gate['state'] is states['EGRESS_1_1']:
            if not inSensor:
                gate['state'] = states['EGRESS_0_1']

            elif not outSensor:
                gate['state'] = states['EGRESS_1_0']

        elif gate['state'] is states['EGRESS_0_1']:
            if inSensor:
                gate['state'] = states['EGRESS_1_1']

            elif not outSensor:
                gate['state'] = states['IDLE']

                if count > 0:
                    count -= 1

        elif gate['state'] is states['INGRESS_0_1']:
            if inSensor:
                gate['state'] = states['INGRESS_1_1']

            elif not outSensor:
                gate['state'] = states['IDLE']

        elif gate['state'] is states['INGRESS_1_1']:
            if not outSensor:
                gate['state'] = states['INGRESS_1_0']

            elif not inSensor:
                gate['state'] = states['INGRESS_0_1']

        elif gate['state'] is states['INGRESS_1_0']:
            if outSensor:
                gate['state'] = states['INGRESS_1_1']

            elif not inSensor:
                gate['state'] = states['IDLE']
                count += 1
    time.sleep(0.1)
