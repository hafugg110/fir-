from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world.'

@app.route('/')
def index():
    # 顯示表單
    return 'Hello, world.'


@app.route('/', methods=['POST'])
def process():
    # 處理圖片
    return 'Process'