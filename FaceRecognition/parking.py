from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.title('Smart Parking System')
root.iconbitmap('car.ico')
root.geometry('400x400')

C = Canvas(root, bg="blue", height=200, width=200)
filename = PhotoImage(file = r"C:\Users\LENOVO OFFICIAL\Desktop\Mini-Project-III\FaceRecognition\blur.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()





def quit_file():
    root.quit()

mybutton=Button(root,text='Exit',command=quit_file,padx=15,pady=8).place(x=170,y=250)

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

    labelName=Label(root2,text="Enter your Name : ").grid(row=5,column=0)
    labelPhone=Label(root2, text="Enter you Phone Nmber : ").grid(row=10,column=0)
    labelEmailID=Label(root2,text="Enter your Email ID : ").grid(row=15,column=0)
    labelVehicleNumber=Label(root2,text="Enter your Vehicle Number : ").grid(row=20,column=0)

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


new_user_button= Button(root, text="New User", padx=20,pady=15,command=click_new_user).place(x=150,y=25)

existing_user_button=Button(root, text="Existing User",padx=20,pady=15,command=click_existing_user).place(x=140,y=150)


root.mainloop()
