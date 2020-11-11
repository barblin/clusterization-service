from flask import Blueprint

from sample.api.request import extract_query_params
from sample.api.variances_plot import VariancesPlot
from sample.services.cluster import cluster_variance

variances_controller = Blueprint('variances_controller', __name__)


@variances_controller.route('/api/v1/views/variances-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    filters = extract_query_params()
    return VariancesPlot(cluster_variance.cluster_for_incr_wasser_dist(filename, filters)).jsonify()
