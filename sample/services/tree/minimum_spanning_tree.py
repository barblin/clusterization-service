from sample.models.tree import Distance
from sample.models.union_find import UnionFind
from sample.services.tree.tree_wasser_distance_unification import unify_by_wasser_distance
from sample.services.tree_factory import create_tree


def create_min_tree(filename, distance, filters):
    if distance is Distance.WASSER:
        return cluster_min_tree(filename, filters)
    else:
        tree = get_and_prep_tree(filename, filters)
        return __minimum_eucledian_tree(tree, UnionFind(tree.point_array))


def cluster_min_tree(filename, filters):
    return unify_by_wasser_distance(get_and_prep_tree(filename, filters))


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
