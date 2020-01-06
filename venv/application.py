from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to Key Signature Kittens. Learn key signature, earn (digital) kittens!'

@app.route('/hello')
def hello_world():
  return 'Hello, World!'
  
@app.route('/about')
def about():
  return 'This is the about page'