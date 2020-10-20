import json


class MinTreeWasserScatterPlot:
    def __init__(self, wasser_scatter_plot):
        self.data = []
        color_dict = {}
        color_idx = 0
        labels = wasser_scatter_plot.u_find.id.copy()

        for i in range(0, len(labels)):
            if labels[i] in color_dict.keys():
                labels[i] = color_dict[labels[i]]
            else:
                color_dict[labels[i]] = color_idx
                color_idx += 1

        self.max_X = 0
        self.max_Y = 0

        for index, row in wasser_scatter_plot.data_frame.iterrows():
            x = row['feat-1']
            y = row['feat-2']
            label = labels[index]

            if self.max_X < x:
                self.max_X = x

            if self.max_Y < y:
                self.max_Y = y

            self.data.append((x, y, int(label)))

    def jsonify(self):
        return json.dumps(self.__dict__)