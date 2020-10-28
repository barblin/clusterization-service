import json


class TripleView:
    def __init__(self, tree_max_x, tree_max_y, tree_data, scatter_max_x, scatter_max_y, scatter_data):
        self.tree_max_x = tree_max_x
        self.tree_max_y = tree_max_y
        self.tree_data = tree_data
        self.scatter_max_x = scatter_max_x
        self.scatter_max_y = scatter_max_y
        self.scatter_data = scatter_data

    def jsonify(self):
        return json.dumps(self.__dict__)
