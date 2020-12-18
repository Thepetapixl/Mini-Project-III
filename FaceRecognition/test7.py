from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *

root=Tk()
root.geometry('500x400')
root.configure(background="white")

root.title('Photo Viewer')
root.iconbitmap('apple.ico')

def quit_file():
    root.quit()

deathwing=Image.open('download.jpg')
image2=deathwing.resize((150,150),Image.ANTIALIAS)
Deathwing2 = ImageTk.PhotoImage(image2)
label=Label(root,image=Deathwing2).pack()

start_button=PhotoImage(file=r"C:\Users\LENOVO OFFICIAL\Desktop\Mini-Project-III\FaceRecognition\start.png")

def callback():
    my_label=Label(root,text=" WELCOME TO SMART PARKING SYSTEM ! ").pack()


button = Button(image=start_button, command=callback, width=190).pack()

mybutton=Button(root,text='Exit',command=quit_file).pack()

root.mainloop()