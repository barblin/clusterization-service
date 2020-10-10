from flask import Flask
from sample.services import dataset
from sample.services import plot
from sample.services import cluster

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '1.0.0'


@app.route('/api/v1/clusters/data')
def cluster_data():
    return dataset.load().to_json()


@app.route('/api/v1/clusters/data/files/<filename>')
def cluster_data_for_file(filename):
    return dataset.load_file(filename).to_json()


@app.route('/api/v1/plots/files/<filename>')
def plot_file(filename):
    plot.plot(dataset.load_file(filename))
    return 'file plotting finished'


@app.route('/api/v1/plots/clusters/<filename>')
def plot_cluster(filename):
    cluster.plot_clusters(filename)
    return 'cluster plotting finished'


app.run(debug=True)
