import os

SIMPLE_PLOT = "simple-plots"
DELAUNAY_TRIANGULATION = "delaunay-triangulation"
MINIMUM_SPANNING_TREE = "min-span-tree"
MINIMUM_SPANNING_TREE_WASSER = "min-span-tree-wasser"
MIN_TREE_WASSER_CLUSTER = "cluster"
TRIPLE_PLOTS = "cluster-compare"
VARIANCES_PLOTS = "scores"

SUPPORTED_VIEWS = [[SIMPLE_PLOT, "Scatter plot original data"],
                   [DELAUNAY_TRIANGULATION, "Delaunay Triangulation"],
                   [MINIMUM_SPANNING_TREE, "Minimum spanning tree 2D"],
                   [MINIMUM_SPANNING_TREE_WASSER, "Min tree by Wasserstein distance"],
                   [MIN_TREE_WASSER_CLUSTER, "Cluster by Wasserstein distance"],
                   [VARIANCES_PLOTS, "Cluster scores for range"]]
SUPPORTED_ALGOS = []

FILE_NMIS = {
    "skinnyDipData_0.csv": {"skinny": 0.80},
    "skinnyDipData_1.csv": {"skinny": 0.81},
    "skinnyDipData_2.csv": {"skinny": 0.83},
    "skinnyDipData_3.csv": {"skinny": 0.84},
    "skinnyDipData_4.csv": {"skinny": 0.82},
    "skinnyDipData_5.csv": {"skinny": 0.82},
    "skinnyDipData_6.csv": {"skinny": 0.81},
    "skinnyDipData_7.csv": {"skinny": 0.81},
    "skinnyDipData_8.csv": {"skinny": 0.81},
    "skinnyDipData_9.csv": {"skinny": 0.70},
    "waveData_0.csv": {"skinny": 0.6, "ada": 0.8},
    "waveData_1.csv": {"skinny": 0.6, "ada": 0.8},
    "waveData_2.csv": {"skinny": 0.55, "ada": 0.8},
    "waveData_3.csv": {"skinny": 0.5, "ada": 0.79},
    "waveData_4.csv": {"skinny": 0.52, "ada": 0.78},
    "waveData_5.csv": {"skinny": 0.49, "ada": 0.76},
    "waveData_6.csv": {"skinny": 0.45, "ada": 0.8},
    "waveData_7.csv": {"skinny": 0.43, "ada": 0.75},
    "waveData_8.csv": {"skinny": 0.42, "ada": 0.71},
    "waveData_9.csv": {"skinny": 0.2, "ada": 0.55},
}

FILE_NEIGHS = {
    "CutESC.csv": 20,
    "skinnyDipData_0.csv": 5,
    "skinnyDipData_1.csv": 50,
    "skinnyDipData_2.csv": 100,
    "skinnyDipData_3.csv": 200,
    "skinnyDipData_4.csv": 200,
    "skinnyDipData_5.csv": 250,
    "skinnyDipData_6.csv": 250,
    "skinnyDipData_7.csv": 150,
    "skinnyDipData_8.csv": 300,
    "skinnyDipData_9.csv": 450,
    "waveData_0.csv": 30,
    "waveData_1.csv": 30,
    "waveData_2.csv": 30,
    "waveData_3.csv": 35,
    "waveData_4.csv": 100,
    "waveData_5.csv": 200,
    "waveData_6.csv": 200,
    "waveData_7.csv": 350,
    "waveData_8.csv": 350,
    "waveData_9.csv": 450,
}

dir_path = os.path.dirname(os.path.realpath(__file__))
source_location = dir_path + '/../../ressources/syntheticData/'
edge_location = dir_path + '/../../ressources/edges/'
var_location = dir_path + '/../../ressources/variances/'


def resources():
    return source_location


def edges_location():
    return edge_location


def variances_location():
    return var_location
