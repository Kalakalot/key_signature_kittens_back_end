import pymongo
import config
# from flask import jsonify
from bson.json_util import dumps

# my_client = pymongo.MongoClient(config.MONGO_URI)

mongo = pymongo.MongoClient(config.MONGO_URI, connect=False)

db = pymongo.database.Database(mongo, 'key_signatures')

collection = pymongo.collection.Collection(db, 'by_name')

try:
  print(dumps(collection.find()))  
except pymongo.errors.OperationFailure as error:
  print(error)
  quit(1)