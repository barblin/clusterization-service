
class ClusterFilters:
    def __init__(self, num_clusters, wasser_error, remove_outliers):
        if num_clusters is None:
            self.num_clusters = 6
        else:
            self.num_clusters = int(num_clusters)

        if wasser_error is None:
            self.wasser_error = 0
        else:
            self.wasser_error = float(wasser_error)

        if remove_outliers is None:
            self.remove_outliers = False
        else:
            self.remove_outliers = bool(remove_outliers)
