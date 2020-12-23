#login
from tkinter import *
window = Tk()
window.title("LOGIN")
heading = Label(window, text = 'Smart Car Parking System', bg = "blue", fg = "white",
                   font = "Times 24 bold italic").pack()
l1 = Label(window,text = 'USERNAME : ')
l2 = Label(window,text = 'PASSWORD : ')
t1 = Entry(window, textvariable = StringVar())
t2 = Entry(window,  show = '*', textvariable = StringVar())
def click_new_user():
    root1=Tk()
    root1.title('New User')
    root1.iconbitmap('car.ico')
    root1.geometry('400x400')


    labelName=Label(root1,text="Enter your Name : ").grid(row=5,column=0)
    labelPhone=Label(root1, text="Enter you Phone Nmber : ").grid(row=10,column=0)
    labelEmailID=Label(root1,text="Enter your Email ID : ").grid(row=15,column=0)
    labelVehicleNumber=Label(root1,text="Enter your Vehicle Number :").grid(row=20,column=0)


    entryName=Entry(root1, width=30,fg="black")
    entryName.grid(row=5,column=20)

    entryPhone=Entry(root1,width=30, fg="black")
    entryPhone.grid(row=10,column=20)

    entryEmailID=Entry(root1,width=30, fg="black")
    entryEmailID.grid(row=15,column=20)

    entryVehicleNumber=Entry(root1,width=30,fg="black")
    entryVehicleNumber.grid(row=20,column=20)

    def display():
        myName=Label(root1, text= "Hello"+"  "+ entryName.get()+"  " +entryEmailID.get())
        myName.grid(row=100,column=5)
        entryName.delete(0,END)
        entryEmailID.delete(0,END)
        entryVehicleNumber.delete(0,END)


    enterButton=Button(root1,text="Submit",padx=10,pady=5,command=display)
    enterButton.place(x=150, y=150)

def click_existing_user():
    root2=Tk()
    root2.title('Existing User')
    root2.iconbitmap('car.ico')
    root2.geometry('400x400')

    labelName=Label(root2,text="Enter your Name : ").pack()
    labelPhone=Label(root2, text="Enter you Phone Nmber : ").pack()
    labelEmailID=Label(root2,text="Enter your Email ID : ").pack()
    labelVehicleNumber=Label(root2,text="Enter your Vehicle Number : ").pack()

    entryName=Entry(root2, width=30,fg="black")
    entryName.grid(row=5,column=20)

    entryPhone=Entry(root2,width=30, fg="black")
    entryPhone.grid(row=10,column=20)

    entryEmailID=Entry(root2,width=30, fg="black")
    entryEmailID.grid(row=15,column=20)

    entryVehicleNumber=Entry(root2,width=30,fg="black")
    entryVehicleNumber.grid(row=20,column=20)

    def display():
        myName=Label(root2, text= "Hello"+"  "+ entryName.get()+"  " +entryEmailID.get())
        myName.grid(row=55,column=5)
        entryName.delete(0,END)
        entryEmailID.delete(0,END)
        entryVehicleNumber.delete(0,END)


    enterButton=Button(root2,text="Verify",padx=10,pady=5,command=display)
    enterButton.place(x=150, y=150)

b1 = Button(window,text = "Sign-in", bg = "blue", fg = "red", font = "none", command = click_existing_user)
b2 = Button(window,text = "NEW USER", bg = "grey", fg = "blue", font = "none", command = click_new_user)
b3 = Button(window,text = "EXIT", bg = "yellow", fg = "orange", font = "none", command = window.destroy)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
b2.pack()
b3.pack()
window.mainloop()