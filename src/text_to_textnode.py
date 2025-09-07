import re
from itertools import chain, cycle
from typing import Iterable

from textnode import TextType, TextNode


def _split_node_delimiter(old_node: TextNode, delimiter: str, new_text_type: TextType) -> Iterable[TextNode]:
    if old_node.text_type is TextType.TEXT:
        texts = old_node.text.split(delimiter)
        return (
            TextNode(text, text_type)
            for text, text_type in zip(texts, cycle([TextType.TEXT, new_text_type]))
            if text
        )
    else:
        return [old_node]


def split_nodes_delimiter(old_nodes: Iterable[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = chain.from_iterable(
        _split_node_delimiter(old_node, delimiter, text_type)
        for old_node in old_nodes
    )

    return list(new_nodes)


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)]\((.*?)\)", text)
    return matches
