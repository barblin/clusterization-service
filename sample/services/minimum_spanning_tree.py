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
    tree.flatten_neighbours()
    tree.calc_wasser_dist()
    tree.sort()
    minimum_edges = []

    avg_wass_d = tree.average_wasser_dist
    err_margin = avg_wass_d * filters.wasser_error
    error_range = [avg_wass_d - err_margin, avg_wass_d + err_margin]

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

    return MinTreeWasserClusterPlot(minimum_edges, union_find.id, union_find.num_components)


def __wasser_cost_in_range(wasser_cost, error_range):
    return wasser_cost <= error_range[1]
