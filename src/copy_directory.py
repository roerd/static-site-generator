from os import PathLike
from pathlib import Path


def clean_directory(dst: Path):
    if not dst.is_dir():
        raise NotADirectoryError(dst)

    print(f"Cleaning {dst}")

    for dirpath, _, filenames in dst.walk(top_down=False):
        for filename in filenames:
            (dirpath / filename).unlink()
            if dirpath != dst:
                dirpath.rmdir()


def copy_directory(src: str | PathLike[str], dst: str | PathLike[str]) -> None:
    src = Path(src)
    dst = Path(dst)

    if not src.exists():
        raise FileNotFoundError(src)

    if dst.exists():
        clean_directory(dst)
    else:
        dst.mkdir()

    for child in src.iterdir():
        if child.is_dir():
            copy_directory(child, dst / child.name)
        else:
            print(f"Copying {child} to {dst / child.name}")
            content = child.read_bytes()
            (dst / child.name).write_bytes(content)
