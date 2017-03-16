#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description='Measure as fast as possible, record measurements to file.')
parser.add_argument('filename', metavar='O', type=str, nargs='?', help='log file')
args = parser.parse_args()
f = open(args.filename or 'readings.log', 'r')

frequency = {}

for line in f:
    if int(line) in frequency:
        frequency[int(line)] += 1
    else:
        frequency[int(line)] = 1

for elem in frequency:
    print "Number: " + repr(elem) + ", Amount: " + repr(frequency[elem])
