import sys

from copy_directory import copy_directory
from generate_pages import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public", basepath)


if __name__ == "__main__":
    main()
