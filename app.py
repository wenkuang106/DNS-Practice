## importing the flask package 
from flask import Flask

## creating a Flask App with the name app 
app = Flask(__name__)

## this is the index page where users will first land on 
@app.route('/')
def home():
    return 'Hello world!'

## this is the about page
@app.route('/about/')
def about():
    return ' This is the Flask-Part 1 Assignment created for HHA 504'

## this is the help page 
@app.route('/help/')
def help():
    return "please ask google for help since I asked google for help too"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)