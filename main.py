import pymongo
client = pymongo.MongoClient("mongodb+srv://shantanu89:shan123@cluster0.ql9x8os.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.test
print(db)
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)