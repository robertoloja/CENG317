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


print 'Measuring baseline reading.'

def weight(x):
    x = int(x)
    a = 1E-8*x**4 - 1E-5*x**3 + 0.0036*x**2 - 0.1661*x + 1.5569
    b = 1E-8*x**4 - 7E-6*x**3 + 0.0007*x**2 + 0.2831*x - 6.8611
    c = 2E-9*x**4 - 2E-6*x**3 + 0.0004*x**2 + 0.2194*x - 6.515

    return (a + b + c) / 3


def mode(x):
    mostCommon = 0
    highest = 0

    for number in x:
        val = x.count(number)

        if val > highest:
            mostCommon = number
            highest = val

    return mostCommon


def takeFirstMeasurement():
    runningSum = []

    for i in range(101):
        runningSum.append(mcp.read_adc(0))
        time.sleep(0.01)

    ret = mode(runningSum)

    print repr(ret)
    return ret


def measureContinuously(initial):
    count = 0
    average = 0
    f = open('readings.log', 'w')

    while True:
        values = mcp.read_adc(0)

        f.write(repr(values) + '\n')

        #if values in range(initial - 10, initial + 11):
        count += 1
        average += values
            #initial = values

        if count == 10:
            average /= 10

            sys.stdout.write('\rWeight: %s  ' % repr(int(weight(average) if
                weight(average) >= 0 else 0)))

            sevenSegment.displayNumber(int((average - 1) / 102.3))
            sys.stdout.flush()
            average = 0
            count = 0

        time.sleep(0.01)

measureContinuously(takeFirstMeasurement())
