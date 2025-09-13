import re

from block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = [text_node.to_html_node() for text_node in text_nodes]
    return children


def block_to_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            lines = block.splitlines()
            text = " ".join(lines)
            children = text_to_children(text)
            return ParentNode(tag="p", children=children)
        case BlockType.HEADING:
            matches = re.match(r"(#+) (.*)", block)
            level = len(matches[1])
            text = matches[2]
            children = text_to_children(text)
            return ParentNode(tag=f"h{level}", children=children)
        case BlockType.CODE:
            matches = re.match(r"```((.|\n)*)```", block)
            text = matches[1].lstrip()
            text_node = TextNode(text=text, text_type=TextType.TEXT)
            html_node = text_node.to_html_node()
            child = ParentNode(tag="code", children=[html_node])
            return ParentNode(tag="pre", children=[child])
        case BlockType.QUOTE:
            lines = block.splitlines()
            text = " ".join(line[1:].strip() for line in lines)
            children = text_to_children(text)
            return ParentNode(tag="blockquote", children=children)
        case BlockType.UNORDERED_LIST:
            lines = block.splitlines()
            line_texts = [line[2:] for line in lines]
            line_children = [text_to_children(text) for text in line_texts]
            list_items = [
                ParentNode(tag="li", children=li_children)
                for li_children in line_children
            ]
            return ParentNode(tag="ul", children=list_items)
        case BlockType.ORDERED_LIST:
            lines = block.splitlines()
            line_texts = [re.sub(r"\d+. ", "", line) for line in lines]
            line_children = [text_to_children(text) for text in line_texts]
            list_items = [
                ParentNode(tag="li", children=li_children)
                for li_children in line_children
            ]
            return ParentNode(tag="ol", children=list_items)



def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = [block_to_node(block) for block in blocks]
    return ParentNode(tag="div", children=nodes)
