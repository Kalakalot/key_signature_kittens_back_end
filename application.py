from flask import Flask, make_response
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
  response = make_response(data)
  response.headers.add('Access-Control-Allow-Origin', '*')
  print(data) 
  # return 'Welcome to Key Signature Kittens. Learn key signatures, earn (digital) kittens!'
  return response  