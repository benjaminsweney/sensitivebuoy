import pycom
import machine
from network import WLAN

pycom.heartbeat(False)

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)

wlan.connect('iotakl24', auth=(WLAN.WPA2, 'iotakl17'), timeout=5000)

while not wlan.isconnected():
    machine.idle()

print('Connected to Wifi')
