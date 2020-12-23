import pyfirmata
import time
 
pin = 13
port = '/dev/cu.usbmodem14101'
board = pyfirmata.Arduino(port)
 
it = pyfirmata.util.Iterator(board)
it.start()
 
board.digital[10].mode = pyfirmata.INPUT
 
while True:
	sw = board.digital[10].read()
 
	if sw is True:
		board.digital[13].write(1)
	else:
		board.digital[13].write(0)
	time.sleep(0.1)
