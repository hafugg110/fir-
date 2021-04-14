from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello!'

@app.route('/hello/<name>')
def helloname(name):   #宣告名help不能重複
    return 'Hello, {}!'.format(name)