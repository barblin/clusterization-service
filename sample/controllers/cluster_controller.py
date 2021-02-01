import time

from flask import Blueprint

from sample.api.request import extract_query_params
from sample.config.config import MIN_TREE_WASSER_CLUSTER
from sample.services.cluster.cluster_variance import cluster_for_wasser_dist

cluster_controller = Blueprint('cluster_controller', __name__)


@cluster_controller.route('/api/v1/views/' + MIN_TREE_WASSER_CLUSTER + '/files/<filename>')
def clusters_min_tree_wasser_for_file(filename):
    filters = extract_query_params()
    dings = cluster_for_wasser_dist(filename, filters).jsonify()
    return dings
