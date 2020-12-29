from flask import Blueprint

from sample.api.multi_view import MultiView
from sample.api.request import extract_query_params
from sample.services.cluster.cluster_variance import cluster_for_wasser_dist

multi_controller = Blueprint('multi_controller', __name__)


@multi_controller.route('/api/v1/views/multi-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    filters = extract_query_params()
    variance_data = cluster_for_wasser_dist(filename, filters).jsonify()
    return MultiView(variance_data).jsonify()
