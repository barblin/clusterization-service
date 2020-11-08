SIMPLE_PLOT = "simple-plots"
CLUSTER = "clusters"
DELAUNAY_TRIANGULATION = "delaunay-triangulation"
MINIMUM_SPANNING_TREE = "minimum-spanning-tree"
MINIMUM_SPANNING_TREE_WASSER = "minimum-spanning-tree-wasser"
MIN_TREE_WASSER_CLUSTER = "clusters-min-tree-wasser"
TRIPLE_PLOTS = "multi-plots"

SUPPORTED_VIEWS = [[SIMPLE_PLOT, "Plot data as scatter"],
                   [DELAUNAY_TRIANGULATION, "Delaunay Triangulation"],
                   [MINIMUM_SPANNING_TREE, "Minimum spanning tree"],
                   [MINIMUM_SPANNING_TREE_WASSER, "Min tree by W distance"],
                   [MIN_TREE_WASSER_CLUSTER, "Vertices of min tree by W distance (labeled)"],
                   [TRIPLE_PLOTS, "Cross compare clusters"]]
SUPPORTED_ALGOS = []
