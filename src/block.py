"""
    The purpose of this module is to process block elements.
    Every function in here serves to process blocks into a
    workable object.
"""

from enum import Enum
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
        case b if re.match(r"^```.*```$", b) or re.match(r"^`.*`$", b):
            return BlockType.CODE
        case c if markdown[0] == ">":
            return BlockType.QUOTE
        case d if markdown[0:2] == "- ":
            return BlockType.UNORDERED_LIST
        case e if re.match(r"^\d+\.", e):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
