# As per CMDA regulations, the minimum size of a car parking space is 2.5 m (8'2”) wide and 5 m (16'4”) long.
# Jan 25, 2013


import serial #Import Serial Library
import time
 

pin = 13
port = '/dev/cu.usbmodem14101'
arduinoSerialData = serial.Serial(port,9600) #Create Serial port object called arduinoSerialData
distanceFromSensor = 75     
flag = 0
lengthOfParking = 500                        # 5 meters = 500 cm
 
def Values():

    while (1==1):
        if (arduinoSerialData.inWaiting()>0):
            myData = arduinoSerialData.readline()

        # distance = float(myData)
        # print(float(myData))

            if (float(myData) <= distanceFromSensor):
                print("Car Detected")
                Flag = 1
            else:
                print("No Car is Present")
                Flag = 0

            distance = float(myData)
            print(str(distance) + " cm")

    time.sleep(0.5)

while True:
    Values()

# New user -> auth -> no of spaces -> check if car has reached

# existing user -> check in(entrance) -> no of spaces -> check if car has reached 
#          | 
#          |
#          -> Pickup -> check if car has left 