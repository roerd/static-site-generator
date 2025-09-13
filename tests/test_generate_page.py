import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        md = """
# This is the header
And this is some text."""
        title = extract_title(md)
        self.assertEqual(title, "This is the header")

    def test_extract_title_2(self):
        md = """A line before the title
# This is the header
And this is some text."""
        title = extract_title(md)
        self.assertEqual(title, "This is the header")

    def test_extract_title_error(self):
        md = """
This is just some text.

And another such line."""
        self.assertRaises(ValueError, extract_title, md)


if __name__ == '__main__':
    unittest.main()
