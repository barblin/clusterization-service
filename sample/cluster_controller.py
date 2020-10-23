import json

from flask import Flask
from flask import request

from sample.api.delaunay_plot_response import DelaunayPlotResponse
from sample.api.min_tree_wasser_scatter_plot import MinTreeWasserScatterPlot
from sample.api.minimum_tree_response import MinimumTreeResponse
from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.models.cluster_filters import ClusterFilters
from sample.models.cluster_tree import Distance
from sample.models.config import SUPPORTED_VIEWS
from sample.plotting import plot
from sample.services import cluster
from sample.services import datasource
from sample.services.delaunay_triangulation import triangulation_plot
from sample.services.minimum_spanning_tree import create_min_tree, cluster_min_tree

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
    return DelaunayPlotResponse(triangulation_plot(filename)).jsonify()


@app.route('/api/v1/views/minimum-spanning-tree/files/<filename>')
def minimum_spanning_tree_for_file(filename):
    filters = extract_query_params()
    return MinimumTreeResponse(create_min_tree(filename, Distance.DIRECT, filters)).jsonify()


@app.route('/api/v1/views/minimum-spanning-tree-wasser/files/<filename>')
def minimum_spanning_tree_wasser_for_file(filename):
    filters = extract_query_params()
    return MinimumTreeResponse(create_min_tree(filename, Distance.WASSER, filters)).jsonify()


@app.route('/api/v1/views/clusters-min-tree-wasser/files/<filename>')
def clusters_min_tree_wasser_for_file(filename):
    filters = extract_query_params()
    return MinTreeWasserScatterPlot(cluster_min_tree(filename, filters)).jsonify()


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


def extract_query_params():
    return ClusterFilters(request.args.get('numClusters'),
                          request.args.get('wasserError'),
                          request.args.get('distError'))


app.run(debug=True)
