import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>"I am in fact a Hobbit in all but size."  -- J.R.R. Tolkien</blockquote></div>',
        )

    def test_unordered_list(self):
        md = """
- **bold**
- _italic_
- `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li><b>bold</b></li><li><i>italic</i></li><li><code>code</code></li></ul></div>",
        )


if __name__ == '__main__':
    unittest.main()
