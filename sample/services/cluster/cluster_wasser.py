from sample.services.cluster.union_find import Cluster
from sample.services.data.color_mapping import create_cluster_by_size_decreasing
from sample.services.score.score_service import calc_score_from_clusters


class ClusterData:
    def __init__(self, clusters, max_x, max_y, nmi):
        self.clusters = clusters
        self.max_x = max_x
        self.max_y = max_y
        self.nmi = nmi


def cluster(union_find, tree, wass_err):
    wasser_range = calc_error_range(tree, wass_err)
    cluster_candidates = unify(union_find, tree.edges, wasser_range)
    sig_clusters = reduce_to_significant(cluster_candidates)
    complete_clusters = add_noise_cluster(sig_clusters, tree, cluster_candidates)
    score = calc_score_from_clusters(complete_clusters, tree.point_array)
    return ClusterData(complete_clusters, cluster_candidates.max_x, cluster_candidates.max_y, score.nmi)


def add_noise_cluster(clusters, tree, union_find):
    noise_cluster = Cluster(-1, 0, 8, [], 0)
    already_managed_noise_cluster = {}

    for edge in tree.edges:
        root_src = union_find.find_root_elem(edge.src)
        root_dest = union_find.find_root_elem(edge.dest)

        if not union_find.connected(edge.src, edge.dest):
            if root_src not in clusters.keys() and root_src not in already_managed_noise_cluster:
                union_find.id_sz[root_src].new_label = -1
                noise_cluster.merge(union_find.id_sz[root_src])
                already_managed_noise_cluster[root_src] = None

            if root_dest not in clusters.keys() and root_dest not in already_managed_noise_cluster:
                union_find.id_sz[root_dest].new_label = -1
                noise_cluster.merge(union_find.id_sz[root_dest])
                already_managed_noise_cluster[root_dest] = None

    clusters[noise_cluster.id] = noise_cluster

    return clusters


def calc_error_range(tree, wasser_error):
    err_margin = (tree.max_wasser - tree.min_wasser) * wasser_error
    error_range = tree.min_wasser + err_margin

    return error_range


def unify(union_find, filtered_edges, error_range):
    start = union_find.offset

    for i in range(start, len(filtered_edges)):
        edge = filtered_edges[i]

        if edge.wasser_cost == -1:
            continue
        if not __wasser_cost_in_range(edge.wasser_cost, error_range):
            union_find.offset = i
            break
        if not union_find.connected(edge.src, edge.dest):
            union_find.unify(edge.src, edge.dest, edge.wasser_cost)

    return union_find


def reduce_to_significant(uf):
    return create_cluster_by_size_decreasing(uf)


def __wasser_cost_in_range(wasser_cost, error_range):
    return 0 <= wasser_cost <= error_range
