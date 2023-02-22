from flask import Flask

app = Flask(__name__)

from flask import request

@app.errorhandler(Exception)
def handle_exception(err):
  path = request.path # this var was shown to be 'favicon.ico' or 'manifest.json'
  
@app.route('/')
def hello_world(): 
    return 'Hello World!'