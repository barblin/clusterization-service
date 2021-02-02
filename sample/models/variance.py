import json


class VarianceData:
    def __init__(self, id, wasser_margin, variance, plot, runtime, nmis, overall_time, nmi):
        self.identity = id
        self.wasser_margin = float(wasser_margin)
        self.cluster_variance = variance
        self.max_X = plot.max_features[0]
        self.max_Y = plot.max_features[1]
        self.significant = False
        self.nmi = nmi
        self.runtime = float(runtime)
        self.skinny_nmi = float(nmis.skinny)
        self.ada_nmi = float(nmis.ada)
        self.overall_time = float(overall_time)

    def jsonify(self):
        return json.dumps(self.__dict__)
