
class ClusterFilters:
    def __init__(self, num_clusters, wasser_error, dist_error):
        if num_clusters is None:
            self.num_clusters = 6
        else:
            self.num_clusters = int(num_clusters)

        if wasser_error is None:
            self.wasser_error = 0
        else:
            self.wasser_error = float(wasser_error)

        if dist_error is None:
            self.dist_error = 0
        else:
            self.dist_error = float(dist_error)
