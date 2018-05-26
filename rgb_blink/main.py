import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0x007f00) # green
    time.sleep(1)
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(1)
    pycom.rgbled(0x7f0000) # red
    time.sleep(1)
