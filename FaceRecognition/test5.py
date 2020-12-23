from tkinter import *
root= Tk()

root.title("My Input Field")
root.iconbitmap("apple.ico")
root.geometry('500x500')

e = Entry(root, width=30, fg="red")
e.grid(row=0,column=1)

e2 = Entry(root,width=30, fg="black")
e2.grid(row=0,column=2)

#entrylabel.get will take the input from input box and display on screen
def click_me():
    myFirstName=Label(root, text="Hello"+"  "+ e.get())
    myFirstName.grid(row=3,column=1)
    e.delete(0,END)

def click_me2():
    myLastName= Label(root,text= "Hello"+"  "+e2.get())
    myLastName.grid(row=3,column=2)
    e2.delete(0,END)


myButton=Button(root, padx=20,pady=5, text="Enter your First name ", command=click_me)
myButton.grid(row=2,column=1)

myButton2=Button(root, padx=20,pady=5, text="Enter your Last name ", command=click_me2)
myButton2.grid(row=2,column=2)
"""
Code for enetring name in input box
entryFirstName=Entry(root, width=30,fg="black")
entryFirstName.grid(row=3,column=2)

entryLastName=Entry(root,width=30, fg="black")
entryLastName.grid(row=5,column=2)

def display():
    myName=Label(root, text= "Hello"+"  "+ entryFirstName.get()+"  " +entryLastName.get())
    myName.grid(row=8,column=5)
    entryFirstName.delete(0,END)
    entryLastName.delete(0,END)

enterButton=Button(root,text="OK",padx=10,pady=5,command=display)
enterButton.grid(row=7,column=5)
"""
root.mainloop()