def create_color_map_by_size_decreasing(labels, num_components):
    labels.sort(key=lambda x: x.sz, reverse=True)

    color_dict = {}
    for i in range(0, num_components):
        color_dict[labels[i].id] = labels[i].new_label

    return color_dict
