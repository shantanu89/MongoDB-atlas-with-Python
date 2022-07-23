import pymongo

client = pymongo.MongoClient("mongodb+srv://shantanu89:shan1234@cluster0.ql9x8os.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"test",
    "email" : "test@sample.com",
    "no":"12334343",
    "last":"sample"
}

d1 = {
    "name":"test",
    "email" : "test@sample.com",
    "no":"12334343",
    "last":"sample"
}

text="https://us02web.zoom.us/j/82360564107?pwd=ck9iRmlycm9EY3ZKSjlMMG5VaUh6Zz09 "
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
coll.insert_one(d1)
