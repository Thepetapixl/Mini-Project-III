from firebase import firebase 

firebase = firebase.FirebaseApplication("https://helo-e98d4.firebaseio.com/", None)

firebase.put('/helo-e98d4/Student/-MM_ViP-WWHRvWmBNFNo',
             'Name','Bob')
print("Record Updated")