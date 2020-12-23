from tkinter import *
root= Tk()

root.title('My Radio Buttons')
root.iconbitmap('apple.ico')
root.geometry('600x600')

q=IntVar() 
q.get()
q.set(2)

def click_me(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

Radiobutton(root,text="Option 1", variable=q, value=1).pack()
Radiobutton(root,text="Option 2", variable=q, value=2).pack()
Radiobutton(root,text="Option 3", variable=q, value=3).pack()
Radiobutton(root,text="Option 4", variable=q, value=4).pack()

my_label=Label(root,text=q.get().pack()

mybutton=Button(root, text="Submit!!", command=lambda value: click_me(q.get())
mybutton.pack()

root.mainloop()