from firebase import firebase 

firebase = firebase.FirebaseApplication("https://helo-e98d4.firebaseio.com/", None)

result = firebase.get('/helo-e98d4/Student','')
print(result)