from scipy.spatial import Delaunay
from sample.services import datasource
from sample.models.plots import TriPlot
from sample.services.datasource import data_without_labels


def triangulate(filename):
    df = datasource.load_file(filename)
    point_array = data_without_labels(df)

    return TriPlot(df, triangulation_data(point_array))


def triangulation_data(point_array):
    tri = triangulate_delaunay(point_array)
    data = []
    for entries in tri.simplices:
        row = []
        for entry in entries:
            row.append(point_array[entry].tolist())
        data.append(row)

    return data


def triangulate_delaunay(point_array):
    return Delaunay(point_array)
