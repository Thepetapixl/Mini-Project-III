import serial #Import Serial Library
 
pin = 13
port = '/dev/cu.usbmodem14101'
arduinoSerialData = serial.Serial(port,9600) #Create Serial port object called arduinoSerialData
 
 
while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        distance = float(myData)
        print(str(distance) + " cm")