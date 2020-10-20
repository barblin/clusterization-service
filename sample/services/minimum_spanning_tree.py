from sample.models.cluster_tree import Distance
from sample.models.plots import MinTreeWasserClusterPlot
from sample.models.tree_factory import create_tree
from sample.models.union_find import UnionFind
from sample.services import datasource


def create_min_tree(filename, distance):
    tree = create_tree(filename)
    return __minimum_tree(distance, tree)


def cluster_min_tree(filename):
    data_frame = datasource.load_file(filename)
    tree = create_tree(filename)
    return MinTreeWasserClusterPlot(data_frame, __wasser_vertex_union(tree))


def __wasser_vertex_union(tree):
    union_find = UnionFind(tree.number_vertices)
    tree.calc_wasser_dist()
    tree.sort()

    for edge in tree.edges:
        if union_find.num_components <= 6:
            break

        if not union_find.connected(edge.src, edge.dest):
            union_find.unify(edge.src, edge.dest)

    return union_find


def __minimum_tree(distance, tree):
    if distance is Distance.WASSER:
        return __minimum_wasser_tree(tree, UnionFind(tree.number_vertices))
    else:
        return __minimum_eucledian_tree(tree, UnionFind(tree.number_vertices))


def __minimum_eucledian_tree(tree, union_find):
    tree.sort()

    minimum_edges = []

    for edge in tree.edges:
        if union_find.num_components <= 6:
            break

        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest)

    return minimum_edges


def __minimum_wasser_tree(tree, union_find):
    tree.calc_wasser_dist()
    tree.wasser_sort()

    minimum_edges = []

    for edge in tree.edges:
        if tree.average_wasser_dist < edge.wasser_cost:
            break

        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest)

    return minimum_edges
