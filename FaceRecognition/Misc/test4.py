from tkinter import *
root= Tk()

root.title("My Button")
root.iconbitmap("apple.ico")
root.geometry('500x500')
#the label is shown on the same screen when clicked the button
#fg=foreground, bg=background.You can put fg ,bg anywhere with hex color starting with #
#with padx and pady you can increase the size of the button
def myClick():
    myLabel= Label(root, text='Label is shown when clicked the button on the screen',fg="red",bg="white")
    myLabel.pack()

myButton = Button(root, text='CLick Here', command=myClick,fg="blue",bg="white",padx= 20, pady=15)
myButton.pack()


root.mainloop()