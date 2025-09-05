from dataclasses import dataclass
from enum import Enum

from htmlnode import HTMLNode, LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


@dataclass
class TextNode:
    text: str
    text_type: TextType
    url: str | None = None

    def to_html_node(self) -> HTMLNode:
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=self.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=self.text)
            case TextType.LINK:
                return LeafNode(tag="a", value=self.text, props={"href": self.url})
            case TextType.IMAGE:
                return LeafNode(tag="img", value="", props={"src": self.url, "alt": self.text})
            case _:
                raise ValueError(f"Unknown text type: {self.text_type}")
