from vex import *
brain=Brain()
optical_1 = Optical(Ports.PORT1)
object_detect_threshold = 100


while True: 
    z = optical_1.brightness()

    brain.screen.print(z)
    wait(0.1,SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    delay = max(0.1, min(1.0, z / 100))
    play_vexcode_sound("game over")
