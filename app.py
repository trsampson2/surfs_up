# import Flask dependency
from flask import Flask

#Creates the Flask instance called app
app = Flask(__name__)

#root or starting point function and the function that will run with it
@app.route('/')
def hello_world():
    return 'Hello world'

