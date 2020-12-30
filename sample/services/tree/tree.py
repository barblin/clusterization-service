import sys

from scipy.stats import wasserstein_distance

from sample.services.math import calc_cutoff


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

        if edge.src in self.neighbours.keys():
            self.neighbours[edge.src].append(edge.cost)
        else:
            self.neighbours[edge.src] = [edge.cost]

        if edge.dest in self.neighbours.keys():
            self.neighbours[edge.dest].append(edge.cost)
        else:
            self.neighbours[edge.dest] = [edge.cost]

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

    def remove_outliers(self, stdv_multiplier):
        filtered_edges = []

        for edge in self.edges:
            src_neighs = self.neighbours[edge.src]
            dest_neighs = self.neighbours[edge.dest]

            cutoff_src = calc_cutoff(src_neighs, stdv_multiplier)
            cutoff_dest = calc_cutoff(dest_neighs, stdv_multiplier)

            if edge.cost <= cutoff_src and edge.cost <= cutoff_dest:
                filtered_edges.append(edge)
            else:
                self.neighbours[edge.src] = [x for x in src_neighs if (x <= cutoff_src)]
                self.neighbours[edge.dest] = [x for x in dest_neighs if (x <= cutoff_dest)]

        self.edges = filtered_edges
