def create_cluster_by_size_decreasing(uf):
    labels = uf.id_sz.copy()
    labels.sort(key=lambda x: x.sz, reverse=True)

    j = 0
    cluster_dict = {}
    for i in range(0, 8):
        cluster = labels[i]

        if cluster.id not in cluster_dict.keys():
            cluster.new_label = j
            cluster_dict[cluster.id] = cluster
            j += 1

        i += 1

    return cluster_dict


def create_color_map_by_size_decreasing(labels):
    labels.sort(key=lambda x: x.sz, reverse=True)

    j = 0
    color_dict = {}
    for i in range(0, len(labels)):
        color_dict[labels[i].id] = str(j)
        j += 1

    return color_dict
