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

    def test_extract_markdown(self):
        test_text = "Hello my name is bob and this is me![bob](file:///)"
        self.assertEqual(
            extract_markdown_images(test_text),
            [("bob", "file:///")]
        )

    def test_extract_markdown(self):
        test_text = "my website is [bob](https://www.google.com)"
        # debugging
        # print(extract_markdown_links(test_text))
        self.assertEqual(
            extract_markdown_links(test_text),
            [("bob", "https://www.google.com")]
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        list_of_old_nodes = [node]

        new_nodes = split_nodes_link(list_of_old_nodes)
        # debugging
        # print(new_nodes)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            TextType.TEXT,
        )
        list_of_old_nodes = [node]

        new_nodes = split_nodes_image(list_of_old_nodes)
        # debugging
        # print(f"output: {new_nodes}")

    def test_text_to_textnodes(self):
        test_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test_output = text_to_textnodes(test_string)

        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        for index, item in enumerate(expected_output):
            self.assertTrue(
                item == test_output[index]
            )

if __name__ == "main":
    unittest.main()
