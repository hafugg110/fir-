import json
from flask import Flask, request, render_template
import db

DB = db.DatabaseDriver()

app = Flask(__name__)


def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            DB.insert_task_table(nm,addr,city,pin)
            msg = "新增成功"
        except Exception as e:
            print(e)
            msg = "新增失敗"

        finally:
            return render_template("result.html", msg = msg)


@app.route('/list')
def list():
    rows = DB.get_all_tasks()

    return render_template("list.html", rows=rows)



# @app.route("/tasks/")
# def get_tasks():
#     return success_response(DB.get_all_tasks())


# @app.route("/tasks/", methods=["POST"])
# def create_task():
#     body = json.loads(request.data)
#     description = body["description"]
#     task_id = DB.insert_task_table(description, False)
#     print(task_id)
#     task = DB.get_task_by_id(task_id)
#     print(task)
#     if task is None:
#         return failure_response("Something went wrong while creating task!")
#     return success_response(task, 201)

# @app.route("/tasks/<int:task_id>/")
# def get_task(task_id):
#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     return success_response(task)

# @app.route("/tasks/<int:task_id>/", methods=["POST"])
# def update_task(task_id):
#     body = json.loads(request.data)
#     description = body["description"]
#     done = bool(body["done"])
#     DB.update_task_by_id(task_id, description, done)

#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     return success_response(task)

# @app.route("/mem_manage/", methods=["DELETE"])
# def delete_task():
#     task = DB.get_task_by_id(task_id)
#     if task is None:
#         return failure_response("Task not found!")
#     DB.delete_task_by_id(task_id)
#     return success_response(task)