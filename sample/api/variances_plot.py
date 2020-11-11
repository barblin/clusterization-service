import json


class VariancesPlot:
    def __init__(self, data):
        self.data = data

    def jsonify(self):
        return json.dumps(self.data)
