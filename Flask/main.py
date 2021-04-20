from flask import Flask, request, jsonify, render_template, make_response
import cv2
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def index():
    # 顯示表單
    return render_template('form.html')

#讀取圖片
# @app.route('/', methods=['POST'])
# def process():
#     # 取得上傳的圖片
#     file1 = request.files['image1']
#     # 讀取檔案內容
#     file1_content = file1.read()
#     # 將檔案內容轉為 Numpy Array
#     npimg1 = np.fromstring(file1_content, np.uint8)
#     # 將 Numpy Array 進行圖像解碼
#     bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)

#     return jsonify(bgr1.shape)

#回傳圖片 這裡有問題
# @app.route('/', methods=['POST'])
# def process():
#     # 取得上傳的圖片
#     file1 = request.files['image1']
#     # 讀取檔案內容
#     file1_content = file1.read()
#     # 將檔案內容轉為 Numpy Array
#     npimg1 = np.fromstring(file1_content, np.uint8)
#     # 將 Numpy Array 進行圖像解碼
#     bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
#     _, buffer = cv2.imencode('.jpg', bgr1)
#     response = make_response(buffer.tobytes())
#     response.mimetype = 'image/jpg'

#     return response
#處理圖片
# @app.route('/', methods=['POST'])
# def process():
#     # 取得上傳的圖片
#     file1 = request.files['image1']
#     # 讀取檔案內容
#     file1_content = file1.read()
#     # 將檔案內容轉為 Numpy Array
#     npimg1 = np.fromstring(file1_content, np.uint8)
#     # 將 Numpy Array 進行圖像解碼
#     bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
    
#     _ , buffer = cv2.imencode('.jpg', bgr1)
#     response = make_response(buffer.tobytes())
#     response.mimetype = 'image/jpg'

#     return response

#處理圖片
@app.route('/', methods=['POST'])
def process():
    # 取得上傳的圖片
    file1 = request.files['image1']
    # 讀取檔案內容
    file1_content = file1.read()
    # 將檔案內容轉為 Numpy Array
    npimg1 = np.fromstring(file1_content, np.uint8)
    # 將 Numpy Array 進行圖像解碼
    # _ , buffer = cv2.imencode('.jpg', bgr1)
    # response = make_response(buffer.tobytes())
    # response.mimetype = 'image/jpg'

    rgb1 = cv2.cvtColor(bgr1, cv2.COLOR_BGR2RGB)
    height, width = rgb1.shape[:2]
    radius = int(min(height, width) * 0.48)
    thickness = int(min(height, width) * 0.02)
    cv2.circle(rgb1, (int(width / 2), int(height / 2)), radius, (255, 0, 0), thickness)
    bgr1 = cv2.cvtColor(rgb1, cv2.COLOR_BGR2RGB)

    return response

#4/19
# import json
# from flask import Flask, request, jsonify
# app = Flask(__name__)

# tasks = {
#     0:{
#         'id': 0,
#         'description': 'todo-1',
#         'done': False
#     },
#     1:{
#         'id': 1,
#         'description': 'todo-2',
#         'done': False
#     }
# }
# #定義清單計數器
# task_id_counter = 2
# # 新增一個 route

# @app.route('/')
# @app.route('/tasks/')
# def get_tasks():
#     res = {
#         'success':True,
#         'data':list(tasks.values())
#     }
#     return jsonify(res)

# #新增todo項目
# @app.route('/tasks/', methods=['POST'])
# def create_task():
#     #讓計數器可以被全域讀取
#     global task_id_counter
#     #將取得的資料以 json 載入
#     body = json.loads(request.data)
#     #指定拿取 description , 若無則顯示 no description
#     description = body.get("description", "no description")
#     #開始建立新的清單內容
#     task = {"id": task_id_counter,
#             "description": description,    
#             "done": False}
#     #將清單內容增加回 task 清單中
#     tasks[task_id_counter] = task
#     task_id_counter += 1
#     return json.dumps({
#         "success": True,
#         "data": task
#     }), 201
#     #取得特定 id 內容

# @app.route('/tasks/<int:task_id>/')
# def get_task(task_id):
#     task = tasks.get(task_id)
#     if not task:
#         return json.dumps({
#             "success": False,
#             "error": "Task not found"
#         }), 404
#     return json.dumps({           
#         "success": True,
#         "data": task
#     }), 200

# #更新特定id內容
# @app.route('/tasks/<int:task_id>/' , methods=['POST'])
# def update_task(task_id):
#     task = tasks.get(task_id)
#     if not task:
#         return json.dumps({
#                 "success": False,
#                 "error": "Task not found"
#         }), 404
#     body = json.loads(request.data)
#     description = body.get("description")
#     if description:
#         task['description'] = description
#     task['done'] = body.get("done", False)
#     return json.dumps({
#         "success": True,
#         "data": task
#     }), 200

# #刪除特定 id 清單
# @app.route('/tasks/<int:task_id>/', methods=['DELETE'])
# def delete_task(task_id):
#     task = tasks.get(task_id)
#     if not task:
#         return json.dumps({
#              "success": False,
#              "error": "Task not found"
#         }), 404
#     del tasks[task_id]
#     return json.dumps({
#         "success": True,
#         "data": task
#     }), 200

#4/15
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

