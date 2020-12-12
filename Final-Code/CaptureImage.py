import cv2 # importing cv2 library
import ImageFirebase
import time

def Capture(name):

    cam = cv2.VideoCapture(0)
    
    ImageTaken = 0

    while True:
        if ImageTaken == 0 :
            
            count = 0

            ret, img = cam.read()

            cv2.imshow("Test", img)

            if not ret:
                break

            k = cv2.waitKey(1)

            if k % 256 == 27:
                #For Esc key
                print("Close")
                break

            elif k % 256 == 32:
                #For Space key
            
                file = '/Users/admin/VScode/Mini-Project-III-Python/Final-Code/ResFaceRecog/' + name + '.jpg'
                cv2.imwrite(file, img)
                
                print("Image " + str(count) + "saved")
                
                # time.sleep(5)
                
                # ImageFirebase.SendtoFirebase(name)
                
                count += 1
                ImageTaken += 1
                
        elif ImageTaken == 1:
            
            break

    cam.release
    cv2.destroyAllWindows
    
    
name = "Apurv Vidhate"
Capture(name) # Only Uncomment this line when you are using the code independently 