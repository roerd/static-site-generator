from os import PathLike
from pathlib import Path

from generate_page import generate_page


def generate_pages_recursive(
        dir_path_content: str | PathLike,
        template_path: str | PathLike,
        dest_dir_path: str | PathLike,
        basepath: str
) -> None:
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)

    for dir_path, _, file_names in dir_path_content.walk():
        relative_path = dir_path.relative_to(dir_path_content)
        for file_name in file_names:
            src_path = dir_path / file_name
            if src_path.suffix == ".md":
                dest_path = dest_dir_path / relative_path / (src_path.stem + ".html")
                generate_page(src_path, template_path, dest_path, basepath)
