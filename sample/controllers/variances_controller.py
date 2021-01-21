import json

from flask import Blueprint

from sample.api.request import extract_query_params
from sample.api.variances_plot import VariancesPlot
from sample.config.config import VARIANCES_PLOTS
from sample.services.cluster import cluster_variance

variances_controller = Blueprint('variances_controller', __name__)
variances_plot_controller = Blueprint('variances_plot_controller', __name__)


@variances_controller.route('/api/v1/views/' + VARIANCES_PLOTS + '/files/<filename>')
def variances(filename):
    filters = extract_query_params()
    return VariancesPlot(cluster_variance.cluster_for_incr_wasser_dist(filename, filters)).jsonify()


@variances_plot_controller.route('/api/v1/views/' + VARIANCES_PLOTS + '/plots/<plotid>')
def variances_plot(plotid):
    return json.loads(cluster_variance.load_plot(plotid))
