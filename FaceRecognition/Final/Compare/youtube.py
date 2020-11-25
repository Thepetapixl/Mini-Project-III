import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file(r"/Users/admin/VScode/Mini-Project-III-Python/FaceRecognition/2020/Compare/Elon_Musk.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file(r"/Users/admin/VScode/Mini-Project-III-Python/FaceRecognition/2020/Compare/Elon_Test.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3],faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDistance = face_recognition.face_distance([encodeElon], encodeTest)

print(results, faceDistance)
cv2.putText(imgTest,f'{results}{round(faceDistance[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)

cv2.waitKey(0)



# def MarkAttendance(name):

#     with open(r'/Users/admin/VScode/Mini-Project-III-Python/FaceRecognition/2020/Attendance/Attendance.csv', 'r+') as f:

#         myDataList = f.readlines()
#         nameList = []

#         print(myDataList)

#         for line in myDataList:

#             entry = line.split(',')
#             nameList.append(entry[0])

#         if name not in nameList:
            
#             now = datetime.now()

#             dateString = now.strftime('%H:%M:%S')

#             f.writelines(f'\n{name},{dateString}')