from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font

#2.0 page
root3 = Tk()

root3.title('Frame GUI')
root3.iconbitmap('car.ico')
root3.configure(background = "black")

frame = LabelFrame(root3,padx = 100, pady = 80,font = "Perpetua 15 ")
frame.grid(padx = 15, pady = 15)
frame.configure(background ="white")

def click_pick_up():
    root4 = Tk()
    root4.title('User')
    root4.iconbitmap('car.ico')
    clearlabel = Label(root4,text = "Camera takes Picture").pack()



pick_up_image = PhotoImage(file = r"pickup.png")
pickup_button = Button(frame,image =  pick_up_image,command = click_pick_up() ,height = 230, width = 290, bg = "white",borderwidth=0)
pickup_button.grid(row = 0,column = 0)

blank_label = Label(frame,text = "                  ",bg = "white")
blank_label.grid(row = 0,column = 1)

drop_off_image = PhotoImage(file = r"dropoff.png")
dropoff_button = Button(frame,image = drop_off_image,command = open ,height =215, width = 295, bg = "white",borderwidth=0)
dropoff_button.grid(row = 0, column = 2)

photo3= PhotoImage(file="exit.png")
btn=Button(root3,image=photo3,command=root3.quit ,height=50 , width=50, bg="white",borderwidth=0).place(x=18,y=350)


root3.mainloop()
