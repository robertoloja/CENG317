#!/usr/bin/python
import argparse
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK  = 2
MISO = 3
MOSI = 4
CS   = 17
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

parser = argparse.ArgumentParser(description='Measure as fast as possible, record measurements to file.')
parser.add_argument('filename', metavar='O', type=str, nargs='?', help='log file')
args = parser.parse_args()

f = open(args.filename or 'readings.log', 'w')

while True:
    values = mcp.read_adc(0)
    f.write(repr(values) + '\n')
    print repr(values)
