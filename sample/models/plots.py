class ScatterPlot:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels


class TriPlot:
    def __init__(self, dataframe, plot):
        self.dataframe = dataframe
        self.plot = plot


class MinTreeWasserClusterPlot:
    def __init__(self, data_frame, u_find):
        self.data_frame = data_frame
        self.u_find = u_find
