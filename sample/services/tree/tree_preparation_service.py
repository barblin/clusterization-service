def apply_filters_and_wasser_distance(tree, filters):
    if filters.remove_outliers is True:
        tree.flatten_neighbours(filters.stdv_multiplier)

    if filters.normalize_neigh_dist is True:
        tree.normalize_neighbours()

    tree.calc_wasser_dist()
    return tree
