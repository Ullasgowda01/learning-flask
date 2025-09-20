from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to flask'

@app.route('/aboutUs')
def aboutUs():
    return 'about me '

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        return 'data sent'
    else :
        return 'user viewed '
    