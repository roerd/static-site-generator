from dataclasses import dataclass


@dataclass
class HTMLNode:
    tag: str = None
    value: str = None
    children: list["HTMLNode"] = None
    props: dict[str, str] = None

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        str_props = [f'{k}="{v}"' for k, v in self.props.items()]
        return " ".join(str_props)
