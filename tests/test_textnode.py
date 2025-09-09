import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "http://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "http://example2.com")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(text='This is a text node', text_type=<TextType.BOLD: 'bold'>, url=None)")

    def test_repr_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        self.assertEqual(repr(node), "TextNode(text='This is a link', text_type=<TextType.LINK: 'link'>, url='http://example.com')")

    def test_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_to_html_node_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = node.to_html_node()
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_to_html_node_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = node.to_html_node()
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        html_node = node.to_html_node()
        self.assertEqual(html_node.to_html(), '<a href="http://example.com">This is a link node</a>')

    def test_to_html_node_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "http://example.com/pic.png")
        html_node = node.to_html_node()
        html_node = node.to_html_node()
        self.assertEqual(html_node.to_html(), '<img src="http://example.com/pic.png" alt="This is an image node"></img>')

    def test_to_html_node_unknown(self):
        node = TextNode("This is an unknown node", None)
        self.assertRaises(ValueError, node.to_html_node)

if __name__ == "__main__":
    unittest.main()
