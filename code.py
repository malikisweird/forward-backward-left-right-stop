import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

Right_motor_forward = board.GP14
Right_motor_backward = board.GP15
Left_motor_forward = board.GP12
Left_motor_backward = board.GP13

pwm_Ra = pwmio.PWMOut(Right_motor_forward, frequency=10000)
pwm_Rb = pwmio.PWMOut(Right_motor_backward , frequency=10000)
pwm_La = pwmio.PWMOut(Left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(Left_motor_backward , frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line(it is required)
Left_Motor_speed = 0
Right_Motor = motor.DCMotor( pwm_Ra, pwm_Rb)
Right_Motor_speed = 0

def forward():
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(3)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(3)

while True:
    forward()
'''

def: backward
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(3)
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(3)

def: forward
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(3)

def: backward
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(3)
'''

