from flask import Flask
from flask_script import Command, Manager

from sample.services.asyncron import pre_calc_tree


class Precompute(Command):
    def run(self):
        pre_calc_tree.issue()


app = Flask(__name__)
manager = Manager(app)
manager.add_command('edges', Precompute())

manager.run()
