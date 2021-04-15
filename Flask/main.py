# from flask import Flask
# app = Flask(__name__)

# # @app.route('/')
# # def hello_world():
# #     return 'Hello, World!'

# # @app.route('/hello')
# # def hello():
# #     return 'Hello!'

# # @app.route('/hello/<name>')
# # def helloname(name):   #宣告名help不能重複
# #     return 'Hello, {}!'.format(name)

# @app.route('/hello', defaults={'name': 'Someone'})
# @app.route('/hello/<name>')
# def helloname1(name):
#     return 'Hello, {}!'.format(name)

# @app.route('/', methods=['POST', 'GET'])
# def hello_world1():      #宣告名hello_world不能重複
#     return 'Hello, World!'

# @app.route('/<int:num>')
# def get_integer(num):
#     return 'Integer: {}'.format(num)
# @app.route('/<float:num>')
# def get_float(num):
#     return 'Float: {}'.format(num)

# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/query')
# def query():
#     name = request.args.get('name')
#     return 'Hello, {}!'.format(name)

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello, World!'
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/loop')
@app.route('/loop/<int:n>')
def loop(n=3):
    return render_template('loop.html', n=n)

@app.route('/bgwb')
def bgwp():
    return render_template('bgwb.html')