class ScatterPlot:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels


class TriPlot:
    def __init__(self, dataframe, plot):
        self.dataframe = dataframe
        self.plot = plot


class MinTreeWasserClusterPlot:
    def __init__(self, edges, minimum_edges, union_find, num_clusters):
        self.edges = edges
        self.minimum_edges = minimum_edges
        self.union_find = union_find
        self.num_clusters = num_clusters
