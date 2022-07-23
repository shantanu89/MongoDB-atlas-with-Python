import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://shantanu89:shan1234@cluster0.ql9x8os.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

database = client['Inventory']
collection = database["table"]

# collection.insert_many(data)

# record = collection.find()

# record = collection.find({"status":"A"})

# record = collection.find({"status": {'$in':['A','P']}})  # or condition

# record = collection.find({"status": {'$gt':'B'}})   #gt greater than

# record = collection.find({"qty":100})

# record = collection.find({"qty": {'$gte':75}})  # gte greate than equal

# record = collection.find({"item":"sketch pad","qty":95})

# record = collection.find({"item":"sketch pad","qty":{"$gte":75}})

# record = collection.find({"$or":[{"item":"sketch pad"},{"qty":{"$gte":75}}]}) # or condition check

# collection.update_one({'item': 'canvas'},{'$set':{'item': 'test'}})  # data updation operation

collection.delete_one({'item': 'test'})  # data delete operation

data1 = collection.find()

# for i in record:
#     print(i)

for i in data1:
    print(i)
