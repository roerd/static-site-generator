import re
from enum import Enum
from turtledemo.sorting_animate import Block


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    if re.match(r"#{1,6} ", block):
        return BlockType.HEADING
    elif re.fullmatch(r"```(.|\n)*```", block):
        return BlockType.CODE
    elif all(re.match(r">", line) for line in block.splitlines()):
        return BlockType.QUOTE
    elif all(re.match(r"- ", line) for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    elif all(re.match(r"\d+. ", line) for line in block.splitlines()):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
