import unittest
from sample.models.cluster_tree import DistanceTree
from sample.models.cluster_tree import Edge


class MyTestCase(unittest.TestCase):
    def test_tree_is_sorted_in_right_order(self):
        tree = DistanceTree(3)
        edge1 = Edge(1, 2, 10)
        edge2 = Edge(2, 1, 4)
        edge3 = Edge(2, 3, 1)
        edge4 = Edge(1, 3, 99)

        tree.add_edge(edge1)
        tree.add_edge(edge2)
        tree.add_edge(edge3)
        tree.add_edge(edge4)

        tree.sort()

        self.assertEqual([edge3, edge2, edge1, edge4], tree.edges, "Is supposed to be sorted")


if __name__ == '__main__':
    unittest.main()