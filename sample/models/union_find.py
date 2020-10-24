class UnionFind:
    def __init__(self, size):

        self.size = size
        self.num_components = size

        self.id_sz = {}
        for i in range(0, size):
            self.id_sz[i] = [i, 1]

    def connected(self, p, q):
        return self.find_root_elem(p) == self.find_root_elem(q)

    def find_root_elem(self, p):
        root = p
        while root != self.id_sz[root][0]:
            root = self.id_sz[root][0]

        while p != root:
            next_el = self.id_sz[p][0]
            self.id_sz[p][0] = root
            p = next_el

        return root

    def unify(self, p, q):
        root1 = self.find_root_elem(p)
        root2 = self.find_root_elem(q)

        if root1 == root2:
            return

        if self.id_sz[root1][1] < self.id_sz[root2][1]:
            self.id_sz[root2][1] += self.id_sz[root1][1]
            self.id_sz[root1][0] = root2
        else:
            self.id_sz[root1][1] += self.id_sz[root2][1]
            self.id_sz[root2][0] = root1

        self.num_components = self.num_components - 1
