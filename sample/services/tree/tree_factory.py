from sample.models.edge import Edge
from sample.models.vertex import Vertex
from sample.services.tree.tree import DistanceTree
from sample.services.data.datasource import load_file, data_without_labels
from sample.services.delaunay.delaunay_triangulation import triangulate_delaunay
from sample.services.math import two_d_distance


def create_tree(filename):
    return __fetch_tree(filename)


def __fetch_tree(filename):
    return __create_tree(filename)


def __create_tree(filename):
    df = load_file(filename)
    point_array = df.to_numpy()
    tri = triangulate_delaunay(filename, data_without_labels(df))
    tree = DistanceTree(point_array)

    for entries in tri.simplices:
        row = []
        for entry in entries:
            row.append(point_array[entry].tolist())

        dist1 = two_d_distance(row[0][0], row[0][1], row[1][0], row[1][1])
        dist2 = two_d_distance(row[0][0], row[0][1], row[2][0], row[2][1])
        dist3 = two_d_distance(row[1][0], row[1][1], row[2][0], row[2][1])

        edge1 = Edge(entries[0], entries[1], dist1, Vertex(row[0]), Vertex(row[1]))
        edge2 = Edge(entries[0], entries[2], dist2, Vertex(row[0]), Vertex(row[2]))
        edge3 = Edge(entries[1], entries[2], dist3, Vertex(row[1]), Vertex(row[2]))

        tree.add_edge(edge1)
        tree.add_edge(edge2)
        tree.add_edge(edge3)

    return tree