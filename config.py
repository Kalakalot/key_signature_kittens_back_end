import pymongo
import json
from bson.json_util import dumps


MONGO_URI='mongodb+srv://Administrator:Admin101@cluster0-s2a33.mongodb.net/test?retryWrites=true&w=majority'

PRIVATE_KEY='af711037-d223-402e-b9fd-57636a205b7c'

PUBLIC_KEY='YROMGKED'

mongo = pymongo.MongoClient(MONGO_URI, connect=False)

db = pymongo.database.Database(mongo, 'key_signatures')

collection = pymongo.collection.Collection(db, 'by_name')

