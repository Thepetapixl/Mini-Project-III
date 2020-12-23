import pyrebase

config= {
    "apiKey" : "AIzaSyDstouhAG65tGqbjjc4t-WlVvJ3lI88n-8",
    "authDomain" : "parking-93e46.firebaseapp.com",
    "databaseURL" : "https://parking-93e46.firebaseio.com",
    "projectId" : "parking-93e46",
    "storageBucket" : "parking-93e46.appspot.com",
    "messagingSenderId" : "148522606728",
    "appId" : "1:148522606728:web:b5b48427051c28b2707f3d",
    "measurementId" : "G-165GLPGPY0"
}

firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

path_on_cloud=r"C:\Users\LENOVO OFFICIAL\Desktop\Mini-Project-III\FaceRecognition\mishalee.jpeg"
path_local="mishalee.jpeg"
#storage.child(path_on_cloud).put(path_local)

storage.child(path_on_cloud).download("test_download.jpg")