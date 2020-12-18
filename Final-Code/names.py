import os 
import cv2

def namelist():
    path = r'/Users/admin/VScode/Mini-Project-III-Python/Final-Code/ResFaceRecog/'
    images = []
    classNames = []

    myList = os.listdir(path)
    print(myList)

    for cls in myList:

        curImg = cv2.imread(f'{path}/{cls}')

        images.append(curImg)

        classNames.append(os.path.splitext(cls)[0])

    print(classNames)
    return classNames
