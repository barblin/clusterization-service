from sample.services import dataset
from sample.services import find_neighbours
from sample.services import plot
from sample.services.wasserstein_distance import distances
from sklearn.cluster import DBSCAN  # DBSCAN gives us "wasserstein" connected points
import numpy as np


def plot_clusters(filename):
    data = dataset.load_file(filename)
    nbs = find_neighbours.execute(data)
    dist_mtrx = distances(nbs)
    db = DBSCAN(metric="precomputed", eps=0.5, min_samples=50).fit(dist_mtrx)

    labels = db.labels_
    unique_labels = np.unique(labels)
    print(unique_labels)
    np.unique(labels)

    remove = False
    if remove:
        for li in [5, 6, 7]:
            labels[labels == li] = -1

    np.unique(labels)
    plot.plot_cluster(data, labels)
