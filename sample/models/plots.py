class ScatterPlot:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels


class TriPlot:
    def __init__(self, dataframe, plot):
        self.dataframe = dataframe
        self.plot = plot


class MinTreeWasserClusterPlot:
    def __init__(self, minimum_edges, ids, components):
        self.minimum_edges = minimum_edges
        self.ids = ids
        self.components = components
