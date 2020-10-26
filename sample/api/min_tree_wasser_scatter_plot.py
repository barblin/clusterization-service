import json

import numpy as np


class MinTreeWasserScatterPlot:
    def __init__(self, wasser_scatter_plot):
        self.data = []
        self.processed_points = {}

        labels = wasser_scatter_plot.union_find.id_sz;
        color_dict = self.__create_color_map(labels, wasser_scatter_plot)

        self.max_X = 0
        self.max_Y = 0

        for edge in wasser_scatter_plot.edges:
            self.__create_point(edge.point1, edge.src, labels, color_dict)
            self.__create_point(edge.point2, edge.dest, labels, color_dict)

        self.processed_points = None

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __create_color_map(self, labels, wasser_scatter_plot):
        values = []
        for key in labels:
            values.append(wasser_scatter_plot.union_find.id_sz[key])

        self.components = wasser_scatter_plot.num_clusters

        id_sz = np.array(values)
        id_sz = id_sz[id_sz[:, 1].argsort()][::-1][:self.components]

        color_dict = {}
        color_idx = 0
        for i in range(0, self.components):
            color_dict[id_sz[i][0]] = color_idx
            color_idx += 1

        return color_dict

    def __create_point(self, point, key, labels, color_dict):
        if key in self.processed_points.keys():
            return

        point_x = point.coords[0]
        point_y = point.coords[1]

        if labels[key][0] in color_dict.keys():
            label = color_dict[labels[key][0]]
        else:
            label = -1

        if self.max_X < point_x:
            self.max_X = point_x

        if self.max_Y < point_y:
            self.max_Y = point_y

        self.data.append((point_x, point_y, int(label)))
        self.processed_points[key] = None
