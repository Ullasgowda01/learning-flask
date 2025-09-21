from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to flask'

@app.route('/aboutUs/<name>')
def aboutUs(name):
    return f'<h1> about {name}</h1> '

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        return 'data sent'
    else :
        return 'user viewed '
    