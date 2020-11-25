import pyfirmata
import time
 
pin = 13
port = '/dev/cu.usbmodem14101'
board = pyfirmata.Arduino(port)
 
while True:
    board.digital[pin].write(1)
    time.sleep(0.9) # delays for 9 seconds
    board.digital[pin].write(0)
    time.sleep(0.9) # delays for 9 seconds
 
board.exit()