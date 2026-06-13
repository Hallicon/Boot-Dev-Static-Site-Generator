import unittest
import leafnode


class LeafNodeTest(unittest.TestCase):
    def test_to_html(self):
        node1 = leafnode.LeafNode("p", "yoyoyothis how it do")
        node2 = leafnode.LeafNode("a", "google", {"href": "www.google.com"})
        node3 = leafnode.LeafNode("img", "", {"src": "some_url_here"})
        self.assertEqual(node3.to_html(), "<img src=\"some_url_here\"></img>")
        # Debugging
        # print(node1.to_html())
        # print(node2.to_html())

    def test_repr(self):
        node1 = leafnode.LeafNode("p", "yoyoyothis how it do")
        node2 = leafnode.LeafNode("a", "google", {"href": "www.google.com"})
        # Debugging
        # print(node1)
        # print(node2)


if __name__ == "__main__":
    unittest.main()
