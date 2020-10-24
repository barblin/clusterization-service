from sample.models.cluster_tree import Distance
from sample.models.plots import MinTreeWasserClusterPlot
from sample.models.tree_factory import create_tree
from sample.models.union_find import UnionFind


def create_min_tree(filename, distance, filters):
    tree = create_tree(filename)
    return __minimum_tree(distance, tree, filters)


def cluster_min_tree(filename, filters):
    tree = create_tree(filename)
    return __wasser_vertex_union(tree, filters)


def __minimum_tree(distance, tree, filters):
    if distance is Distance.WASSER:
        return __wasser_vertex_union(tree, filters).minimum_edges
    else:
        return __minimum_eucledian_tree(tree, UnionFind(tree.number_vertices), filters)


def __minimum_eucledian_tree(tree, union_find, filters):
    tree.sort()

    minimum_edges = []

    for edge in tree.edges:
        if union_find.num_components <= filters.num_clusters:
            break

        if not union_find.connected(edge.src, edge.dest):
            minimum_edges.append(edge)
            union_find.unify(edge.src, edge.dest)

    return minimum_edges


def __wasser_vertex_union(tree, filters):
    union_find = UnionFind(tree.number_vertices)

    if filters.remove_outliers:
        tree.flatten_neighbours()

    tree.calc_wasser_dist()
    tree.sort()

    err_margin = (tree.max_wasser - tree.min_wasser) * filters.wasser_error
    error_range = tree.min_wasser + err_margin

    minimum_edges = []
    for edge in tree.edges:
        if union_find.num_components <= filters.num_clusters:
            break

        if edge.wasser_cost == -1:
            continue

        if not union_find.connected(edge.src, edge.dest) and __wasser_cost_in_range(edge.wasser_cost, error_range):
            union_find.unify(edge.src, edge.dest)
            minimum_edges.append(edge)

    for edge in tree.edges:
        union_find.find_root_elem(edge.src)
        union_find.find_root_elem(edge.dest)

    return MinTreeWasserClusterPlot(tree.edges, minimum_edges, union_find, filters.num_clusters)


def __wasser_cost_in_range(wasser_cost, error_range):
    return wasser_cost <= error_range
