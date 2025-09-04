from dataclasses import dataclass


@dataclass
class HTMLNode:
    tag: str | None = None
    value: str | None = None
    children: list["HTMLNode"] | None = None
    props: dict[str, str] | None = None

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        str_props = [f'{k}="{v}"' for k, v in self.props.items()]
        return " ".join(str_props)

    def _tag_str(self):
        tag_str = [self.tag]
        props_str = self.props_to_html()
        if props_str:
            tag_str.append(props_str)
        return " ".join(tag_str)



class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")

        if not self.tag:
            return self.value

        tag_str = self._tag_str()
        return f"<{tag_str}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")

        if not self.children:
            raise ValueError("All parent nodes must have children.")

        tag_str = self._tag_str()
        inner_str = "".join(child.to_html() for child in self.children)
        return f"<{tag_str}>{inner_str}</{self.tag}>"
