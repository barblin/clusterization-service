import threading

from cluswasser.tree import create_tree

from sample.config.config import FILE_NEIGHS
from sample.services.data.datasource import list_files, load_file, to_features
from sample.services.data.tree_source import store_edges


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

        data = load_file(filename)
        features = to_features(data)
        print("create tree for " + filename)
        tree = create_tree(features, FILE_NEIGHS[filename])
        print("store edges for " + filename)
        store_edges(tree.edges, filename)
