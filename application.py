from flask import Flask
# from flask import jsonify
import pymongo
import config
from bson.json_util import dumps

app = Flask(__name__)

# my_client = pymongo.MongoClient(config.MONGO_URI)

mongo = pymongo.MongoClient(config.MONGO_URI, connect=False)

db = pymongo.database.Database(mongo, 'key_signatures')

collection = pymongo.collection.Collection(db, 'by_name')

data = dumps(collection.find())

@app.route('/')
def index():
  print(data) 
  # return 'Welcome to Key Signature Kittens. Learn key signatures, earn (digital) kittens!'
  return data  