import json
import numpy as np


class MinTreeWasserScatterPlot:
    def __init__(self, wasser_scatter_plot):
        self.data = []

        labels = wasser_scatter_plot.union_find.id_sz;
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

        self.max_X = 0
        self.max_Y = 0

        for edge in wasser_scatter_plot.edges:
            src_x = edge.point1.coords[0]
            src_y = edge.point1.coords[1]

            if labels[edge.src][0] in color_dict.keys():
                label_src = color_dict[labels[edge.src][0]]
            else:
                label_src = -1

            if self.max_X < src_x:
                self.max_X = src_x

            if self.max_Y < src_y:
                self.max_Y = src_y

            self.data.append((src_x, src_y, int(label_src)))

            des_x = edge.point2.coords[0]
            des_y = edge.point2.coords[1]

            if labels[edge.dest][0] in color_dict.keys():
                label_des = color_dict[labels[edge.dest][0]]
            else:
                label_des = -1

            if self.max_X < des_x:
                self.max_X = des_x

            if self.max_Y < des_y:
                self.max_Y = des_y

            self.data.append((des_x, des_y, int(label_des)))

    def jsonify(self):
        return json.dumps(self.__dict__)