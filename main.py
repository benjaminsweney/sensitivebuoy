# Code to run a stepper to draw water into a chamber for
# 'Spectural analysis'
# RGB LED mounted opposite photo resister in sample tube


import pycom
import machine
from machine import Pin
from uln2003Pycom import *
import time

delaytime = 1000 # Delay between samples

def led_on():
    led_G.value(1)
    led_R.value(1)
    led_B.value(1)

def led_off():
    led_G.value(0)
    led_R.value(0)
    led_B.value(0)

def take_sample():
    s1 = Stepper(FULL_STEP, 'G10', 'G9', 'G8','G7', delay=15)
    s1.step(100*3,1)     # Rotate 100 steps clockwis4

def eject_sample():
    s1 = Stepper(FULL_STEP, 'G10', 'G9', 'G8','G7', delay=15)
    s1.step(100*3,-1)     # Rotate 100 steps clockwis4

#take_sample()


led_G = Pin('G17', mode=Pin.OUT)
led_R = Pin('G22', mode=Pin.OUT)
led_B = Pin('G28', mode=Pin.OUT)


take_sample()


#TODO: Refactor to methods
#Sample 1
led_G.value(1);
time.sleep_ms(delaytime)
g_val= apin()
print('g_val: {}'.format(g_val))
time.sleep_ms(delaytime)
led_off()

#Sample 2
led_R.value(1);
time.sleep_ms(delaytime)
r_val= apin()
print('r_val: {}'.format(r_val))
time.sleep_ms(delaytime)
led_off()

#Sample 3
led_B.value(1);
time.sleep_ms(delaytime)
b_val= apin()
print( 'b_val: {}'.format( b_val))
time.sleep_ms(delaytime)
led_off()

#Sample 4

led_on()
time.sleep_ms(delaytime)
w_val= apin()
print('w_val: {}'.format(w_val))
time.sleep_ms(delaytime)
led_off()
