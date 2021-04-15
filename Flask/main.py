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
#     name = request.args.get('name')  #取得透過GET方式傳送來的name參數值
#     return 'Hello, {}!'.format(name)

from flask import Flask
from flask import render_template
app = Flask(__name__)
app = Flask(__name__, static_url_path='/image', static_folder='image')

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

@app.route('/img')
def img():
    return render_template('img.html')

# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/form')
# def form():
#     return '''
#         <form method="POST" action="/process">
#             <label>Input Name: <input type="text" name="name"></label>
#             <input type="submit" value="Submit">
#         </form>
#     '''

# @app.route('/process', methods=['POST'])
# def post_form():
#     name = request.form['name']
#     return 'Hello, {}!'.format(name)

# @app.route("/submit", methods=['POST'])
# def submit():
#     firstname = request.values['firstname']
#     lastname = request.values['lastname']
#     return render_template('submit.html',**locals())