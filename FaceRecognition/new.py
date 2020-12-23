import tkinter as tk
from tkinter import PhotoImage

def print_hello():
    print('hello')

root = tk.Tk()
root.geometry("960x600")

imagetest = PhotoImage(file="getstart.jpg")

button_qwer = tk.Button(root, text="asdfasdf", image=imagetest, command=print_hello)
button_qwer.pack()   # <-- don't forget to place the button in the window

root.mainloop()