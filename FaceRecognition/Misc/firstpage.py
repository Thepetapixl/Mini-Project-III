from tkinter import *
from PIL import Image,ImageTk

root= Tk()

root.title('Smart Car Parking System')
root.iconbitmap('car.ico')
root.configure(background="black")


heading = Label(root, text = 'Smart Car Parking System', bg = "black", fg = "white",font = "Perpetua 24 bold").grid(row=0,column=0)

frame= LabelFrame(root,padx=100, pady=50)
frame.grid(padx=10, pady=10)
frame.configure(background="white")

deathwing=Image.open('smart.png')
image2=deathwing.resize((455,307),Image.ANTIALIAS)
Deathwing2 = ImageTk.PhotoImage(image2)
label=Label(frame,image=Deathwing2,borderwidth=0).grid(row=0,column=0)

photo= PhotoImage(file="exit.png")

btn=Button(root,image=photo,command=root.quit ,height=50 , width=50, bg="white",borderwidth=0).place(x=18,y=470)

start_button=PhotoImage(file=(r"enter.png"))
mybutton = Button(frame,image=start_button, command=open, height=100, width=100, bg="white",borderwidth=0).grid(row=1,column=0)







root.mainloop()
