from pymongo import MongoClient

# Function to connect to MongoDB
def connect_mongodb():
    # Replace with your MongoDB connection URL
    MONGO_CLIENT = MongoClient("mongodb://username:password@localhost:27017")
    return MONGO_CLIENT["dbname"]["profiles"]


# Function to insert profile picture into MongoDB
def insert_profile_picture(profile_data):
    collection = connect_mongodb()
    collection.insert_one(profile_data)


# Function to get profile picture from MongoDB
def get_profile_picture(user_id):
    collection = connect_mongodb()
    return collection.find_one({"user_id": user_id})
