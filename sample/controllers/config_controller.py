import json

from flask import Blueprint

from sample.config.config import SUPPORTED_VIEWS
from sample.services.data import datasource

config_controller = Blueprint('config_controller', __name__)


@config_controller.route('/api/v1/version')
def version():
    return '0.0.1'


@config_controller.route('/api/v1/files')
def get_files():
    return json.dumps(sorted(datasource.list_files()))


@config_controller.route('/api/v1/views')
def get_views():
    return json.dumps(SUPPORTED_VIEWS)
