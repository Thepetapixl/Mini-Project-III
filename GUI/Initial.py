from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Modern Parking")
logo_set = PhotoImage(file = 'Logo.png') 
root.iconphoto(False, logo_set)
root.geometry("500x500")


def N_User():
    new = Toplevel()
    new.title("New User")
    root.iconbitmap("Logo1.ico")
    new.geometry("500x500")
    my_label1 = Label(root, text ="Parking Spots left are: 01", fg="Violet").grid(row = 1, column = 5)
    i_button1 = Button(new, text = "Exit", command = new.quit).grid(row = 1, column=5)
    
def E_User():
    ash = Toplevel()
    ash.title("Exisiting User")
    root.iconbitmap("Logo1.ico")
    new.geometery("500x500")
    my_label2 = Label(root, text ="You may take the Car", fg="Violet").grid(row = 4, column = 4)
    i_button2 = Button(new, text = "Exit", command = new.quit).grid(row = 1, column=5)
    
    
def popup():
    messagebox.askyesno("Confirmation", "Sure ?")
    

button1 = Button(root, text= "New User", padx = 5, pady =5, bg = "Yellow", fg ="Blue", command = N_User).grid(row=4, column = 6)
button2 = Button(root, text="Exisisting User", padx = 5, pady= 5, bg ="White", fg = "Black", command = E_User).grid(row=6, column=6)

    
but = Button(root, text ="Confirm", command = popup).grid(row=8, column =6)

root.mainloop()