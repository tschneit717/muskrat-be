from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "It's working!"

@app.route('/greet/')
def say_hello():
  return "Hello from the server"
