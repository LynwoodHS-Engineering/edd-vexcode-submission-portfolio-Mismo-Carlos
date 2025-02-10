# Library imports
from vex import *
brain=Brain()

# Robot configuration code
bumper_a = Bumper(brain.three_wire_port.a)
bumper_b = Bumper(brain.three_wire_port.b)
led_g = Led(brain.three_wire_port.g)
led_h = Led(brain.three_wire_port.h)
# Begin project code

while True:
    if bumper_a.pressing() and bumper_b.pressing():
        led_g.on()
        led_h.off()
    else:
        led_g.off()
        led_h.on()
    wait(20,MSEC)
