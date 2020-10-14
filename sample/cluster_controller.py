from flask import Flask

from sample.models.SatterPlotResponse import ScatterPlotResponse
from sample.services import cluster
from sample.services import dataset
from sample.services import plot

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '0.0.1'


@app.route('/api/v1/clusters/data')
def cluster_data():
    return dataset.load().to_json()


@app.route('/api/v1/clusters/data/files/<filename>')
def cluster_data_for_file(filename):
    return ScatterPlotResponse(cluster.compute_clusters(filename)).jsonify()


@app.route('/api/v1/plots/files/<filename>')
def plot_file(filename):
    plot.plot(dataset.load_file(filename))
    return 'file plotting finished'


@app.route('/api/v1/plots/clusters/<filename>')
def plot_cluster(filename):
    cluster.plot_clusters(filename)
    return 'cluster plotting finished'


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


app.run(debug=True)
