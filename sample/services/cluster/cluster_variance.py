import time

import numpy as np

from sample.models.variance import VarianceData
from sample.services.cluster.cluster_wasser import cluster
from sample.services.math import variance
from sample.services.score.score_service import get_file_nmi
from sample.services.tree.minimum_spanning_tree import compute_wasser_tree


def cluster_for_incr_wasser_dist(filename, filters):
    overall_time = time.time()
    start_time = overall_time

    tree = compute_wasser_tree(filename, filters)
    file_nmis = get_file_nmi(filename)

    samples = np.arange(filters.vars_from, filters.vars_until, filters.vars_step_size)
    sig_variances = [None] * len(samples)
    harmonic_clus_idx = 0
    cur_max_nmi = 0
    cur_idx = 0

    for i in samples:
        cluster_data = cluster(tree, i)

        in_clusters = variance(cluster_data.clusters)
        cur_var = np.var(in_clusters)

        if cur_max_nmi < cluster_data.nmi:
            cur_max_nmi = cluster_data.nmi
            harmonic_clus_idx = cur_idx

        sig_variances[cur_idx] = VarianceData(filename + str(int(i * 1000)), float(i), float(cur_var),
                                              cluster_data, time.time() - start_time, file_nmis,
                                              time.time() - overall_time)
        start_time = time.time()
        cur_idx += 1

    sig_variances[harmonic_clus_idx].significant = True
    return sig_variances


def cluster_for_wasser_dist(filename, filters):
    start_time = time.time()
    tree = compute_wasser_tree(filename, filters)
    cluster_data = cluster(tree, filters.wasser_error)
    file_nmis = get_file_nmi(filename)

    return VarianceData(filename, filters.wasser_error, 0, 0, cluster_data, time.time() - start_time, file_nmis,
                        time.time() - start_time)
