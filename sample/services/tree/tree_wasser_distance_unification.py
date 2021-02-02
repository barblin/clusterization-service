from cluswasser.union_find import UnionFind


def unify_wasser(tree, labels):
    union_find = UnionFind(tree.features, labels)

    filtered_edges = []
    for edge in tree.edges:
        if not union_find.connected(edge.src, edge.dest):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)
            filtered_edges.append(edge)

    return filtered_edges


def wasser_vertex_union(tree, wasser_error):
    err_margin = (tree.max_wasser - tree.min_wasser) * wasser_error
    error_range = tree.min_wasser + err_margin

    filtered_edges = []
    for edge in tree.edges:
        if __wasser_cost_in_range(edge.wasser_cost, error_range):
            filtered_edges.append(edge)

    return filtered_edges


def unify(point_array, filtered_edges):
    union_find = UnionFind(point_array)

    for edge in filtered_edges:
        if edge.wasser_cost == -1:
            continue
        if not union_find.connected(edge.src, edge.dest):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)

    return union_find


def __wasser_cost_in_range(wasser_cost, error_range):
    return 0 <= wasser_cost <= error_range
