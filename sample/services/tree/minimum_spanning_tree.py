from sample.models.enums.distance import Distance
from sample.services.cluster.union_find import UnionFind
from sample.services.data.datasource import load_file
from sample.services.data.tree_source import load_edges
from sample.services.tree.tree import DistanceTree
from sample.services.tree.tree_factory import create_tree
from sample.services.tree.tree_wasser_distance_unification import unify_by_wasser_distance


def create_min_tree(filename, distance, filters):
    if distance is Distance.WASSER:
        return cluster_min_tree(filename, filters)
    else:
        tree = get_and_prep_tree(filename, filters)
        return __minimum_eucledian_tree(tree, UnionFind(tree.point_array))


def cluster_min_tree(filename, filters):
    return unify_by_wasser_distance(get_and_prep_tree(filename, filters))


def compute_wasser_tree(filename, filters):
    edges = load_edges(filename)

    if 0 < len(edges):
        df = load_file(filename)
        point_array = df.to_numpy()
        tree = DistanceTree(point_array)

        for edge in edges:
            tree.add_edge(edge)

        return tree

    tree = get_and_prep_tree(filename, filters)
    if filters.remove_outliers:
        tree.remove_outliers(filters.stdv_multiplier)

    tree.clean_wasser_calc()
    tree.sort_wasser()
    return tree


def get_and_prep_tree(filename, filters):
    tree = create_tree(filename)

    if filters.normalize_neigh_dist is True:
        tree.normalize_neighbours()

    return tree


def __minimum_eucledian_tree(tree, union_find):
    tree.sort()

    minimum_edges = []

    for edge in tree.edges:
        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest, 0)

    return minimum_edges
