from sample.models.union_find import UnionFind
import json


class Edge:
    def __init__(self, src, dest, cost, point1, point2):
        self.src = src
        self.dest = dest
        self.cost = cost
        self.wasser_cost = cost
        self.point1 = point1
        self.point2 = point2


class WassersteinDistanceTree:
    def __init__(self, vertices):
        self.edges = []
        self.number_vertices = vertices

    def add_edge(self, edge):
        self.edges.append(edge)

    def sort(self):
        self.edges.sort(key=lambda x: x.cost)

    def minimum_tree(self):
        self.sort()

        union_find = UnionFind(self.number_vertices)

        minimum_edges = []

        for edge in self.edges:
            if not union_find.connected(edge.src, edge.dest):
                minimum_edges.append(edge)
                union_find.unify(edge.src, edge.dest)

        return minimum_edges
