from flask import Flask
import pymongo
from flask_pymongo import PyMongo 
import config
app = Flask(__name__)

my_client = pymongo.MongoClient(
  'mongodb+srv://Administrator:Admin101@cluster0-s2a33.mongodb.net/test?retryWrites=true&w=majority'
)

@app.route('/')
def index():
  return 'Welcome to Key Signature Kittens. Learn key signature, earn (digital) kittens!'

@app.route('/hello')
def hello_world():
  return 'Hello, World!'
  
@app.route('/about')
def about():
  return 'This is the about page'