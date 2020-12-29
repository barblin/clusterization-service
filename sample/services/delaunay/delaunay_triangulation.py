from scipy.spatial import Delaunay
from sample.services.data import datasource
from sample.models.plots import TriPlot
from sample.services.data.datasource import data_without_labels

tri_cache = {}
delaunay_cache = {}


def triangulation_plot(filename):
    df = datasource.load_file(filename)
    point_array = data_without_labels(df)

    return TriPlot(df, triangulation_data(filename, point_array))


def triangulation_data(filename, point_array):
    if filename in tri_cache.keys():
        return tri_cache[filename]

    tri = triangulate_delaunay(filename, point_array)
    data = []
    for entries in tri.simplices:
        row = []
        for entry in entries:
            row.append(point_array[entry].tolist())
        data.append(row)

    tri_cache[filename] = data
    return tri_cache[filename]


def triangulate_delaunay(filename, point_array):
    if filename in delaunay_cache.keys():
        return delaunay_cache[filename]

    delaunay_cache[filename] = Delaunay(point_array)
    return delaunay_cache[filename]
