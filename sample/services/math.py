import math

import numpy as np


def two_d_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def calc_cutoff(neighs, stdv_multiplier):
    value = neighs
    arr = np.array(value)
    mean = np.mean(arr)
    sd = np.std(arr)

    return mean + stdv_multiplier * sd


def variance(clusters):
    variances = []

    for key in clusters:
        if len(clusters[key].costs) > 0:
            var = np.var(clusters[key].costs)

            if str(var) != 'nan' and var != 0:
                variances.append(float(var))
                clusters[key].var = var

    return variances
