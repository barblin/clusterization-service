from sample.models.cluster_tree import Distance
from sample.models.tree_factory import create_tree
from sample.models.union_find import UnionFind
from sample.services.tree.tree_preparation_service import apply_filters_and_wasser_distance
from sample.services.tree.tree_wasser_distance_unification import unify_by_wasser_distance


def create_min_tree(filename, distance, filters):
    if distance is Distance.WASSER:
        return cluster_min_tree(filename, filters).minimum_edges
    else:
        tree = get_and_prep_tree(filename, filters)
        return __minimum_eucledian_tree(tree, UnionFind(tree.point_array), filters)


def cluster_min_tree(filename, filters):
    return unify_by_wasser_distance(get_and_prep_tree(filename, filters), filters.wasser_error, filters.num_clusters)


def get_and_prep_tree(filename, filters):
    tree = create_tree(filename)
    return apply_filters_and_wasser_distance(tree, filters)


def __minimum_eucledian_tree(tree, union_find, filters):
    tree.sort()

    minimum_edges = []

    for edge in tree.edges:
        if union_find.num_components <= filters.num_clusters:
            break

        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest, 0)

    return minimum_edges
