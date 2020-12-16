# This is the main file where everything takes place

# Importing the necessary libraries 

from tkinter import *
from PIL import Image,ImageTk

# importing our other python files 

import Sheets
import CaptureImage
import FinalScreen
import names

path = r"/Users/admin/Mini-Project-III/Resources/"

# Main Screen i.e. first Screen when the code is executed 

window = Tk()

# All the properties of the first screen is set here:

window.title('Smart Car Parking System')
window.iconbitmap(path + 'car.ico')
window.configure(background = "black")

heading = Label(window, text = 'Smart Car Parking System', bg = "black", fg = "white",font = "Perpetua 24 bold")
heading.grid(row = 0,column = 0)

frame = LabelFrame(window,padx = 100, pady = 50)
frame.grid(padx = 10, pady = 10)
frame.configure(background = "white")

deathwing = Image.open(path + 'smart.png')
image = deathwing.resize((455,307),Image.ANTIALIAS)
Deathwing = ImageTk.PhotoImage(image)
imagelabel = Label(frame,image = Deathwing,borderwidth = 0)
imagelabel.grid(row = 0,column = 0)


# Start button function starts here:

def click_start():
    window.destroy()
    
    #Second page starts here (New and Existing user)
    
    root = Tk()
    root.title('User')
    root.iconbitmap(path + 'car.ico')
    root.configure(background = "black")

    new_frame = LabelFrame(root,padx = 100, pady = 80)
    new_frame.grid(padx = 15, pady = 15)
    new_frame.configure(background = "white")
    
    # A check / tag to see if it is working properly
    
    print("This has been passsed")  
    
    
    # New User button function starts here:
    
    def click_new_user():
        root.destroy()
        
        # Third page.new user starts here (Details for Registration)
        
        root1 = Tk()

        root1.title('New User')
        root1.iconbitmap(path + 'car.ico')
        root1.configure(background = "black")

        frame = LabelFrame(root1, text = 'Sign-In',padx = 100, pady = 120,font = "Perpetua 15 ")
        frame.grid(padx = 15, pady = 15)
        frame.configure(background = "white")

        labelName = Label(frame,text = "Enter your Name : ",bg = "white",pady = 5,font = "Perpetua 15 ")
        labelName.grid(row = 0,column = 0,sticky = 'w')
        labelPhone = Label(frame, text = "Enter your Phone Number : ",bg = "white",pady = 5,font = "Perpetua 15 ")
        labelPhone.grid(row = 5,column = 0,sticky = 'w')
        labelEmailID = Label(frame,text = "Enter your Email ID : ",bg = "white",pady = 5,font = "Perpetua 15 ")
        labelEmailID.grid(row = 10,column = 0,sticky = 'w')
        labelVehicleNumber = Label(frame,text = "Enter your Vehicle Number : ",bg = "white",pady = 5,font = "Perpetua 15 ")
        labelVehicleNumber.grid(row = 15,column = 0,sticky = 'w')


        # All the data is entered and saved here:
        
        
        entryName = Entry(frame, width = 30,fg = "black",bg = "#EFE4E4")
        entryName.grid(row = 0,column = 5,sticky = 'w')

        entryPhone = Entry(frame,width = 30, fg = "black",bg = "#EFE4E4")
        entryPhone.grid(row = 5,column = 5,sticky = 'w')

        entryEmailID = Entry(frame,width = 30, fg = "black",bg = "#EFE4E4")
        entryEmailID.grid(row = 10,column = 5,sticky = 'w')

        entryVehicleNumber = Entry(frame,width = 30,fg = "black",bg = "#EFE4E4")
        entryVehicleNumber.grid(row = 15,column = 5,sticky = 'w')
        
        # Next Button function start here which is linked to Capturing the face of the new user

        def click_next():
            label = Label(frame,text = 'All the Fields are required for successfull Login !',fg = 'red',bg = "white")
            label.grid(row = 20,column = 5)
            
            # Stores the name for future reference 
            
            name = entryName.get()

            # Clears the fields
            
            entryName.delete(0,END)
            entryPhone.delete(0,END)
            entryEmailID.delete(0,END)
            entryVehicleNumber.delete(0,END)

            # The file CaptureImage.py executes here 
            
            CaptureImage.Capture(name)
            
            # Moves to the park car option
            
            FinalScreen.FinalScreenRegister(name)
            
            
        # Clear button incase the user made a mistake in the form filling
        
        def click_clear():
            entryName.delete(0,END)
            entryPhone.delete(0,END)
            entryEmailID.delete(0,END)
            entryVehicleNumber.delete(0,END)
            
        # A Tag / Check to see if the code is working till here:
            
        print("2nd Pass")
        
        # Next button Properties:
        
        next_button_image = PhotoImage(file = path + "next.png")
        nextButton = Button(frame,image = next_button_image, command = click_next, height = 140, width = 118, bg = "white",borderwidth = 0)
        nextButton.image = next_button_image
        nextButton.grid(row = 25,column = 2)
        
        # Clear Button Properties:

        clearbtn = PhotoImage(file = path + "trash.png")
        btn = Button(frame,image = clearbtn,command = click_clear ,height = 100, width = 114, bg = "white",borderwidth = 0)
        btn.image = clearbtn
        btn.grid(row = 25,column = 0)
        
        # Exit button Properties:
        
        exit_img = PhotoImage(file = path + "exit.png")
        exit_button = Button(root1,text = 'Exit', command = root1.quit,image = exit_img,height = 50,bg = "white", width = 50,borderwidth = 0)
        exit_button.image = exit_img
        exit_button.place(x = 18,y = 490)
       
        # Third page.new user function ends here
    

    # Exisiting User Function starts here 

    def click_existing_user():
        
        # We destroy the first page here
        
        root.destroy()
        
        #  New page for Pick Up and Drop Off starts here 
        
        root3 = Tk() 
        root3.title('Existing User')
        root3.iconbitmap(path + 'car.ico')
        root3.configure(background = "black")

        frame = LabelFrame(root3,padx = 70, pady = 100,font = "Perpetua 15 ")
        frame.grid(padx = 15, pady = 15)
        frame.configure(background = "white")
        
        # Functions for Pick Up and drop off

        def click_pick_up():
            
            # Calls the function FaceRec() file from Sheets.py
            root3.destroy()
                
            name = Sheets.FaceRec() 
            FinalScreen.finalScreenPickUp(name)
                        
        def click_drop_off():
            
            # Calls the function FaceRec() file from Sheets.py
            
            name = Sheets.FaceRec() 
            FinalScreen.finalScreenDropOff(name)
                        
        # Properties for Pick UP 

        pick_up_image = PhotoImage(file = path + "pickup.png")
        pickup_button = Button(frame,image =  pick_up_image,command = click_pick_up ,height = 230, width = 290, bg = "white",borderwidth=0)
        pickup_button.image = pick_up_image
        pickup_button.grid(row = 0,column = 0)

        blank_label = Label(frame,text = "                  ",bg = "white")
        blank_label.grid(row = 0,column = 1)
        
        # Properties for Drop Off

        drop_off_image = PhotoImage(file = path + "dropoff.png")
        dropoff_button = Button(frame,image = drop_off_image,command = click_drop_off ,height = 215, width = 295, bg = "white",borderwidth=0)
        dropoff_button.image = drop_off_image
        dropoff_button.grid(row = 0, column = 2)
        
        # Properties for Exit 

        exit_img = PhotoImage(file = path + "exit.png")
        exit_button = Button(root3,image = exit_img,command = root3.quit ,height = 50 , width = 50, bg = "white",borderwidth = 0)
        exit_button.image = exit_img
        exit_button.place(x = 18,y = 350)
        
        
        # Third page.existing user ends here
    
    # New user Properties:
    
    new_user_img = PhotoImage(file = path + "new-user.png")    
    new_user_button = Button(new_frame, text = "New User",image = new_user_img , command = click_new_user,compound = TOP,borderwidth = 0,bg = "white",font = "Perpetua 15 ")
    new_user_button.image = new_user_img
    new_user_button.grid(row = 0,column = 0)

    blank_label = Label(new_frame,text = "             ",bg = "white")
    blank_label.grid(row = 0,column = 1)
    
    # Existing User Properties:

    existing_user_img = PhotoImage(file = path + "face-detection.png")
    existing_user_button = Button(new_frame, text = "Existing User",image = existing_user_img,command = click_existing_user,compound = TOP,borderwidth = 0,bg = "white",font = "Perpetua 15 ")
    existing_user_button.image = existing_user_img
    existing_user_button.grid(row = 0,column = 2)
    
    # Exit Properties:

    exit_img = PhotoImage(file = path + "exit.png")
    exit_button = Button(root,image = exit_img,command = root.quit ,height = 50 , width = 50, bg = "white",borderwidth = 0)
    exit_button.image = exit_img
    exit_button.place(x=18,y=270) 
    
    # 2nd page ends here
    

# Start Button Properties:
    
start_img = PhotoImage(file = path + "start.png")
start_button = Button(frame,image = start_img, command = click_start, height = 120, width = 190, bg = "white",borderwidth = 0)
start_button.image = start_img
start_button.grid(row = 1,column = 0)

# Exit Button Properties:

exit_img = PhotoImage(file = path + "exit.png")
exit_button = Button(window,image = exit_img,command = window.quit ,height = 50 , width = 50, bg = "white",borderwidth = 0)
exit_button.image = exit_img
exit_button.place(x = 18,y = 490)

window.mainloop()

# Code Ends here