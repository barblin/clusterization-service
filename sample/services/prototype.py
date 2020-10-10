import sys
import os

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from scipy.stats import wasserstein_distance
from sklearn.neighbors import NearestNeighbors




# Choose point to visualize


sys.path.insert(0, '/home/sebastian/Documents/PhD/pyprojects/neighborhood')
from filter_neighborhood import local_reachability_density, lrd_filter, gauss_sample

lrd_data = local_reachability_density(df_nbh, k=4, n=15)
_, nbh_indices_lrd = lrd_filter(nbh_distance=nbh_distances, nbh_indices=nbh_indices, lrd_data=lrd_data, threshold=0.6,
                                keep_min=80)

_, nbh_indices_gauss = gauss_sample(nbh_distance=nbh_distances, nbh_indices=nbh_indices, alpha=1, power=1,
                                    draw_n_samples=300, weight_dist=30)





labels = db.labels_
unique_labels = np.unique(labels)
print(unique_labels)
# for l_i in unique_labels:
# break
# if len(labels[labels==l_i])<200 or len(labels[labels==l_i])>2500:
#    labels[labels==l_i] = -1
np.unique(labels)

REMOVE = False
if REMOVE:
    for li in [5, 6, 7]:
        labels[labels == li] = -1

np.unique(labels)

from sklearn.metrics import adjusted_mutual_info_score

adjusted_mutual_info_score(data['labels'],
                           labels)  # if you choose to merge the regions (set REMOVE=True 2 cells above) then you can improve the AMI to ~0.87 in the


def local_reachability_density(data, k, n, **nn_kwargs):
    """
    Reachability distance: maximum of the distance of two points and the k-distance of the second point
    In practice we only need the reachability distance between the nearest neighbors, so therefore we first build a kd/ball tree and then calculate the
    :param data: pandas DataFrame or numpy.ndarray
    :param k: integer; distance to that neighbor is calculated (for k-distance)
    :param n: Number of nearest neighbors used to calculate the LRD
    :param nn_kwargs: Kwargs for NearestNeighbors class (sklearn)
    :return: local reachability density for each point in the input data set 'data'
    """
    if not isinstance(data, (pd.DataFrame, pd.Series, np.ndarray)):
        raise TypeError('Variable "df" has to be of type pandas.DataFrame or pandas.Series')
    nn = NearestNeighbors(n_neighbors=n + 1, **nn_kwargs).fit(data)
    ndist, _ = nn.kneighbors(data, n_neighbors=n + 1, return_distance=True)
    # the first k distances are now set to the k-distance
    k_dist_idx = lambda i, k: i if (i > k) else k  # k-distance indices
    idx = [k_dist_idx(i, k) for i in range(1, n + 1)]
    k_dist = ndist[:, idx]
    # one over LRD
    oo_lrd = np.sum(k_dist, axis=1) / n
    return 1 / oo_lrd


lrd = local_reachability_density(data[columns], k=3, n=10)
