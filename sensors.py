import sys
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import sevenSegment

CLK  = 27
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:
    values = mcp.read_adc(0)

    sys.stdout.write('\rWeight: %s    ' % repr(values))
    sevenSegment.displayNumber(int((values - 1) / 102.3))
    time.sleep(0.5)
    sys.stdout.flush()
