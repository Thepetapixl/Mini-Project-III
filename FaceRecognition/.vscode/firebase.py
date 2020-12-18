from firebase import firebase

firebase = firebase.FirebaseApplication("https://parking-93e46.firebaseio.com/",None)



data={

    'Customer Name': 'Mishalee Lambat',
    'Customer Email ID': 'mishaleelambat31@gmail.com',
    'Customer Mobile Number': 123456789,
    'Costomer Vehicle Number': 'AP5164',
}
result= firebase.post('/parking-93e46/SmartDatabase',data)
print(result)