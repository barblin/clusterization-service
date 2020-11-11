from sample.models.plots import MinTreeWasserClusterPlot
from sample.models.union_find import UnionFind


def unify_by_wasser_distance(tree, wasser_error, num_clusters):
    tree.sort()
    return __wasser_vertex_union(tree, wasser_error, num_clusters)


def __wasser_vertex_union(tree, wasser_error, num_clusters):
    union_find = UnionFind(tree.point_array)

    err_margin = (tree.max_wasser - tree.min_wasser) * wasser_error
    error_range = tree.min_wasser + err_margin

    minimum_edges = []
    for edge in tree.edges:
        if union_find.num_components <= num_clusters:
            break

        if edge.wasser_cost == -1:
            continue

        if not union_find.connected(edge.src, edge.dest) and __wasser_cost_in_range(edge.wasser_cost, error_range):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)
            minimum_edges.append(edge)

    for edge in tree.edges:
        union_find.find_root_elem(edge.src)
        union_find.find_root_elem(edge.dest)

    return MinTreeWasserClusterPlot(tree.edges, minimum_edges, union_find, num_clusters)


def __wasser_cost_in_range(wasser_cost, error_range):
    return 0 <= wasser_cost <= error_range