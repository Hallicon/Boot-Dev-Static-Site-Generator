import unittest
from block import *


class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING)
        self.assertEqual(block_to_block_type(
            "`print('hello')`"),
            BlockType.CODE)
        self.assertEqual(
            block_to_block_type("> Quote"),
            BlockType.QUOTE)
        self.assertEqual(
            block_to_block_type("- Item"),
            BlockType.UNORDERED_LIST)
        self.assertEqual(
            block_to_block_type("1. Item"),
            BlockType.ORDERED_LIST)
        self.assertEqual(
            block_to_block_type("Just a paragraph"),
            BlockType.PARAGRAPH)


if __name__ == "main":
    unittest.main()
