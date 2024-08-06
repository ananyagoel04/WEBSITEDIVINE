from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb+srv://ananyagoel:hUAgixIgEEEPPiTJ@dwswebcluster.uyuegnq.mongodb.net/')
db = client['DWSWEBCLUSTER']
counter = db['counter']

def get_next_id(collection_name):
    """
    Get the next ID for a given collection.
    """
    result = counter.find_one_and_update(
        {'_id': collection_name},
        {'$inc': {'seq': 1}},
        return_document=True,
        upsert=True
    )
    return result['seq']
