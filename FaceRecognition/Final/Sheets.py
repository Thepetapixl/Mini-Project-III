import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


path = r'/Users/admin/VScode/Mini-Project-III-Python/FaceRecognition/2020/Attendance'
images = []
classNames = []

myList = os.listdir(path)
print(myList)

for cls in myList:

    curImg = cv2.imread(f'{path}/{cls}')

    images.append(curImg)

    classNames.append(os.path.splitext(cls)[0])

print(classNames)

def findEncodings(images):

    encodeList = []

    for img in images:
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]

        encodeList.append(encode)
    
    return encodeList

def MarkAttendance(name):

    with open(r'/Users/admin/VScode/Mini-Project-III-Python/FaceRecognition/Final/Previous/Attendance.csv', 'r+') as f:

        myDataList = f.readlines()
        nameList = []

        # print(myDataList)

        for line in myDataList:

            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            
            now = datetime.now()

            dateString = now.strftime('%H:%M:%S')

            f.writelines(f'\n{name},{dateString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)

    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodingsCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodingsCurFrame,facesCurFrame):

        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)

        FaceDist = face_recognition.face_distance(encodeListKnown, encodeFace)

        # print(FaceDist)

        matchIndex = np.argmin(FaceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)

            y1, x2, y2 ,x1 = faceLoc
            y1 ,x2 ,y2 ,x1 = y1 * 4,x2 * 4,y2 * 4,x1 * 4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.rectangle(img,(x1,y2 - 35),(x2,y2),(0,255,0),cv2.FILLED)

            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255), 2)

            MarkAttendance(name)
    
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)








# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255),2)

# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3],faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),(255,0,255),2)

# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDistance = face_recognition.face_distance([encodeElon], encodeTest)

