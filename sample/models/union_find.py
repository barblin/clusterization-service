
class Cluster:
    def __init__(self, id, sz, new_label, old_label):
        self.id = id
        self.sz = sz
        self.new_label = new_label
        self.old_label = old_label
        self.costs = []


class UnionFind:
    def __init__(self, vertex_data):
        size = len(vertex_data)

        self.size = size
        self.num_components = size

        self.id_sz = [None] * size
        for i in range(0, size):
            self.id_sz[i] = Cluster(i, 1, vertex_data[i][2], vertex_data[i][2])

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
            self.id_sz[root2].sz += self.id_sz[root1].sz
            self.id_sz[root2].costs.append(w_cost)
            self.id_sz[root2].costs.extend(self.id_sz[root1].costs)

            self.id_sz[root1].id = root2
            self.id_sz[root1].new_label = self.id_sz[root2].old_label
        else:
            self.id_sz[root1].sz += self.id_sz[root2].sz
            self.id_sz[root1].costs.append(w_cost)
            self.id_sz[root1].costs.extend(self.id_sz[root2].costs)

            self.id_sz[root2].id = root1
            self.id_sz[root2].new_label = self.id_sz[root1].old_label

        self.num_components = self.num_components - 1
