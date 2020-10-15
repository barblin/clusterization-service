from flask import Flask

from sample.api.ScatterPlotResponse import ScatterPlotResponse
from sample.services import cluster
from sample.services import datasource
from sample.services import plot
import json

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '0.0.1'


@app.route('/api/v1/files')
def get_files():
    return json.dumps(datasource.files())


@app.route('/api/v1/clusters/data')
def cluster_data():
    return datasource.load().to_json()


@app.route('/api/v1/clusters/data/files/<filename>')
def cluster_data_for_file(filename):
    return ScatterPlotResponse(cluster.compute_clusters(filename)).jsonify()


@app.route('/api/v1/plots/files/<filename>')
def plot_file(filename):
    plot.plot(datasource.load_file(filename))
    return 'file plotting finished'


@app.route('/api/v1/plots/clusters/files/<filename>')
def plot_cluster(filename):
    cluster.plot_clusters(filename)
    return 'cluster plotting finished'


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


app.run(debug=True)
