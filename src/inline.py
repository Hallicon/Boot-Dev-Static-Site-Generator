from textnode import *
import re

"""
    TO DO:
    [ ] Need to turn split nodes into higher order variants
    [ ] Need to cover grounds when missing pieces
        or bad things are input in split nodes
"""

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
        if node.text_type == TextType.TEXT:
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
        else:
            output_nodes.append(node)
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


"""
    The following functions are meant to split nodes with text that
    have links in them into individual TextNodes with appropriate
    TextTypes corresponding parts of the text member of each node.
    An example of how this is supposed to work is as follows:

    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])

    Should result in:

    [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
            "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
        ),
    ]
"""


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    output_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text_split = re.split(
                r"!\[(.*?)\]\((.*?)\)",
                node.text
            )

            """
                The individual parts are always going to follow an order
                first text, then name of link, then the link itself, to
                cycle through this a modulus can be used.
            """
            for index in range(0, len(text_split)):
                mod = index % 3
                match(mod):
                    case 0:
                        output_nodes.append(
                            TextNode(
                                text_split[index],
                                TextType.TEXT
                            )
                        )
                    case 1:
                        output_nodes.append(
                            TextNode(
                                text_split[index],      # Name of Image
                                TextType.IMAGE,
                                text_split[index + 1]   # Path to Image
                            )
                        )
                    case 2:
                        pass
        else:
            output_nodes.append(node)
    return output_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    output_nodes = []
    for node in old_nodes:
        """
            The individual parts are always going to follow an order
            first text, then name of link, then the link itself, to
            cycle through this a modulus can be used.
        """

        if node.text_type == TextType.TEXT:
            text_split = re.split(
                r"\[(.*?)\]\((https:\/\/.*?)\)",
                node.text
            )
            for index in range(0, len(text_split)):
                mod = index % 3
                match(mod):
                    case 0:
                        output_nodes.append(
                            TextNode(
                                text_split[index],
                                TextType.TEXT
                            )
                        )
                    case 1:
                        output_nodes.append(
                            TextNode(
                                text_split[index],      # Name of link
                                TextType.LINK,
                                text_split[index + 1]   # URL
                            )
                        )
                    case 2:
                        pass
        else:
            # push the old node onto the stack
            output_nodes.append(node)

    return output_nodes


"""
    The purpose of this function is to take a long piece of text
    with markdown and convert it into a list of TextNodes.
"""


def text_to_textnodes(text) -> list[TextNode]:
    # First we make a TextNode out of the text
    main_list = [TextNode(text, TextType.TEXT)]

    # Split by images
    image_main_list = split_nodes_image(main_list)

    # Split by links
    link_main_list = split_nodes_link(image_main_list)

    """
        By this point link_main_list will have all the "link" parts split
        the next task is to get the delimiters settled.
    """

    # Split by code
    code_main_list = split_nodes_delimiter(
        link_main_list,
        "`",
        TextType.CODE_TEXT)

    # Split by bold
    bold_main_list = split_nodes_delimiter(
        code_main_list,
        "**",
        TextType.BOLD_TEXT)

    # Split by italic
    italic_main_list = split_nodes_delimiter(
        bold_main_list,
        "_",
        TextType.ITALIC_TEXT)


    return italic_main_list
