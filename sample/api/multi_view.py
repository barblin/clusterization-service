import json

from sample.services.data.color_mapping import create_color_map_by_size_decreasing


class MultiView:
    def __init__(self, wasser_scatter_plot):
        self.tree_max_x = 0
        self.tree_max_y = 0
        self.tree_data = []
        self.scatter_max_x = 0
        self.scatter_max_y = 0
        self.scatter_data = []
        self.clustered_points = 0
        self.clustered_points_match = 0
        self.cluster_compare = []

        self.processed_points = {}

        labels = wasser_scatter_plot.union_find.id_sz
        color_dict = create_color_map_by_size_decreasing(labels.copy())

        for edge in wasser_scatter_plot.edges:
            self.__create_point(edge.vertex1, edge.src, labels, color_dict)
            self.__create_point(edge.vertex2, edge.dest, labels, color_dict)

        self.processed_points = None

    def jsonify(self):
        return json.dumps(self.__dict__)

    def __create_point(self, point, key, labels, color_dict):
        if key in self.processed_points.keys():
            return

        point_x = point.coords[0]
        point_y = point.coords[1]

        label = -1
        cluster_compare_label = 5
        if labels[key].id in color_dict.keys():
            label = color_dict[labels[key].id]

        if self.tree_max_x < point_x:
            self.tree_max_x = point_x
            self.scatter_max_x = point_x

        if self.tree_max_y < point_y:
            self.tree_max_y = point_y
            self.scatter_max_y = point_y

        if label != -1:
            self.clustered_points += 1

            if int(labels[key].old_label) == int(label):
                self.clustered_points_match += 1
                cluster_compare_label = 3

        self.tree_data.append((point_x, point_y, int(label)))
        self.scatter_data.append((point_x, point_y, labels[key].old_label))
        self.cluster_compare.append((point_x, point_y, cluster_compare_label))
        self.processed_points[key] = None
