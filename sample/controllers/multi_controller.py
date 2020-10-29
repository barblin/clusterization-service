from flask import Blueprint

from sample.api.multi_view import MultiView
from sample.api.request import extract_query_params
from sample.services.minimum_spanning_tree import cluster_min_tree

multi_controller = Blueprint('multi_controller', __name__)


@multi_controller.route('/api/v1/views/multi-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    filters = extract_query_params()
    return MultiView(cluster_min_tree(filename, filters)).jsonify()
