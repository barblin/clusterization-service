from cluswasser.tree import DistanceTree, create_tree
from cluswasser.union_find import UnionFind

from sample.config.config import FILE_NEIGHS
from sample.models.enums.distance import Distance
from sample.services.cluster.cluster_variance import fetch_edges
from sample.services.data.datasource import load_file, to_features, to_labels
from sample.services.data.tree_source import load_edges
from sample.services.tree.tree_wasser_distance_unification import unify_wasser


def create_min_tree(filename, distance):
    data = load_file(filename)
    labels = to_labels(data)

    if distance is Distance.WASSER:
        return unify_wasser(get_and_prep_tree(filename), labels)
    else:
        tree = get_and_prep_tree(filename)
        return __minimum_eucledian_tree(tree, UnionFind(tree.features, labels))


def compute_wasser_tree(filename):
    edges = load_edges(filename)

    if 0 < len(edges):
        df = load_file(filename)
        point_array = df.to_numpy()
        tree = DistanceTree(point_array)

        for edge in edges:
            tree.add_edge(edge)

        return tree

    tree = get_and_prep_tree(filename)
    return tree


def get_and_prep_tree(filename):
    edges = fetch_edges(filename)

    data = load_file(filename)
    features = to_features(data)

    if 0 < len(edges):
        return DistanceTree(features, edges)

    return create_tree(features, FILE_NEIGHS[filename])


def __minimum_eucledian_tree(tree, union_find):
    tree.sort()

    minimum_edges = []

    for edge in tree.edges:
        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest, 0)

    return minimum_edges
