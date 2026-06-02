import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    new_node = HTMLNode(
            "<p>",
            "This is a pragraph node",
            ["child1", "child2"],
            {"lang": "en", "id": 1}
        )

    def test_initializer(self):
        print(self.new_node)

    def test_convert_attributes(self):
        attrib_list = self.new_node.props_to_html()
        print(f"attrib_list test: {attrib_list}")
        self.assertEqual(attrib_list, [f"lang=\"en\"", f"id=\"1\""])
