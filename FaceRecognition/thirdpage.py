from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font

#third page
root1= Tk()

root1.title('Frame GUI')
root1.iconbitmap('car.ico')
root1.configure(background="black")

frame= LabelFrame(root1, text='Sign-In',padx=100, pady=140,font = "Perpetua 15 ")
frame.grid(padx=15, pady=15)
frame.configure(background="white")

labelName=Label(frame,text="Enter your Name : ",bg="white",pady=5,font = "Perpetua 15 ").grid(row=0,column=0,sticky='w')
labelPhone=Label(frame, text="Enter your Phone Nmber : ",bg="white",pady=5,font = "Perpetua 15 ").grid(row=5,column=0,sticky='w')
labelEmailID=Label(frame,text="Enter your Email ID : ",bg="white",pady=5,font = "Perpetua 15 ").grid(row=10,column=0,sticky='w')
labelVehicleNumber=Label(frame,text="Enter your Vehicle Number : ",bg="white",pady=5,font = "Perpetua 15 ").grid(row=15,column=0,sticky='w')

entryName=Entry(frame, width=30,fg="black",bg="#EFE4E4")
entryName.grid(row=0,column=5,sticky='w')

entryPhone=Entry(frame,width=30, fg="black",bg="#EFE4E4")
entryPhone.grid(row=5,column=5,sticky='w')

entryEmailID=Entry(frame,width=30, fg="black",bg="#EFE4E4")
entryEmailID.grid(row=10,column=5,sticky='w')

entryVehicleNumber=Entry(frame,width=30,fg="black",bg="#EFE4E4")
entryVehicleNumber.grid(row=15,column=5,sticky='w')

def click_next():
    implabel=Label(frame,text='All the Fields are required for successfull Login !',fg='red',bg="white").grid(row=20,column=5)
    name=entryName.get()

    entryName.delete(0,END)
    entryPhone.delete(0,END)
    entryEmailID.delete(0,END)
    entryVehicleNumber.delete(0,END)

    root2=Tk()
    root2.title('Camera')
    root2.iconbitmap('car.ico')
    root2.geometry('400x400')
    root2.configure(background="white")

    details=Label(root2, text= "Hello "+ name,fg='red',bg="white")
    details.grid(row=55,column=5)
    
    clearlabel=Label(root2,text="Camera takes Picture").grid(row=5,column=0)

def click_clear():
    entryName.delete(0,END)
    entryPhone.delete(0,END)
    entryEmailID.delete(0,END)
    entryVehicleNumber.delete(0,END)
    

nextbtn=PhotoImage(file=(r"next.png"))
nextButton = Button(frame,image=nextbtn, command=click_next, height=140, width=118, bg="white",borderwidth=0).grid(row=25,column=2)

clearbtn= PhotoImage(file="trash.png")
btn=Button(frame,image=clearbtn,command=click_clear ,height=100, width=114, bg="white",borderwidth=0).grid(row=25,column=0)

exitbtn= PhotoImage(file="exit.png")
exitButon=Button(root1,text='Exit', command=root1.quit,image=exitbtn,height=50,bg="white", width=50,borderwidth=0).place(x=18,y=550)

root.mainloop()