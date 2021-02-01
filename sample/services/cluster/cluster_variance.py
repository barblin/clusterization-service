import time

import numpy as np

from sample.models.variance import VarianceData
from sample.models.variance_plot import VariancePlot
from sample.services.cluster.cluster_wasser import cluster
from sample.services.cluster.union_find import UnionFind
from sample.services.data.variance_source import delete_repo, store, load
from sample.services.math import variance
from sample.services.score.score_service import get_file_nmi
from sample.services.tree.minimum_spanning_tree import compute_wasser_tree


def cluster_for_incr_wasser_dist(filename, filters):
    delete_repo()

    overall_time = time.time()
    start_time = overall_time

    tree = compute_wasser_tree(filename)
    union_find = UnionFind(tree.point_array)
    file_nmis = get_file_nmi(filename)

    samples = np.arange(filters.vars_from, filters.vars_until, filters.vars_step_size)
    sig_variances = [None] * len(samples)
    harmonic_clus_idx = 0
    cur_max_nmi = 0
    cur_idx = 0

    for i in samples:
        cluster_data = cluster(union_find, tree, i)

        in_clusters = variance(cluster_data.clusters)

        cur_var = 0
        if 0 < len(in_clusters):
            cur_var = np.var(in_clusters)

        if cur_max_nmi < cluster_data.nmi:
            cur_max_nmi = cluster_data.nmi
            harmonic_clus_idx = cur_idx

        identity = "v" + str(cur_idx) + filename
        variance_data = VarianceData(identity, float(i), float(cur_var),
                                     cluster_data, time.time() - start_time, file_nmis,
                                     time.time() - overall_time)
        variance_plot = VariancePlot(identity, float(i), float(cur_var),
                                     cluster_data, time.time() - start_time, file_nmis,
                                     time.time() - overall_time)

        sig_variances[cur_idx] = variance_data
        store(variance_plot)

        start_time = time.time()
        cur_idx += 1

    sig_variances[harmonic_clus_idx].significant = True
    return sig_variances


def load_plot(identity):
    return load(identity)


def cluster_for_wasser_dist(filename, filters):
    start_time = time.time()
    tree = compute_wasser_tree(filename)
    union_find = UnionFind(tree.point_array)
    cluster_data = cluster(union_find, tree, filters.wasser_error)
    file_nmis = get_file_nmi(filename)

    return VariancePlot(filename, filters.wasser_error, 0, cluster_data, time.time() - start_time, file_nmis,
                        time.time() - start_time)
