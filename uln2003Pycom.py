# Ported from a ULN2003 library for the microbit by:
# (c) IDWizard 2017
# MIT License.
# TODO: GET DIRECTION CHANGE WORKING - SEEMS TO GO IN ONE DIRECTION ONLY
from machine import Pin
import time

#0 = 0
#1 = 1
FULL_ROTATION = int(4075.7728395061727 / 8) # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

HALF_STEP = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]
"""
FULL_STEP = [
 [1, 0, 1, 0],
 [0, 1, 1, 0],
 [0, 1, 0, 1],
 [1, 0, 0, 1]
]
"""

FULL_STEP = [
 [1, 0, 0, 1],
 [0, 1, 0, 1],
 [0, 1, 1, 0],
 [1, 0, 1, 0]
]


class Command():
    """Tell a stepper to move X many steps in direction"""
    def __init__(self, stepper, steps, direction=1):
        self.stepper = stepper
        self.steps = steps
        self.direction = direction

class Driver():
    """Drive a set of motors, each with their own commands"""

    @staticmethod
    def run(commands):
        """Takes a list of commands and interleaves their step calls"""

        # Work out total steps to take
        max_steps = sum([c.steps for c in commands])

        count = 0
        while count != max_steps:
            for command in commands:
                # we want to interleave the commands
                if command.steps > 0:
                    command.stepper.step(1, command.direction)
                    command.steps -= 1
                    count += 1

class Stepper():
    def __init__(self, mode, pin1, pin2, pin3, pin4, delay):
        self.mode = mode
        self.pin1 = Pin(pin1, mode=Pin.OUT)
        self.pin2 = Pin(pin2, mode=Pin.OUT)
        self.pin3 = Pin(pin3, mode=Pin.OUT)
        self.pin4 = Pin(pin4, mode=Pin.OUT)
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP

        # Initialize all to 0
        self.reset()

    def step(self, count, direction):
        """Rotate count steps. direction = -1 means backwards"""
    #    direction = 1
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1.value(bit[0])
                self.pin2.value(bit[1])
                self.pin3.value(bit[2])
                self.pin4.value(bit[3])

                #print(bit[0])
                #sleep(self.delay)
                time.sleep_ms(self.delay)
                self.reset()

    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1.value(0)
        self.pin2.value(0)
        self.pin3.value(0)
        self.pin4.value(0)

if __name__ == '__main__':

    s1 = Stepper(HALF_STEP, pin1, pin2, pin3, pin4, delay=5)
    s2 = Stepper(HALF_STEP, microbit.pin6, microbit.pin5, microbit.pin4, microbit.pin3, delay=5)

    #(self, mode, pin1, pin2, pin3, pin4, delay=2)
    #s1.step(FULL_ROTATION)
    #s2.step(FULL_ROTATION)

    runner = Driver()
    runner.run([Command(s1, FULL_ROTATION, 1), Command(s2, FULL_ROTATION/2, -1)])
