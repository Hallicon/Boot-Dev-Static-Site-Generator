from textnode import *
import re




"""
    The purpose of this function is to take in a list of TextNodes
    that have their TextType member set to TextType.TEXT. The
    delimiter is used to tell where each new TextNode is to be
    created.
"""


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType) -> list[TextNode]:
    """
        For each TextNode, we want to split the text in the node
        by the delimiter, then from the generated list, we want
        to take each element and form a TextNode from it.
        Knowing that the delimiter starts at the center of the 
        text parts allows us to use the [1]th element of the split
        text.
    """
    output_nodes = []

    for node in old_nodes:
        split_node_text = str.split(node.text, delimiter)
        for index, text_part in enumerate(split_node_text):
            if index == 1:
                output_nodes.append(
                    TextNode(
                        text_part,
                        text_type=text_type
                    )
                )
            else:
                output_nodes.append(
                    TextNode(
                        text_part,
                        text_type=TextType.TEXT
                    )
                )

    return output_nodes


"""
    The following two functions are meant to extract links to both
    images as well as links to websites that are being marked down.
    They both take strings as inputs
"""


def extract_markdown_images(text: str):
    extract = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return extract


def extract_markdown_links(text: str):
    extract = re.findall(r"\[(.*?)\]\((https:\/\/.*?)\)", text)
    return extract
