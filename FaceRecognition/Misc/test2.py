from tkinter import *
root= Tk()

root.title("My First GUI")
root.iconbitmap("apple.ico")
root.geometry("300x200")

mylabel=Label(root,text="Hi !" ).pack()
mylabel2=Label(root,text="how you doing?").pack()


root.mainloop()