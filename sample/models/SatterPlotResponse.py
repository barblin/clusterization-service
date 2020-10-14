import json


class Dot:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class ScatterPlotResponse:
    def __init__(self, scatter_plot):
        self.data = []
        data_frame = scatter_plot.data

        for index, row in data_frame.iterrows():
            x = row['feat-1']
            y = row['feat-2']
            label = row['labels']
            self.data.append((x, y, label))

    def jsonify(self):
        return json.dumps(self.__dict__)
