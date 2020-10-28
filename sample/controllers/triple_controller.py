from flask import Blueprint

from sample.api.min_tree_wasser_scatter_plot import MinTreeWasserScatterPlot
from sample.api.request import extract_query_params
from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.api.triple_view import TripleView
from sample.services import datasource
from sample.services.minimum_spanning_tree import cluster_min_tree

triple_controller = Blueprint('triple_controller', __name__)


@triple_controller.route('/api/v1/views/triple-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    filters = extract_query_params()
    tree = MinTreeWasserScatterPlot(cluster_min_tree(filename, filters))
    scatter = ScatterPlotResponse(datasource.load_scatter_plot(filename))

    return TripleView(tree.max_X, tree.max_Y, tree.data,
                      scatter.max_X, scatter.max_Y, scatter.data).jsonify()
