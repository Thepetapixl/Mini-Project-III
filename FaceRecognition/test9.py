from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Tkinter window")
root.geometry("700x500")
root.configure(background="white")

photo= PhotoImage(file=r"dropoff.png")
btn=Button(root,image=photo,command=open ,height=500, width=500, bg="white",fg="white")
btn.pack()

root.mainloop()