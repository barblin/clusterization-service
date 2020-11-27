from sample.models.union_find import UnionFind, Cluster
from sample.services.color.color_mapping import create_cluster_by_size_decreasing


class ClusterData:
    def __init__(self, clusters, max_x, max_y):
        self.clusters = clusters
        self.max_x = max_x
        self.max_y = max_y


def prepare_tree(tree, stdv_multiplier):
    tree.sort()
    tree.remove_outliers(stdv_multiplier)
    tree.flatten_neighbours(stdv_multiplier)
    tree.calc_wasser_dist()
    return tree


def cluster(tree, wass_err):
    edges = filter_by_wasser_dist(tree, wass_err)
    cluster_candidates = unify(tree.point_array, edges)
    sig_clusters = reduce_to_significant(cluster_candidates)
    complete_clusters = add_noise_cluster(sig_clusters, tree, cluster_candidates)
    return ClusterData(complete_clusters, cluster_candidates.max_x, cluster_candidates.max_y)


def add_noise_cluster(clusters, tree, union_find):
    for edge in tree.edges:
        root_src = union_find.find_root_elem(edge.src)
        root_dest = union_find.find_root_elem(edge.dest)

        if root_src in clusters.keys() or root_dest in clusters.keys():
            continue

        if not union_find.connected(edge.src, edge.dest):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)

    noise_cluster = Cluster(-1, 0, 8, [])
    already_managed_noise_cluster = {}
    for i in range(0, len(union_find.id_sz)):
        root = union_find.find_root_elem(union_find.id_sz[i].id)
        if root not in clusters.keys() and root not in already_managed_noise_cluster.keys():
            noise_cluster.sz += union_find.id_sz[root].sz
            noise_cluster.costs.extend(union_find.id_sz[root].costs)
            noise_cluster.vertices.extend(union_find.id_sz[root].vertices)
            already_managed_noise_cluster[root] = None

    clusters[noise_cluster.id] = noise_cluster

    return clusters


def filter_by_wasser_dist(tree, wasser_error):
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


def reduce_to_significant(uf):
    return create_cluster_by_size_decreasing(uf)


def __wasser_cost_in_range(wasser_cost, error_range):
    return 0 <= wasser_cost <= error_range
