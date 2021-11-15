# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
from time import sleep


STOP  = 0
FORWARD  = 1
BACKWARD = 2


CH1 = 0


OUTPUT = 1
INPUT = 0


HIGH = 1
LOW = 0


#PWM PIN
ENA = 5    # BCM5 29 pin
ENB = 27   # BCM27 13 pin

#GPIO PIN
IN1 = 21   # BCM11 23 pin
IN2 = 20    # BCM9 21 pin


class motor:
    def __init__(self, inPin1, inPin2, enAPin, enBPin):        
       
        GPIO.setmode(GPIO.BCM)

        self.motorPin = [[enAPin, inPin1, inPin2]]
  
        self.pwm = []
     
        self.pwm.append(self.setPinConfig(CH1))
     


    def setPinConfig(self, ch):
        EN = self.motorPin[ch][0]
        INA = self.motorPin[ch][1]
        INB = self.motorPin[ch][2]

        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        GPIO.setup(INB, GPIO.OUT)
        # 100khz 로 PWM 동작 시킴 
        pwm = GPIO.PWM(EN, 100) 
    
        pwm.start(0) 
        return pwm

    def setMotorControl(self, ch, speed, stat):        
        EN = self.motorPin[ch][0]
        INA = self.motorPin[ch][2]
        INB = self.motorPin[ch][1] #motor backward 2

    
        self.pwm[ch].ChangeDutyCycle(speed)  
        
        if stat == FORWARD:
            GPIO.output(INA, HIGH)
            GPIO.output(INB, LOW)
            
 
        elif stat == BACKWARD:
            GPIO.output(INA, LOW)
            GPIO.output(INB, HIGH)
            
    
        elif stat == STOP:
            GPIO.output(INA, LOW)
            GPIO.output(INB, LOW)
            
   

            
  
    def setMotor(self, ch, speed, stat):
        self.setMotorContorl(self.pwm[ch], self.motorPin[ch][1], speed, stat)

    def __del__(self):
     
        GPIO.cleanup()
        
class surbo:
    def __init__ (self, pin, hz):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        
        self.p = GPIO.PWM(pin, hz) # 50 Hz
        self.p.start(0)
        
    def doAngle(self, angle):
        self.p.ChangeDutyCycle(angle)  
