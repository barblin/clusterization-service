class Cluster:
    def __init__(self, id, sz, new_label, vertices, old_label):
        self.id = id
        self.sz = sz
        self.new_label = new_label
        self.costs = []
        self.vertices = []
        self.vertices.extend(vertices)
        self.var = 0
        self.old_label = old_label
        self.unified_ids = set([])
        self.unified_ids.add(id)

    def merge(self, other):
        self.sz += other.sz
        self.costs.extend(other.costs)
        self.unified_ids.add(other.id)
        self.unified_ids.update(other.unified_ids)
        self.vertices.extend(other.vertices)

    def clone(self):
        clone = Cluster(self.id, self.sz, self.new_label, self.vertices.copy(), self.old_label)
        clone.costs = self.costs.copy()
        clone.unified_ids = self.unified_ids.copy()
        return clone


class UnionFind:
    def __init__(self, vertex_data):
        size = len(vertex_data)

        self.size = size
        self.num_components = size
        self.max_x = 0
        self.max_y = 0
        self.offset = 0

        self.id_sz = [None] * size
        for i in range(0, size):
            if self.max_x < vertex_data[i][0]:
                self.max_x = vertex_data[i][0]
            if self.max_y < vertex_data[i][1]:
                self.max_y = vertex_data[i][1]
            self.id_sz[i] = Cluster(i, 1, -1,
                                    [[float(vertex_data[i][0]), float(vertex_data[i][1])]],
                                    int(vertex_data[i][2]))

    def connected(self, p, q):
        return self.find_root_elem(p) == self.find_root_elem(q)

    def find_root_elem(self, p):
        root = p
        while root != self.id_sz[root].id:
            root = self.id_sz[root].id

        while p != root:
            next_el = self.id_sz[p].id
            self.id_sz[p].id = root
            p = next_el

        return root

    def unify(self, p, q, w_cost):
        root1 = self.find_root_elem(p)
        root2 = self.find_root_elem(q)

        if root1 == root2:
            return

        if self.id_sz[root1].sz < self.id_sz[root2].sz:
            self.id_sz[root2].merge(self.id_sz[root1])
            self.id_sz[root2].costs.append(float(w_cost))

            self.id_sz[root1].id = root2
        else:
            self.id_sz[root1].merge(self.id_sz[root2])
            self.id_sz[root1].costs.append(float(w_cost))

            self.id_sz[root2].id = root1

        self.num_components = self.num_components - 1
