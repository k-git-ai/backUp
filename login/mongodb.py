import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["logindatabase"]
mycol = mydb["person"]
# mycol.drop()
'''print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
mylist = [
  {"name": "Amy", "email": "amy@xyz.com", "password": "12345"},
  {"name": "Hannah", "email": "hanna@xyz.com", "password": "12345"},
  {"name": "Michael", "email": "michael@xyz.com", "password": "12345"},
  {"name": "Sandy", "email": "sandy@xyz.com", "password": "12345"},
  {"name": "Betty", "email": "betty@xyz.com", "password": "12345"},
  {"name": "Richard", "email": "richard@xyz.com", "password": "12345"},
  {"name": "Susan", "email": "susan@xyz.com", "password": "12345"},
  {"name": "Vicky", "email": "vicky@xyz.com", "password": "12345"},
  {"name": "Ben", "email": "ben@xyz.com", "password": "12345"},
  {"name": "William", "email": "william@xyz.com", "password": "12345"},
  {"name": "Chuck", "email": "chuck@xyz.com", "password": "12345"},
  {"name": "Viola", "email": "viola@xyz.com", "password": "12345"}
]

x = mycol.insert_many(mylist)'''

# print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# for x in mycol.find():
#     print(x)
