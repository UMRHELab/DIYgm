#James Seekamp, Jeffery Xiao, Issa El-Amir, Regina Tuey, Max Li, Andrew Kent
#2/6/2021
#DIY Geiger Kit for RPi Zero W and iOS


#Library Imports
import RPi.GPIO as GPIO
import bluetooth
import socket
import time
import os
import sys

#Declares pins and disables error message
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# PWM Pin
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)

# Measurement Receiver Pin
GPIO.setup(32, GPIO.IN)

# Measurement Power Pin
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.HIGH)

#Set the frequency and GPIO pin. Keep pin to 12.
#Frequency has limited effect on the voltage. 
pwm = GPIO.PWM(12, 1000) 

GPIO.add_event_detect(32,GPIO.RISING)

def detection():
    cpm = 0
    endtime = time.time() + 1 #Change the number in this line to change time (Seconds)
    while time.time() < endtime:
        if GPIO.event_detected(32):
            cpm = cpm + 1
    return cpm    
    
while True:
	print("Beginning of diygm script")

	#Wait for app connection
	while not os.path.exists("transfer.txt"):
		time.sleep(0.1)

	#Start detection after app connection
	pwm.start(10)  #Set duty cycle. Higher the number, higher the voltage.  10 for russian tubes, 60 for american tubes.
	
	print("Connected to app")
	file = open("transfer.txt","w")
	while os.path.exists("transfer.txt"):    
		count_rate = str(detection())

		#Place value in first line of transfer.txt    
		file.seek(0)
		file.write("new" + count_rate)
		file.truncate()
		
	print("End of diygm script (disconnected)")
	pwm.stop()
	time.sleep(3)
