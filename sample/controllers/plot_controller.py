from flask import Blueprint

from sample.plotting import plot
from sample.services import cluster, datasource

plot_controller = Blueprint('plot_controller', __name__)


@plot_controller.route('/api/v1/plots/files/<filename>')
def plot_file(filename):
    plot.plot(datasource.load_file(filename))
    return 'file plotting finished'


@plot_controller.route('/api/v1/plots/clusters/files/<filename>')
def plot_cluster(filename):
    cluster.plot_clusters(filename)
    return 'cluster plotting finished'
