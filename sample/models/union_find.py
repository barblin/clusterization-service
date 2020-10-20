class UnionFind:
    def __init__(self, size):

        self.size = size
        self.num_components = size

        self.sz = [0] * size
        self.id = [0] * size

        for i in range(0, size):
            self.id[i] = i
            self.sz[i] = 1

    def connected(self, p, q):
        return self.find_root_elem(p) == self.find_root_elem(q)

    def find_root_elem(self, p):
        root = p
        while root != self.id[root]:
            root = self.id[root]

        while p != root:
            next_el = self.id[p]
            self.id[p] = root
            p = next_el

        return root

    def unify(self, p, q):
        root1 = self.find_root_elem(p)
        root2 = self.find_root_elem(q)

        if root1 == root2:
            return

        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        self.num_components -= 1
