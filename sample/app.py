from flask import Flask

from sample.controllers.cluster_controller import cluster_controller
from sample.controllers.config_controller import config_controller
from sample.controllers.multi_controller import multi_controller
from sample.controllers.plot_controller import plot_controller
from sample.controllers.variances_controller import variances_controller
from sample.controllers.view_controller import view_controller

app = Flask(__name__)

app.register_blueprint(config_controller)
app.register_blueprint(plot_controller)
app.register_blueprint(view_controller)
app.register_blueprint(cluster_controller)
app.register_blueprint(multi_controller)
app.register_blueprint(variances_controller)


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
