import json

from sample.services.color_mapping import create_color_map_by_size_decreasing


class MinTreeWasserScatterPlot:
    def __init__(self, wasser_scatter_plot):
        self.data = []
        self.processed_points = {}

        labels = wasser_scatter_plot.union_find.id_sz
        color_dict = create_color_map_by_size_decreasing(labels.copy(), wasser_scatter_plot.num_clusters)

        self.max_X = 0
        self.max_Y = 0

        for edge in wasser_scatter_plot.edges:
            self.__create_point(edge.point1, edge.src, labels, color_dict)
            self.__create_point(edge.point2, edge.dest, labels, color_dict)

        self.processed_points = None

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __create_point(self, point, key, labels, color_dict):
        if key in self.processed_points.keys():
            return

        point_x = point.coords[0]
        point_y = point.coords[1]

        label = -1
        if labels[key].id in color_dict.keys():
            label = color_dict[labels[key].id]

        if self.max_X < point_x:
            self.max_X = point_x

        if self.max_Y < point_y:
            self.max_Y = point_y

        self.data.append((point_x, point_y, int(label)))
        self.processed_points[key] = None
