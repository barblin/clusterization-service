from flask import Flask, request

from sample.controllers.cluster_controller import cluster_controller
from sample.controllers.config_controller import config_controller
from sample.models.cluster_filters import ClusterFilters
from sample.controllers.plot_controller import plot_controller
from sample.controllers.view_controller import view_controller

app = Flask(__name__)

app.register_blueprint(config_controller)
app.register_blueprint(plot_controller)
app.register_blueprint(view_controller)
app.register_blueprint(cluster_controller)


@app.route("/")
def hello():
    return "Service running"


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    app.run()

app.run(debug=True)
