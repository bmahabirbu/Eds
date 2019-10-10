import busio
import time
import RPi.GPIO as GPIO
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D6)
mcp = MCP.MCP3008(spi, cs)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)
channel = AnalogIn(mcp, MCP.P0)
print(channel)


while True:
    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    time.sleep(0.5) 