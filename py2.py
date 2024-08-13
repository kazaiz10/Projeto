import RPi.GPIO as GPIO

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

GPIO.cleanup()