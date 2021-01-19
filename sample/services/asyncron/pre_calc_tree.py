import threading

from sample.services.data.datasource import list_files
from sample.services.data.tree_source import store_edges
from sample.services.tree.tree_factory import create_tree


def issue():
    x = threading.Thread(target=__calc)
    x.start()


def __calc():
    for filename in list_files():
        print("create tree for " + filename)
        tree = create_tree(filename)
        print("wasser calculation for " + filename)
        tree.clean_wasser_calc()
        print("sort edges for " + filename)
        tree.sort_wasser()
        print("store edges for " + filename)
        store_edges(tree.edges, filename)
