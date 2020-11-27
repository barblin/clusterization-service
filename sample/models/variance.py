import json

import numpy as np


class VarianceData:
    def __init__(self, identity, wasser_margin, cluster_variance, in_cluster_variances, wasser_scatter_plot):
        cluster_array = []

        self.sum_sz = 0
        for key in wasser_scatter_plot.clusters.keys():
            clus = wasser_scatter_plot.clusters[key]
            self.sum_sz += clus.sz
            cluster_array.append((
                int(clus.id),
                int(clus.new_label),
                int(clus.sz),
                clus.vertices,
                np.sum(clus.costs),
                clus.variance))

        self.identity = identity
        self.wasser_margin = wasser_margin
        self.cluster_variance = cluster_variance
        self.in_cluster_variances = in_cluster_variances
        self.max_X = wasser_scatter_plot.max_x
        self.max_Y = wasser_scatter_plot.max_x
        self.data = cluster_array
        self.significant = False

    def jsonify(self):
        return json.dumps(self.__dict__)
