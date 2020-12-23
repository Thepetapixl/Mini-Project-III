from tkinter import *
from PIL import Image,ImageTk
#second page
root = Tk()

root.title('User')
root.iconbitmap('car.ico')
root.configure(background="black")

new_frame= LabelFrame(root,padx=100, pady=70)
new_frame.grid(padx=15, pady=15)
new_frame.configure(background="white")
existing_user_img= PhotoImage(file="face-detection.png")

new_user_img= PhotoImage(file="new-user.png")

new_user_button= Button(new_frame, text="New User",image=new_user_img,command=open,compound=TOP,borderwidth=0,bg="white").grid(row=0,column=0)

existing_user_button=Button(new_frame, text="Existing User",image=existing_user_img,command=open,compound=TOP,borderwidth=0,bg="white").grid(row=0,column=1)


photo3= PhotoImage(file="exit.png")
btn=Button(root,image=photo3,command=root.quit ,height=50 , width=50, bg="white",borderwidth=0).place(x=18,y=270)
root.mainloop()