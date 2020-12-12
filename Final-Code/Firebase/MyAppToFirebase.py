from firebase import firebase 

firebase = firebase.FirebaseApplication("https://helo-e98d4.firebaseio.com/", None)

data = {
    'Name':'Apurv',
    'Email':'xyx@gmail.com',
    'Phone Number':98983929190
}

result = firebase.post('/helo-e98d4/Student', data)
print(result)