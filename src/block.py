"""
    The purpose of this module is to process block elements.
    Every function in here serves to process blocks into a
    workable object.
"""

from enum import Enum
import leafnode
import parentnode
import textnode
import inline
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    split_pieces = markdown.split("\n\n")
    split_pieces = list(map(lambda part: part.strip(), split_pieces))
    return split_pieces


def block_to_block_type(markdown):
    match(markdown):
        case a if re.match(r"#{1}", a):
            return BlockType.HEADING
        case b if re.match(r"^```.*```$", b, re.DOTALL) or re.match(r"^`.*`$", b):
            return BlockType.CODE
        case c if markdown[0] == ">":
            return BlockType.QUOTE
        case d if markdown[0:2] == "- ":
            return BlockType.UNORDERED_LIST
        case e if re.match(r"^\d+\.", e):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH


def make_list_of_html_nodes(block: str):
    """
        Suppose we have a case such as:
        "This is **bolded** paragraph"
        we need to split it with the
        text_to_text_nodes method from inline.py.
        then from that list of text nodes convert
        them to html.
    """

    list_of_text_nodes = inline.text_to_textnodes(block)

    list_of_html_nodes = list(
        # part is supposed to be a TextNode object
        map(
            lambda part: textnode.text_node_to_html_node(part),
            list_of_text_nodes
        )
    )
    return list_of_html_nodes


def markdown_to_html_node(markdown):
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    # We need to filter out any blocks that are empty strings
    blocks = list(
        filter(
            lambda block: block != "", blocks
        )
    )

    # Make a parent node to contain all the other parent nodes for each block
    the_node = parentnode.ParentNode(
        tag="div",
        children=[]
    )

    # For each block determine the type and then form the HTMLNode
    for block in blocks:
        type = block_to_block_type(block)

        match(type):
            case BlockType.PARAGRAPH:
                # Replace any newlines with " "
                block = block.replace("\n", " ")

                html_noded_blocks = make_list_of_html_nodes(block)

                """
                    Next we have to encase this in a paragraph node that
                    is a type of ParentNode.
                """
                the_node.children.append(
                    parentnode.ParentNode(
                        tag="p",
                        children=html_noded_blocks
                    )
                )

            case BlockType.HEADING:
                block = block.removeprefix("# ")
                html_noded_blocks = make_list_of_html_nodes(block)

                """
                    Next we have to encase this in a heading node that
                    is a type of ParentNode.
                """
                the_node.children.append(
                    parentnode.ParentNode(
                        tag="h1",
                        children=html_noded_blocks
                    )
                )

            case BlockType.CODE:

                block = block.removeprefix("```").removesuffix("```").lstrip("\n")
                the_node.children.append(
                    parentnode.ParentNode(
                        tag="pre",
                        children=[leafnode.LeafNode(
                            tag="code",
                            value=block
                        )]
                    )
                )

            case BlockType.QUOTE:
                block = block.removeprefix("> ")

                html_noded_blocks = make_list_of_html_nodes(block)

                """
                    next we have to encase this in a quote node that
                    is a type of ParentNode.
                """

                the_node.children.append(
                    parentnode.ParentNode(
                        tag="blockquote",
                        children=html_noded_blocks
                    )
                )

            case BlockType.UNORDERED_LIST:

                """
                    An entire list is treated as one whole block,
                    the first step is to split them by newlines to
                    get each member of the list, and then remove
                    the prefix from each list member.
                """

                split_block = block.split("\n")
                removed_prefix = list(
                    map(
                        lambda input_string: input_string.removeprefix("- "),
                        split_block
                    )
                )

                converted_nodes = []
                for item in removed_prefix:
                    converted_nodes.append(make_list_of_html_nodes(item))

                # Now take the converted nodes and set their tag to li
                li_nodes = []
                for item_children in converted_nodes:
                    li_nodes.append(parentnode.ParentNode(tag="li", children=item_children))

                the_node.children.append(
                    parentnode.ParentNode(tag="ul", children=li_nodes)
                )

            case BlockType.ORDERED_LIST:
                split_block = block.split("\n")
                removed_prefix = list(
                    map(
                        lambda input_string: input_string.split(". ", 1)[1],
                        split_block
                    )
                )

                converted_nodes = []
                for item in removed_prefix:
                    converted_nodes.append(make_list_of_html_nodes(item))

                # Now take the converted nodes and set their tag to li
                li_nodes = []
                for item_children in converted_nodes:
                    li_nodes.append(parentnode.ParentNode(tag="li", children=item_children))

                the_node.children.append(
                    parentnode.ParentNode(tag="ol", children=li_nodes)
                )

    return the_node



