import unittest
from inline import *
from textnode import *


class TestInline(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        list_of_old_test_nodes = [
            TextNode("This is a **bold** node", TextType.TEXT),
            TextNode("This is an _italic_ node", TextType.TEXT)
        ]

        test_output = split_nodes_delimiter(
            list_of_old_test_nodes,
            "**",
            TextType.BOLD_TEXT
        )

        test_expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" node", TextType.TEXT),
            TextNode("This is an _italic_ node", TextType.TEXT)
        ]

        iter = 0
        while iter != len(test_expected):
            self.assertTrue(test_expected[iter] == test_output[iter])
            iter += 1


if __name__ == "main":
    unittest.main()
