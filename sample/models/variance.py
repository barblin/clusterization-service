import json

import numpy as np


class VarianceData:
    def __init__(self, id, wasser_margin, variance, in_variances, plot, runtime, nmis):
        cluster_array = []

        self.sum_sz = 0
        for key in plot.clusters.keys():
            clus = plot.clusters[key]
            self.sum_sz += clus.sz
            cluster_array.append((
                int(clus.id),
                int(clus.new_label),
                int(clus.sz),
                clus.vertices,
                np.sum(clus.costs),
                clus.variance))

        self.identity = id
        self.wasser_margin = float(wasser_margin)
        self.cluster_variance = variance
        self.in_cluster_variances = in_variances
        self.max_X = plot.max_x
        self.max_Y = plot.max_x
        self.data = cluster_array
        self.significant = False
        self.nmi = plot.nmi
        self.runtime = runtime
        self.skinny_nmi = float(nmis.skinny)
        self.ada_nmi = float(nmis.ada)

    def jsonify(self):
        return json.dumps(self.__dict__)
