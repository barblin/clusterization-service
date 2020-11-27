import numpy as np

from sample.models.variance import VarianceData
from sample.services.cluster.cluster_wasser import cluster, prepare_tree
from sample.services.tree.minimum_spanning_tree import get_and_prep_tree


def cluster_for_incr_wasser_dist(filename, filters):
    tree = get_and_prep_tree(filename, filters)

    sig_variances = []
    index_of_harmonic_variance = 0
    cur_min_var_mean = 10000
    cur_idx = 0

    tree = prepare_tree(tree, filters.stdv_multiplier)

    for i in np.arange(filters.vars_from, filters.vars_until, filters.vars_step_size):
        cluster_data = cluster(tree, i)

        vars_in_clusters = __calc_in(cluster_data.clusters)
        cur_mean = cluster_data.clusters[-1].variance

        if cur_mean < cur_min_var_mean:
            cur_min_var_mean = cur_mean
            index_of_harmonic_variance = cur_idx

        sig_variances.append(VarianceData("pl" + str(len(sig_variances)), float(i), float(cur_mean),
                                          vars_in_clusters, cluster_data))

        cur_idx += 1

    sig_variances[index_of_harmonic_variance].significant = True
    return sig_variances


def cluster_for_wasser_dist(filename, filters):
    tree = get_and_prep_tree(filename, filters)
    tree = prepare_tree(tree, filters.stdv_multiplier)
    cluster_data = cluster(tree, filters.wasser_error)
    vars_in_clusters = __calc_in(cluster_data.clusters)
    cur_mean = cluster_data.clusters[-1].variance
    return VarianceData("pl", filters.wasser_error, float(cur_mean), vars_in_clusters, cluster_data)


def __calc_in(clusters):
    variances = []

    for key in clusters:
        variance = np.var(clusters[key].costs)

        if str(variance) != 'nan' and variance != 0:
            variances.append(float(variance))
            clusters[key].variance = variance

    return variances
