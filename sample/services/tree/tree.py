import sys
from scipy.stats import wasserstein_distance
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import RobustScaler


class DistanceTree:
    def __init__(self, vertex_data):
        self.point_array = vertex_data
        self.edges = []
        self.neighbours = {}
        self.number_vertices = len(vertex_data)
        self.min_wasser = sys.maxsize
        self.max_wasser = 0

    def add_edge(self, edge):
        if edge.wasser_cost < self.min_wasser:
            self.min_wasser = edge.wasser_cost

        if self.max_wasser < edge.wasser_cost:
            self.max_wasser = edge.wasser_cost

        self.edges.append(edge)

    def calc_neighbours(self):
        points = self.point_array[:, 0:2]
        scaled_data = RobustScaler().fit_transform(points)

        knn = NearestNeighbors(n_neighbors=250, algorithm='ball_tree').fit(scaled_data)
        distances, indices = knn.kneighbors(scaled_data)

        for i in range(0, len(distances)):
            self.neighbours[i] = distances[i].tolist()

    def sort(self):
        self.edges.sort(key=lambda x: x.cost)

    def sort_wasser(self):
        self.edges.sort(key=lambda x: x.wasser_cost)

    def clean_wasser_calc(self):
        for edge in self.edges:
            self.__calc_wasser_dist(edge)

    def __calc_wasser_dist(self, edge):
        if not self.neighbours[edge.src] or not self.neighbours[edge.dest]:
            edge.wasser_cost = -1
        else:
            edge.wasser_cost = wasserstein_distance(self.neighbours[edge.src], self.neighbours[edge.dest])

            if edge.wasser_cost < self.min_wasser:
                self.min_wasser = edge.wasser_cost

            if self.max_wasser < edge.wasser_cost:
                self.max_wasser = edge.wasser_cost
