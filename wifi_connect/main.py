from network import WLAN
import machine

wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    print ('Network SSID is %s' % net.ssid)
    if net.ssid == 'iotakl24':
        print('Network found %s' % net.ssid)
        wlan.connect(net.ssid, auth=(net.sec, 'iotakl17'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
