from tkinter import *
from PIL import Image,ImageTk
import string
import random

lastpg = Tk()

lastpg.title("Smart Car Parking System")
lastpg.iconbitmap('car.ico')
lastpg.configure(background = "black")

frame = LabelFrame(lastpg,padx = 100, pady = 50)
frame.grid(padx = 10, pady = 10)
frame.configure(background = "white")

 
number = random.choice([1, 2, 3, 4, 6, 7, 8, 9, 10])
alpha = random.choice(string.ascii_uppercase)

ty_label = Label(frame, text = "The Parking Slot generated for your car is: " + alpha + str(number),padx = 100, pady = 120,font = "Perpetua 24 ")
ty_label.grid(row = 0,column = 0)

lastpg.mainloop()