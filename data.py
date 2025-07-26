from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access database and collection
db = client['resume_db']
collection = db['resumes']

# Print all documents in the collection
for doc in collection.find():
    print(doc)