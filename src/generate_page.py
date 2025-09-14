import re
from os import PathLike
from pathlib import Path

from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown: str) -> str:
    matches = re.search(r"^# (.*)$", markdown, re.MULTILINE)
    if not matches:
        raise ValueError(f"Could not extract title from markdown")
    return matches[1].strip()


def generate_page(
        from_path: str | PathLike,
        template_path: str | PathLike,
        dest_path: str | PathLike,
        basepath: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = Path(from_path).read_text()
    template = Path(template_path).read_text()

    html_node = markdown_to_html_node(markdown)
    html_str = html_node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_path = Path(dest_path)
    if not dest_path.parent.exists():
        dest_path.parent.mkdir(parents=True)
    dest_path.write_text(template)
