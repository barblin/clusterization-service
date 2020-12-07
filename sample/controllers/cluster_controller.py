import time

from flask import Blueprint

from sample.api.request import extract_query_params
from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.services import cluster
from sample.services.cluster.cluster_variance import cluster_for_wasser_dist

cluster_controller = Blueprint('cluster_controller', __name__)


@cluster_controller.route('/api/v1/views/clusters/files/<filename>')
def cluster_data_for_file(filename):
    return ScatterPlotResponse(cluster.compute_clusters(filename)).jsonify()


@cluster_controller.route('/api/v1/views/clusters-min-tree-wasser/files/<filename>')
def clusters_min_tree_wasser_for_file(filename):
    start_time = time.time()
    filters = extract_query_params()
    dings = cluster_for_wasser_dist(filename, filters).jsonify()
    print("--- %s seconds ---" % (time.time() - start_time))
    return dings
