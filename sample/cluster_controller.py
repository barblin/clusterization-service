from flask import Flask
from sample.services import dataset_service
from sample.services import plot_service

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '1.0.0'


@app.route('/api/v1/cluster/data')
def cluster_data():
    return dataset_service.load().to_json()


@app.route('/api/v1/cluster/data/file/<filename>')
def cluster_data_for_file(filename):
    return dataset_service.load_file(filename).to_json()


@app.route('/api/v1/plot/<filename>')
def hello_world(filename):
    plot_service.plot(dataset_service.load_file(filename))
    return 'plotting finished'


app.run(debug=True)
