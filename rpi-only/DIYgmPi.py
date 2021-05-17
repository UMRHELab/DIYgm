#James Seekamp, Jeffery Xiao, Issa El-Amir, Regina Tuey, Max Li, Andrew Kent
#2/6/2021
#DIY Geiger Kit for RPi Zero W


#Library Imports
import RPi.GPIO as GPIO
import bluetooth
import socket
import time

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

pwm = GPIO.PWM(12, 1000) #Set the frequency and GPIO pin. Keep pin to 12.
                         #Frequency has limited effect on the voltage. 

pwm.start(10) #Set duty cycle. Higher the number, higher the voltage.  10 for russian tubes, 60 for american tubes.

GPIO.add_event_detect(32,GPIO.RISING)


def detection():
    cpm = 100
    endtime = time.time() + 1 #Change the number in this line to change time (Seconds)
    while time.time() < endtime:
        if GPIO.event_detected(32):
            cpm = cpm + 1
    return cpm


x=0
while x < 1000000:

    x = x+1
    print(x)
    print('Counts Per Second: ', str(detection()))
    print()
    print()
    

dose = int



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()


pwm.stop(12)

SGPIO.cleanup()
    
