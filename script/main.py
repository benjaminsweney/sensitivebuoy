import pycom
import time
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE

py = Pysense()
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

def read_light():
    colours = [0x7f0000, 0x007f00, 0x0000ff]

    for colour in colours:
        pycom.rgbled(colour) # toggle on rgb
        time.sleep_ms(250)
        reading = lt.light()
        print(reading)
        return reading # append light reading to lights

def read_acceleromator():
    reading = li.acceleration()
    print(reading)
    return reading # append light reading to lights

while True:
    light_readings = []
    acceleromator_readings = []

    light_readings.append(read_light())
    acceleromator_readings.append(read_acceleromator())

#os.mkfs('/flash')
