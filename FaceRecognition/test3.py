from tkinter import *
root = Tk()

root.title("Grid GUI")
root.iconbitmap("star.ico")
root.geometry("500x300")

mylabel=Label(root,text="suupp?")
mylabel2=Label(root,text="this is line 2")

mylabel.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)

root.mainloop()