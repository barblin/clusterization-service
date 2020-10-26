from flask import Blueprint

from sample.api.min_tree_wasser_scatter_plot import MinTreeWasserScatterPlot
from sample.api.request import extract_query_params
from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.services import cluster
from sample.services.minimum_spanning_tree import cluster_min_tree

cluster_controller = Blueprint('cluster_controller', __name__)


@cluster_controller.route('/api/v1/views/clusters/files/<filename>')
def cluster_data_for_file(filename):
    return ScatterPlotResponse(cluster.compute_clusters(filename)).jsonify()


@cluster_controller.route('/api/v1/views/clusters-min-tree-wasser/files/<filename>')
def clusters_min_tree_wasser_for_file(filename):
    filters = extract_query_params()
    return MinTreeWasserScatterPlot(cluster_min_tree(filename, filters)).jsonify()
