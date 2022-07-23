import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://shantanu89:shan1234@cluster0.ql9x8os.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['MyInfo']
collection = database["sampletable"]
collection1 = database["sampletest2"]

record = collection.find()

# for i in record:
#     print(i)

# data=collection.find({"companyName":"iNeuron"})
data = collection.find({"courseOffered": {"$gt" :"E"}})

for i in data:
    print(i)
