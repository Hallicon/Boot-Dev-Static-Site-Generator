import unittest
import parentnode
import leafnode


class ParentTest(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = leafnode.LeafNode("span", "child")
        parent_node = parentnode.ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = leafnode.LeafNode("b", "grandchild")
        child_node = parentnode.ParentNode("span", [grandchild_node])
        parent_node = parentnode.ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_and_attributes(self):
        grandchild_node = leafnode.LeafNode(
            "b",
            "grandchild"
        )
        child_node = parentnode.ParentNode(
            "span",
            [grandchild_node],
            {"test_attr": "test_value"}
        )
        parent_node = parentnode.ParentNode(
            "div",
            [child_node],
            {"test_attr": "test_value"})

        # Debugging line here
        # print(parent_node.to_html())

        self.assertEqual(
            parent_node.to_html(),
            "<div test_attr=\"test_value\"><span test_attr=\"test_value\"><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
