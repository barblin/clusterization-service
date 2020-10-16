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
        data_frame["labels"] = scatter_plot.labels
        self.max_X = 0
        self.max_Y = 0

        for index, row in data_frame.iterrows():
            x = row['feat-1']
            y = row['feat-2']
            label = row['labels']

            if self.max_X < x:
                self.max_X = x

            if self.max_Y < y:
                self.max_Y = y

            self.data.append((x, y, int(label)))

    def jsonify(self):
        return json.dumps(self.__dict__)
