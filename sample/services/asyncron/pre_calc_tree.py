import threading

from sample.services.data.datasource import list_files
from sample.services.data.tree_source import store_edges
from sample.services.tree.tree_factory import create_tree


def issue(offset=0):
    x = threading.Thread(target=__calc, args=[offset])
    x.start()


def __calc(offset):
    files = list_files()
    files.sort(reverse=True)

    for filename in files:
        if offset > 0:
            offset -= 1
            continue

        print("create tree for " + filename)
        tree = create_tree(filename)
        print("wasser calculation for " + filename)
        tree.clean_wasser_calc()
        print("sort edges for " + filename)
        tree.sort_wasser()
        print("store edges for " + filename)
        store_edges(tree.edges, filename)
