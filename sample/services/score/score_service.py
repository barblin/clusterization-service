import numpy
from scipy.spatial.distance import euclidean
from sklearn.metrics.cluster import normalized_mutual_info_score

from sample.config.config import FILE_NMIS
from sample.services.score.dbcv import DBCV


class ScoreData:
    def __init__(self, nmi, dbcv):
        self.nmi = nmi
        self.dbcv = dbcv


class FileNmis:
    def __init__(self, skinny, ada):
        self.skinny = skinny
        self.ada = ada


def calc_score_from_clusters(clusters, labels):
    size = len(labels)

    actual = []
    predicted = [-1] * size
    for i in range(0, size):
        for key in clusters.keys():
            cluster = clusters[key]
            if i in cluster.unified_ids:
                predicted[i] = cluster.old_label
        actual.append(int(labels[i]))

    nmi = __calc_nmi(actual, predicted)
    dbcv = []  # __calc_dbcv(point_array[:, :2], predicted)

    return ScoreData(nmi, dbcv)


def get_file_nmi(filename):
    skinny = 0
    ada = 0

    if filename in FILE_NMIS.keys():
        file_nmis = FILE_NMIS[filename]

        if "skinny" in file_nmis:
            skinny = file_nmis["skinny"]
        if "ada" in file_nmis:
            ada = file_nmis["ada"]

    return FileNmis(skinny, ada)


def __calc_nmi(actual, predicted):
    return normalized_mutual_info_score(numpy.array(actual), numpy.array(predicted))


def __calc_dbcv(point_array, predicted):
    return DBCV(point_array, numpy.array(predicted), dist_function=euclidean)
