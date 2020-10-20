from scipy.stats import wasserstein_distance

from sample.models.union_find import UnionFind
from enum import Enum


class Distance(Enum):
    WASSER = "wasser"
    DIRECT = "direct"


class Edge:
    def __init__(self, src, dest, cost, point1, point2):
        self.src = src
        self.dest = dest
        self.cost = cost
        self.point1 = point1
        self.point2 = point2
        self.wasser_cost = 0


class DistanceTree:
    def __init__(self, vertices):
        self.edges = []
        self.neighbours = {}
        self.number_vertices = vertices

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

    def wasser_sort(self):
        self.edges.sort(key=lambda x: x.wasser_cost)

    def calc_wasser_dist(self):
        for edge in self.edges:
            edge.wasser_cost = wasserstein_distance(self.neighbours[edge.src], self.neighbours[edge.dest])

    def minimum_tree(self, distance):
        if distance is Distance.WASSER:
            self.calc_wasser_dist()
            self.wasser_sort()
            print("Hallo Wasser")
        else:
            self.sort()
            print("Hallo Dist")

        union_find = UnionFind(self.number_vertices)

        minimum_edges = []

        for edge in self.edges:
            if not union_find.connected(edge.src, edge.dest):
                minimum_edges.append(edge)
                union_find.unify(edge.src, edge.dest)

        return minimum_edges
