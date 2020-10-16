import json

from flask import Flask

from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.models.config import SUPPORTED_VIEWS
from sample.plotting import plot
from sample.services import cluster
from sample.services import datasource

app = Flask(__name__)


@app.route('/api/v1/version')
def version():
    return '0.0.1'


@app.route('/api/v1/files')
def get_files():
    return json.dumps(datasource.files())


@app.route('/api/v1/views')
def get_views():
    return json.dumps(SUPPORTED_VIEWS)


@app.route('/api/v1/views/clusters/files/<filename>')
def cluster_data_for_file(filename):
    return ScatterPlotResponse(cluster.compute_clusters(filename)).jsonify()


@app.route('/api/v1/views/simple-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    return ScatterPlotResponse(datasource.load_scatter_plot(filename)).jsonify()


@app.route('/api/v1/views/delaunay-triangulation/files/<filename>')
def delaunay_triangulation_data_for_file(filename):
    return ScatterPlotResponse(datasource.load_scatter_plot(filename)).jsonify()


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
