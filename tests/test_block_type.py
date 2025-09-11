import unittest

from block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        bt = block_to_block_type("# Title")
        self.assertEqual(bt.value, "heading")

    def test_heading2(self):
        bt = block_to_block_type("## Subtitle")
        self.assertEqual(bt.value, "heading")

    def test_heading6(self):
        bt = block_to_block_type("###### Paragraph title")
        self.assertEqual(bt.value, "heading")

    def test_code(self):
        bt = block_to_block_type("```python```")
        self.assertEqual(bt.value, "code")

    def test_code_multiline(self):
        bt = block_to_block_type("""```
This is text that _should_ remain
the **same** even with inline stuff
```""")
        self.assertEqual(bt.value, "code")

    def test_quote(self):
        bt = block_to_block_type("> This is a quote")
        self.assertEqual(bt.value, "quote")

    def test_unordered_list(self):
        bt = block_to_block_type("- a\n- b\n- c")
        self.assertEqual(bt.value, "unordered_list")

    def test_ordered_list(self):
        bt = block_to_block_type("1. a\n2. b\n3. c")
        self.assertEqual(bt.value, "ordered_list")

    def test_paragraph(self):
        bt = block_to_block_type("This is just some text.")
        self.assertEqual(bt.value, "paragraph")


if __name__ == '__main__':
    unittest.main()
