import unittest
import leafnode


class LeafNodeTest(unittest.TestCase):
    def test_to_html(self):
        node1 = leafnode.LeafNode("p", "yoyoyothis how it do")
        node2 = leafnode.LeafNode("a", "google", {"href": "www.google.com"})
        print(node1.to_html())
        print(node2.to_html())

    def test_repr(self):
        node1 = leafnode.LeafNode("p", "yoyoyothis how it do")
        node2 = leafnode.LeafNode("a", "google", {"href": "www.google.com"})
        print(node1)
        print(node2)