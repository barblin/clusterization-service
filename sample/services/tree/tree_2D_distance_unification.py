from sample.models.plots import MinTreeWasserClusterPlot
from sample.services.cluster.union_find import UnionFind


def unify_by_wasser_distnace(tree, filters):
    tree.sort_wasser()
    return __2d_distance_vertex_union(tree, filters.wasser_error)


def __2d_distance_vertex_union(tree, wasser_error):
    union_find = UnionFind(tree.point_array)

    err_margin = (tree.max_wasser - tree.min_wasser) * wasser_error
    error_range = tree.min_wasser + err_margin

    minimum_edges = []
    for edge in tree.edges:
        if edge.wasser_cost == -1:
            continue

        if not union_find.connected(edge.src, edge.dest) and __wasser_cost_in_range(edge.wasser_cost, error_range):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)
            minimum_edges.append(edge)

    for edge in tree.edges:
        union_find.find_root_elem(edge.src)
        union_find.find_root_elem(edge.dest)

    return MinTreeWasserClusterPlot(tree.edges, minimum_edges, union_find)


def __wasser_cost_in_range(wasser_cost, error_range):
    return 0 <= wasser_cost <= error_range
