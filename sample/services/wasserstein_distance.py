from scipy.stats import wasserstein_distance
from scipy.sparse import csr_matrix


def distances(nbh):
    k_wasser = 200
    _, nbh_indices_wasser = nbh.nbh_model.kneighbors(nbh.df_nbh, k_wasser, return_distance=True)

    calc_wasserstein_index_set = set()
    for center_idx in range(nbh_indices_wasser.shape[0]):
        for idx in nbh_indices_wasser[center_idx][1:]:
            calc_wasserstein_index_set.add(frozenset({center_idx, idx}))
    len(calc_wasserstein_index_set)

    dist_list = nbh.nbh_distances

    row_indices = []
    col_indices = []
    wasserstein_dist = []
    for idx_set in calc_wasserstein_index_set:
        idx_i, idx_j = idx_set
        dist = wasserstein_distance(dist_list[idx_i], dist_list[idx_j])
        wasserstein_dist.extend([dist, dist])
        row_indices.extend([idx_i, idx_j])  # symmetrical matrix
        col_indices.extend([idx_j, idx_i])  # --------||---------

    nb_datapts = nbh.data.shape[0]
    return csr_matrix((wasserstein_dist, (row_indices, col_indices)), shape=(nb_datapts, nb_datapts))
