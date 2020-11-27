from flask import Blueprint

from sample.api.delaunay_plot_response import DelaunayPlotResponse
from sample.api.minimum_tree_response import MinimumTreeResponse
from sample.api.request import extract_query_params
from sample.api.scatter_plot_response import ScatterPlotResponse
from sample.models.tree import Distance
from sample.services import datasource
from sample.services.delaunay.delaunay_triangulation import triangulation_plot
from sample.services.tree.minimum_spanning_tree import create_min_tree

view_controller = Blueprint('view_controller', __name__)


@view_controller.route('/api/v1/views/simple-plots/files/<filename>')
def simple_plot_data_for_file(filename):
    return ScatterPlotResponse(datasource.load_scatter_plot(filename)).jsonify()


@view_controller.route('/api/v1/views/delaunay-triangulation/files/<filename>')
def delaunay_triangulation_data_for_file(filename):
    return DelaunayPlotResponse(triangulation_plot(filename)).jsonify()


@view_controller.route('/api/v1/views/minimum-spanning-tree/files/<filename>')
def minimum_spanning_tree_for_file(filename):
    filters = extract_query_params()
    return MinimumTreeResponse(create_min_tree(filename, Distance.DIRECT, filters)).jsonify()


@view_controller.route('/api/v1/views/minimum-spanning-tree-wasser/files/<filename>')
def minimum_spanning_tree_wasser_for_file(filename):
    filters = extract_query_params()
    return MinimumTreeResponse(create_min_tree(filename, Distance.WASSER, filters)).jsonify()
