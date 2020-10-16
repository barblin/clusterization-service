import json


class DelaunayPlotResponse:
    def __init__(self, tri_plot):
        self.data = tri_plot.plot

        self.max_X = 0
        self.max_Y = 0

        for index, row in tri_plot.dataframe.iterrows():
            x = row['feat-1']
            y = row['feat-2']

            if self.max_X < x:
                self.max_X = x

            if self.max_Y < y:
                self.max_Y = y

    def jsonify(self):
        return json.dumps(self.__dict__)
