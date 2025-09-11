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


def _split_node_image(old_node: TextNode) -> Iterable[TextNode]:
    if old_node.text_type is TextType.TEXT:
        original_text = old_node.text
        matches = extract_markdown_images(original_text)
        text_sections = []
        for image_alt, image_src in matches:
            sections = original_text.split(f"![{image_alt}]({image_src})", 1)
            text_sections.append(sections[0])
            original_text = sections[1]
        result = chain.from_iterable(
            [TextNode(text, TextType.TEXT), TextNode(text=match[0], text_type=TextType.IMAGE, url=match[1])]
            for text, match in zip(text_sections, matches)
        )
        if original_text:
            result = list(result)
            result.append(TextNode(text=original_text, text_type=TextType.TEXT))
        return result
    else:
        return [old_node]

def split_nodes_image(old_nodes):
    new_nodes = chain.from_iterable(
        _split_node_image(old_node)
        for old_node in old_nodes
    )

    return list(new_nodes)


def _split_node_link(old_node: TextNode) -> Iterable[TextNode]:
    if old_node.text_type is TextType.TEXT:
        original_text = old_node.text
        matches = extract_markdown_links(original_text)
        text_sections = []
        for link_text, link_href in matches:
            sections = original_text.split(f"[{link_text}]({link_href})", 1)
            text_sections.append(sections[0])
            original_text = sections[1]
        result = chain.from_iterable(
            [TextNode(text, TextType.TEXT), TextNode(text=match[0], text_type=TextType.LINK, url=match[1])]
            for text, match in zip(text_sections, matches)
        )
        if original_text:
            result = list(result)
            result.append(TextNode(text=original_text, text_type=TextType.TEXT))
        return result
    else:
        return [old_node]


def split_nodes_link(old_nodes):
    new_nodes = chain.from_iterable(
        _split_node_link(old_node)
        for old_node in old_nodes
    )

    return list(new_nodes)


def text_to_textnodes(text: str) -> list[TextNode]:
    text_nodes = [TextNode(text, text_type=TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes
