import re


def extract_title(markdown: str) -> str:
    matches = re.search(r"^# (.*)$", markdown, re.MULTILINE)
    if not matches:
        raise ValueError(f"Could not extract title from markdown")
    return matches[1]
