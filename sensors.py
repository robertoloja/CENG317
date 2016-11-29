import sys
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import sevenSegment

sevenSegment.startup()

CLK  = 2
MISO = 3
MOSI = 4
CS   = 17
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

initial = 0

for i in range(99):
    initial += mcp.read_adc(0)
    time.sleep(0.002)

initial /= 100

count = 0
average = 0

while True:
    values = mcp.read_adc(0)
    time.sleep(0.002)
    count += 1
    average += values

    if count == 99:
        count = 0
        average /= 100
        average -= initial
        sys.stdout.write('\rWeight: %s  ' % repr(average))
        sevenSegment.displayNumber(int((average - 1) / 102.3))
        sys.stdout.flush()
        average = 0
