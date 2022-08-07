from heapq import merge
from unittest import result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# CREATE
# add document with auto id
db.collection('testing').add({"name":"hello","age":40})

#set document with known id
db.collection('testing').document('First').set({"name":"mike"})

#set document with auto id
db.collection('testing').document().set({"name":"mike"})

#merging
db.collection('testing').document('First').set({"age":50}, merge=True)

#documents in documents
db.collection('testing').document('First').collection('newinfo').document().set({"name":"mike"})

#READ
#getting with unknown id
result = db.collection('testing').document().get()
print(result.to_dict())

#getting with known id
result = db.collection('testing').document('First').get()
print(result.to_dict())

#all documents
docs = db.collection('testing').get()
for doc in docs:
    print(doc.to_dict())

#Query (==, !=, >, <, >=, <=, etc)
docs = db.collection('testing').where("age","==",50).get()
for doc in docs:
    print(doc.to_dict())

#UPDATE
#update with known key
db.collection('testing').document('First').update({"name":"Thomas"})

#increment
db.collection('testing').document('First').update({"age":firestore.Increment(10)})

#Update with unknown tag
#First method
# docs = db.collection('testing').get()
# for doc in docs:
#     if doc.to_dict()["name":"Manish"]:
#         key = doc.id
#         db.collection('testing').document(key).update({"name":"SIH"})

#second method
docs = db.collection('testing').where("age",">=",).get()
for doc in docs:
    key = doc.id
    db.collection('testing').document(key).update({"age":40})

#DELETE
#delete by known id
db.collection('testing').document('First').delete()

#delete field
db.collection('testing').document('First').update({"age":firestore.DELETE_FIELD})

#All delete
docs = db.collection('testing').get()
for doc in docs:
    key = doc.id
    db.collection('testing').document(key).delete()