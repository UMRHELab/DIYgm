#James Seekamp, Jeffery Xiao, Issa El-Amir, Regina Tuey
#11/16/2018
#DIY Geiger Kit for RPi Zero W


#Library Imports
import RPi.GPIO as GPIO
import bluetooth
import socket
import time

#Declares pins and disables error message
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.IN)

GPIO.setup(8, GPIO.OUT) # alarm

GPIO.setup(31, GPIO.OUT)

GPIO.setup(3, GPIO.OUT) # LED

GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.HIGH)
#

GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.HIGH)

pwm = GPIO.PWM(12, 1000) #Set the frequency and GPIO pin. Keep pin to 12.
                         #Frequency has limited effect on the voltage. 

pwm.start(10) #Set duty cycle. Higher the number, higher the voltage

GPIO.add_event_detect(32,GPIO.RISING)

#Sets alarm to off by default
GPIO.output(8, GPIO.LOW)



def detection():
    cpm = 100
    endtime = time.time() + 1 #Change the number in this line to change time (Seconds)
    while time.time() < endtime:
        if GPIO.event_detected(32):
            cpm = cpm + 1
    return cpm

#fileoption = int(input("Choose One of the Following Options \n 1: Print Data \n 2: Write to File \n"))

#graphical user interface(GUI)
#root = Tk()
#root.title("Geiger Counter")
x=0
while x < 1000000:

    x = x+1
    print(x)
    print('Counts Per Second: ', str(detection()))
    print()
    print()

    
    #if fileoption == 2:    
        #file = open("testfile.txt", "a+")
        #file.write(str(x))
        #file.write("\n")
        #file.write("Counts Per Second: ")
        #file.write(str(detection()))
        #file.write("\n")
        #file.write(str(session.stream))
    

dose = int
#doserate = ttk.Entry(mainframe, width=5, textvariable=dose).grid(column=5, row=5)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()


pwm.stop(12)

SGPIO.cleanup()
#
    
