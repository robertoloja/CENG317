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

count = 0
average = 0

def weight(x):
    x = int(x)
    a = 1E-8*x**4 - 1E-5*x**3 + 0.0036*x**2 - 0.1661*x + 1.5569 # R^2 = 0.9991
    b = 1E-8*x**4 - 7E-6*x**3 + 0.0007*x**2 + 0.2831*x - 6.8611 # R^2 = 0.9984
    c = 2E-9*x**4 - 2E-6*x**3 + 0.0004*x**2 + 0.2194*x - 6.515  # R^2 = 0.9989

    return (a + b + c) / 3

while True:
    values = mcp.read_adc(0)
    time.sleep(0.01)
    count += 1
    average += values

    if count == 9:
        count = 0
        average /= 10

        if average <= 0:
            average = 0

        if average >= 1023:
            average = 1023

        sys.stdout.write('\rWeight: %s  ' % repr(int(weight(average))))
        sevenSegment.displayNumber(int((average - 1) / 102.3))
        sys.stdout.flush()
        average = 0

