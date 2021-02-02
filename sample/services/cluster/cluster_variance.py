import time

import numpy as np
from cluswasser.cluster import wasser, wasser_range

from sample.config.config import FILE_NEIGHS
from sample.models.variance import VarianceData
from sample.models.variance_plot import VariancePlot
from sample.services.data.datasource import load_file, to_features, to_labels
from sample.services.data.tree_source import load_edges
from sample.services.data.variance_source import delete_repo, store, load
from sample.services.math import variance
from sample.services.score.score_service import get_file_nmi, calc_score_from_clusters


def cluster_for_incr_wasser_dist(filename, filters):
    delete_repo()
    overall_time = time.time()
    start_time = overall_time

    file_nmis = get_file_nmi(filename)
    harmonic_clus_idx = 0
    cur_max_nmi = 0
    cur_idx = 0

    edges = fetch_edges(filename)
    data = load_file(filename)
    features = to_features(data)
    labels = to_labels(data)

    increments = wasser_range(features, filters.vars_from, filters.vars_until, filters.vars_step_size, labels,
                              FILE_NEIGHS[filename], edges)
    sig_variances = [None] * len(increments)

    for incr in increments:
        in_clusters = variance(incr.clusters)
        score = calc_score_from_clusters(incr.clusters, labels)

        cur_var = 0
        if 0 < len(in_clusters):
            cur_var = np.var(in_clusters)

        if cur_max_nmi < score.nmi:
            cur_max_nmi = score.nmi
            harmonic_clus_idx = cur_idx

        identity = "v" + str(cur_idx) + filename
        time_inc = time.time() - start_time
        full_time_inc = time.time() - overall_time

        margin = incr.wasser_margin
        info = VarianceData(identity, margin, float(cur_var), incr, time_inc, file_nmis, full_time_inc, score.nmi)
        plot = VariancePlot(identity, margin, float(cur_var), incr, time_inc, file_nmis, full_time_inc, score.nmi)

        sig_variances[cur_idx] = info
        store(plot)

        start_time = time.time()
        cur_idx += 1

    sig_variances[harmonic_clus_idx].significant = True
    return sig_variances


def load_plot(identity):
    return load(identity)


def cluster_for_wasser_dist(filename, filters):
    start_time = time.time()
    edges = fetch_edges(filename)
    data = load_file(filename)
    features = to_features(data)
    labels = to_labels(data)

    wasser_increment = wasser(features, filters.wasser_error, labels, FILE_NEIGHS[filename], edges)
    score = calc_score_from_clusters(wasser_increment.clusters, labels)
    file_nmis = get_file_nmi(filename)

    time_inc = time.time() - start_time
    return VariancePlot(filename, filters.wasser_error, 0, wasser_increment, time_inc, file_nmis, time_inc, score.nmi)


def fetch_edges(filename):
    return load_edges(filename)
