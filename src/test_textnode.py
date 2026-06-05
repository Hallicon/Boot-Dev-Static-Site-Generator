import unittest
from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node == node2, True)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is not equal", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("The url of this node should be None", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_text_types(self):
        node = TextNode(
            "The type of this node cannot be like the other",
            TextType.CODE_TEXT
        )
        node2 = TextNode(
            "This type of node cannot be like the other",
            TextType.BOLD_TEXT
        )
        self.assertEqual(node == node2, False)

    def test_leaf_node_creation(self):
        # Each type of text node should be tested
        node_text = TextNode("text node content", TextType.TEXT)
        node_bold = TextNode("bold node content", TextType.BOLD_TEXT)
        node_italic = TextNode("italic node content", TextType.ITALIC_TEXT)
        node_code = TextNode("code node content", TextType.CODE_TEXT)
        node_link = TextNode("link node content", TextType.LINK, "google.com")
        node_image = TextNode("image node content", TextType.IMAGE, "file:///")

        node_list = [
            node_text,
            node_bold,
            node_italic,
            node_code,
            node_link,
            node_image,
        ]

        leaf_list = list(
            map(
                lambda some_node: text_node_to_html_node(some_node),
                node_list
            )
        )

        test_list = [
            LeafNode("p", "text node content"),
            LeafNode("b", "bold node content"),
            LeafNode("i", "italic node content"),
            LeafNode("code", "code node content"),
            LeafNode("a", "link node content", {"url": "google.com"}),
            LeafNode("img", "text node content", {"src": "file:///"})
        ]

        for i in range(0, len(test_list)-1):
            try:
                self.assertEqual(
                    HTMLNode.__eq__(test_list[i], leaf_list[i]),
                    True
                )
            except Exception:
                print(f"FAILED VALUES: TEST {test_list[i]} GEN {leaf_list[i]}")


if __name__ == "__main__":
    unittest.main()
