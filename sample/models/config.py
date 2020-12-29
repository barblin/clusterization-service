SIMPLE_PLOT = "simple-plots"
CLUSTER = "clusters"
DELAUNAY_TRIANGULATION = "delaunay-triangulation"
MINIMUM_SPANNING_TREE = "minimum-spanning-tree"
MINIMUM_SPANNING_TREE_WASSER = "minimum-spanning-tree-wasser"
MIN_TREE_WASSER_CLUSTER = "clusters-min-tree-wasser"
TRIPLE_PLOTS = "multi-plots"
VARIANCES_PLOTS = "variances-plots"

SUPPORTED_VIEWS = [[SIMPLE_PLOT, "Scatter plot original data"],
                   [DELAUNAY_TRIANGULATION, "Delaunay Triangulation"],
                   [MINIMUM_SPANNING_TREE, "Minimum spanning tree 2D"],
                   [MINIMUM_SPANNING_TREE_WASSER, "Min tree by Wasserstein distance"],
                   [MIN_TREE_WASSER_CLUSTER, "Cluster by Wasserstein distance"],
                   [TRIPLE_PLOTS, "Cluster scores"],
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
