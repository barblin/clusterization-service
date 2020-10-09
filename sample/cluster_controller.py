from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '1.0.0'


@app.route('/api/v1/hello')
def hello_world():
    return 'hello'


@app.route('/api/v1/cluster/data')
def cluster_data():
    return 'hello'
