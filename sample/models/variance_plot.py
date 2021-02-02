import json

import numpy as np


class VariancePlot:
    def __init__(self, id, wasser_margin, variance, plot, runtime, nmis, overall_time, nmi):
        cluster_array = []

        self.sum_sz = 0

        for key in plot.clusters.keys():
            clus = plot.clusters[key]
            self.sum_sz += len(clus.features)

            cluster_array.append((
                int(clus.identity),
                int(clus.new_label),
                int(len(clus.features)),
                clus.features,
                np.sum(clus.costs),
                0))

        self.identity = id
        self.wasser_margin = float(wasser_margin)
        self.cluster_variance = variance
        self.max_X = float(plot.max_features[0])
        self.max_Y = float(plot.max_features[1])
        self.data = cluster_array
        self.significant = False
        self.nmi = nmi
        self.runtime = float(runtime)
        self.skinny_nmi = float(nmis.skinny)
        self.ada_nmi = float(nmis.ada)
        self.overall_time = float(overall_time)

    def jsonify(self):
        return json.dumps(self.__dict__)
