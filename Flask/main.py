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

# from flask import Flask
# from flask import render_template
# app = Flask(__name__)
# app = Flask(__name__, static_url_path='/image', static_folder='image')

# # @app.route('/', methods=['POST', 'GET'])
# # def hello_world():
# #     return 'Hello, World!'
# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# @app.route('/loop')
# @app.route('/loop/<int:n>')
# def loop(n=3):
#     return render_template('loop.html', n=n)

# @app.route('/bgwb')
# def bgwp():
#     return render_template('bgwb.html')

# @app.route('/img')
# def img():
#     return render_template('img.html')


# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def show_table():
#     basic_info = [
#         {
#             'name': 'Amber',
#             'phone': 'Amber phone',
#             'address': 'Amber address'
#         },
#         {
#             'name': 'Peter',
#             'phone': 'Peter phone',
#             'address': 'Peter address'
#         }
#     ]
#     return render_template("index.html", data=basic_info)

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

import json
from flask import Flask, request, jsonify
app = Flask(__name__)

tasks = {
    0:{
        'id': 0,
        'description': 'todo-1',
        'done': False
    },
    1:{
        'id': 1,
        'description': 'todo-2',
        'done': False
    }
}
#定義清單計數器
take_id_coounter = 2

@app.route('/')
@app.route('/tasks/')
def get_tasks():
    res = {
        'success':True,
        'data':list(tasks.values())
    }
    return jsonify(res)

#新增todo項目
@app.route('/tasks/', methods=['POST'])
def create_task():
    #讓計數器可以被全域讀取
    global task_id_counter
    #將取得的資料以 json 載入
    body = json.loads(request.data)
    #指定拿取 description , 若無則顯示 no description
    description = body.get("description", "no description")
    #開始建立新的清單內容
    task = {"id": take_id_coounter,
            "description": description,    
            "done": False}
    #將清單內容增加回 task 清單中
    tasks[take_id_coounter] = task
    take_id_coounter += 1
    return json.dumps({
        "success": True,
        "data": task
    }), 201