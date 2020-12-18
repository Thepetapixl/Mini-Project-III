import pyrebase

def SendtoFirebase(name):
    config = {
    "apiKey": "AIzaSyCMIV3q9SYIso-A6GKOTon15iIN0adQuGs",
    "authDomain": "helo-e98d4.firebaseapp.com",
    "databaseURL": "https: // helo-e98d4.firebaseio.com",
    "projectId": "helo-e98d4",
    "storageBucket": "helo-e98d4.appspot.com",
    "messagingSenderId": "828775539430",
    "appId": "1:828775539430:web:3838dcfc5d6fce4b181127"
    }

    firebase = pyrebase.initialize_app(config)

    storage = firebase.storage()

    pathOnCloud = 'ResFaceRecog/' + name + '.jpg'
    pathLocal = '/Users/admin/VScode/Mini-Project-III-Python/Final-Code/ResFaceRecog/'+ name +'.jpg'
    storage.child(pathOnCloud).put(pathLocal)

    


# def BringFromFirebase():
    
#     config = {
#     "apiKey": "AIzaSyCMIV3q9SYIso-A6GKOTon15iIN0adQuGs",
#     "authDomain": "helo-e98d4.firebaseapp.com",
#     "databaseURL": "https: // helo-e98d4.firebaseio.com",
#     "projectId": "helo-e98d4",
#     "storageBucket": "helo-e98d4.appspot.com",
#     "messagingSenderId": "828775539430",
#     "appId": "1:828775539430:web:3838dcfc5d6fce4b181127"
#     }

#     firebase = pyrebase.initialize_app(config)

#     storage = firebase.storage()

#     pathOnCloud = 'ResFaceRecog/'
#     pathLocal = '/Users/admin/VScode/Mini-Project-III-Python/Final-Code/'
    
#     storage.child(pathOnCloud).download('/Users/admin/Desktop/download.jpg')
    
    