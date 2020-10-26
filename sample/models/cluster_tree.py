from enum import Enum

import numpy as np
from scipy.stats import wasserstein_distance


class Distance(Enum):
    WASSER = "wasser"
    DIRECT = "direct"


class Vertex:
    def __init__(self, coords):
        self.coords = coords
        self.label = -1


class Edge:
    def __init__(self, src, dest, cost, point1, point2):
        self.src = src
        self.dest = dest
        self.cost = cost
        self.point1 = point1
        self.point2 = point2
        self.wasser_cost = 0
        self.average_neighbour_cost = 0


class DistanceTree:
    def __init__(self, vertices):
        self.edges = []
        self.neighbours = {}
        self.number_vertices = vertices
        self.min_wasser = 200000
        self.max_wasser = 0

    def add_edge(self, edge):
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

    def flatten_neighbours(self, stdv_multiplier):
        for key in self.neighbours.keys():
            value = self.neighbours[key]
            arr = np.array(value)
            mean = np.mean(arr, axis=0)
            sd = np.std(arr, axis=0)

            value = [x for x in value if (x < mean + stdv_multiplier * sd)]

            self.neighbours[key] = value

    def calc_wasser_dist(self):
        for edge in self.edges:
            if not self.neighbours[edge.src] or not self.neighbours[edge.dest]:
                edge.wasser_cost = -1
            else:
                edge.wasser_cost = wasserstein_distance(self.neighbours[edge.src], self.neighbours[edge.dest])

                if edge.wasser_cost < self.min_wasser:
                    self.min_wasser = edge.wasser_cost

                if self.max_wasser < edge.wasser_cost:
                    self.max_wasser = edge.wasser_cost
