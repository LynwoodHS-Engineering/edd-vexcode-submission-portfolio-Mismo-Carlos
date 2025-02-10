from vex import *
import urandom

brain=Brain()

motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)

speed = 23
speed_2 = 25 
claw = 20
while True: 
    motor_1.spin(FORWARD,claw,PERCENT)
    wait(3,SECONDS)    
    motor_2.spin(FORWARD,speed,PERCENT)  
    motor_3.spin(REVERSE,speed_2,PERCENT)
    wait(8,SECONDS)
    motor_2.stop()  
    motor_3.stop()
    motor_1.spin(REVERSE,claw,PERCENT)
    wait(3,SECONDS)
    motor_1.stop()
    wait(2,SECONDS)
    motor_2.spin(REVERSE,speed, PERCENT)  
    motor_3.spin(FORWARD,speed_2,PERCENT)
    wait(8,SECONDS)
    motor_2.stop()  
    motor_3.stop()
    motor_1.spin(FORWARD,claw,PERCENT)
    wait(3,SECONDS)
    motor_1.stop()
    wait(1,SECONDS)
