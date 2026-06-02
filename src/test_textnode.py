import unittest
from textnode import TextNode, TextType


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
        node = TextNode("The type of this node cannot be like the other", TextType.CODE_TEXT)
        node2 = TextNode("This type of node cannot be like the other", TextType.BOLD_TEXT)
        self.assertEqual(node == node2, False)


if __name__ == "__main__":
    unittest.main()
