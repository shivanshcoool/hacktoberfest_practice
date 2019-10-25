from firebase import firebase
firebase = firebase.FirebaseApplication('https://iot-test-119de.firebaseio.com/', None)
result = firebase.get('name', None)
print (result)