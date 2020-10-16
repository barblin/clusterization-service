

class Edge:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost
        self.wasser_cost = cost


class WassersteinDistanceTree:
    def __init__(self, vertices):
        self.edges = []
        self.number_vertices = vertices

    def add_edge(self, edge):
        self.edges.append(edge)

    def sort(self):
        self.edges.sort(key=lambda x: x.cost)
