from flask import Flask,render_template
app = Flask(__name__)
app = Flask(__name__, static_url_path='/image', static_folder='image')

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/bgwb')
def bgwp():
    return render_template('bgwb.html')