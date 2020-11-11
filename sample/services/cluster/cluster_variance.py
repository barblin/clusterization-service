from sample.services.tree.minimum_spanning_tree import get_and_prep_tree
from sample.services.tree.tree_wasser_distance_unification import unify_by_wasser_distance
import numpy as np


def cluster_for_incr_wasser_dist(filename, filters):
    tree = get_and_prep_tree(filename, filters)

    significant_variances = {}

    last_variance = 0
    curr_margin = 0
    for i in range(0, 142):
        wasser_cluster = unify_by_wasser_distance(tree, curr_margin, 1)
        curr_margin += 0.0001

        vars_in_clusters = __calc_in(wasser_cluster.union_find)
        var_between_clusters = np.var(vars_in_clusters)

        if last_variance < var_between_clusters:
            significant_variances[curr_margin] = [var_between_clusters, vars_in_clusters]
            last_variance = var_between_clusters

    return significant_variances


def __calc_in(uf):
    unique_clusters = {}

    for i in range(0, len(uf.id_sz)):
        root = uf.find_root_elem(i)

        if uf.id_sz[root].sz > 1:
            unique_clusters[root] = uf.id_sz[root].costs

    variances = []

    for k, v in unique_clusters.items():
        variance = np.var(v)

        if variance > 0:
            variances.append(variance)
        else:
            print(uf.id_sz[root].sz)

    return variances
