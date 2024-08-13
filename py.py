import sys
import RPi.GPIO as GPIO
import time

x = sys.argv[1]

pinIN1 = 12
pinIN2= 13
pinENA= 6
pinIN3= 20
pinIN4= 21
pinENB= 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinIN1, GPIO.OUT)
GPIO.setup(pinIN2, GPIO.OUT)
GPIO.setup(pinENA, GPIO.OUT)
GPIO.setup(pinIN3, GPIO.OUT)
GPIO.setup(pinIN4, GPIO.OUT)
GPIO.setup(pinENB, GPIO.OUT)

GPIO.output(pinENA, GPIO.HIGH)
GPIO.output(pinENB, GPIO.HIGH)

if(x=="w"):
    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.LOW)

    time.sleep(0.3)


    GPIO.output(pinIN1, GPIO.HIGH)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.HIGH)

elif(x=="s"):
    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.LOW)

    time.sleep(0.3)

    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.HIGH)
    GPIO.output(pinIN4, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.HIGH)

elif(x=="a"):
    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.LOW)

    time.sleep(0.3)

    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.HIGH)

elif(x=="d"):

    GPIO.output(pinIN1, GPIO.LOW)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.LOW)

    time.sleep(0.3)

    GPIO.output(pinIN1, GPIO.HIGH)
    GPIO.output(pinIN2, GPIO.LOW)
    GPIO.output(pinIN3, GPIO.LOW)
    GPIO.output(pinIN4, GPIO.LOW)