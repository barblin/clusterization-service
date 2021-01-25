from flask import Flask
from flask_script import Command, Manager, Option

from sample.services.asyncron import pre_calc_tree


class Precompute(Command):
    option_list = (
        Option('--offset', '-o', dest='offset'),
    )

    def run(self, offset):
        if offset is None:
            offset = 0
        else:
            offset = int(offset)

        pre_calc_tree.issue(offset)


app = Flask(__name__)
manager = Manager(app)
manager.add_command('edges', Precompute())

manager.run()
