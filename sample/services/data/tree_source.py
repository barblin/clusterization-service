import os

from sample.config.config import edges_location
from sample.models.edge import Edge
from sample.models.vertex import Vertex


def store(tree, filename):
    store_edges(tree.edges, filename)


edge_sep = ";"
vex_sep = ","
edge_pre = "edges_"


def store_edges(edges, filename):
    if not os.path.exists(edges_location()):
        os.mkdir(edges_location())

    content = ""
    for edge in edges:
        content += (str(edge.src) + edge_sep +
                    str(edge.dest) + edge_sep +
                    str(edge.cost) + edge_sep +
                    vex_sep.join(map(str, edge.vertex1.coords)) + edge_sep +
                    vex_sep.join(map(str, edge.vertex2.coords)) + edge_sep +
                    str(edge.wasser_cost) + "\n")

    __write_overwrite(edge_pre + filename, content)


def load_edges(filename):
    content = __read(edge_pre + filename)
    lines = content.splitlines()

    edges = []
    for line in lines:
        if not line.strip():
            break

        edge_content = line.split(edge_sep)
        vertex1 = Vertex(__string_to_coords(edge_content[3]))
        vertex2 = Vertex(__string_to_coords(edge_content[4]))
        edges.append(Edge(int(edge_content[0]),
                          int(edge_content[1]),
                          float(edge_content[2]),
                          vertex1,
                          vertex2,
                          float(edge_content[5])))

    return edges


def __string_to_coords(coords_string):
    return [float(x) for x in coords_string.split(vex_sep)]


def __write_overwrite(filename, content):
    file = open(edges_location() + filename, "w")
    file.write(content)
    file.close()


def __read(filename):
    try:
        file = open(edges_location() + filename, "r")
        return file.read()
    except FileNotFoundError:
        return ""
