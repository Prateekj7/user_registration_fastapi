from pymongo import MongoClient

# Function to connect to MongoDB
def connect_mongodb():
    # Replace with your MongoDB connection URL
    # MONGO_CLIENT = MongoClient("mongodb://root:password$@127.0.0.1:27017")
    MONGO_CLIENT = MongoClient()
    return MONGO_CLIENT["dbname"]["profiles"] # This is returning Mongo client with DB - dbname
                                                # and collection profiles


# Function to insert profile picture into MongoDB
def insert_profile_picture(profile_data):
    collection = connect_mongodb()
    collection.insert_one(profile_data)


# Function to get profile picture from MongoDB
def get_profile_picture(user_id):
    collection = connect_mongodb()
    return collection.find_one({"user_id": user_id})
