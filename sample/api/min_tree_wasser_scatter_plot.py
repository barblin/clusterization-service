import json


class MinTreeWasserScatterPlot:
    def __init__(self, wasser_scatter_plot):
        self.data = []
        color_dict = {}
        color_idx = 0
        labels = wasser_scatter_plot.ids.copy()

        for i in range(0, len(labels)):
            if str(labels[i]) in color_dict.keys():
                labels[i] = color_dict[str(labels[i])]
            else:
                color_dict[str(labels[i])] = color_idx
                labels[i] = color_idx
                color_idx += 1

        self.max_X = 0
        self.max_Y = 0
        self.components = wasser_scatter_plot.components

        for edge in wasser_scatter_plot.minimum_edges:
            src_x = edge.point1.coords[0]
            src_y = edge.point1.coords[1]
            label_src = labels[edge.src]

            if self.max_X < src_x:
                self.max_X = src_x

            if self.max_Y < src_y:
                self.max_Y = src_y

            self.data.append((src_x, src_y, int(label_src)))

            des_x = edge.point2.coords[0]
            des_y = edge.point2.coords[1]
            label_des = labels[edge.dest]

            if self.max_X < des_x:
                self.max_X = des_x

            if self.max_Y < des_y:
                self.max_Y = des_y

            self.data.append((des_x, des_y, int(label_des)))

    def jsonify(self):
        return json.dumps(self.__dict__)