from scipy.spatial import Delaunay
from sample.services import datasource
from sample.models.plots import TriPlot


def triangulate(filename):
    df = datasource.load_file(filename)
    del df['labels']
    point_array = df.to_numpy()

    tri = Delaunay(point_array)

    data = []
    for entries in tri.simplices:
        row = []
        for entry in entries:
            row.append(point_array[entry].tolist())
        data.append(row)

    return TriPlot(df, data)
