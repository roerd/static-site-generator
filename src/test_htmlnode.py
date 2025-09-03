import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag='p', value="This is a paragraph")
        node2 = HTMLNode(tag='p', value="This is a paragraph")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode(tag='p', value="This is a paragraph")
        node2 = HTMLNode(tag='p', value="This is a different paragraph")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag='p', value="This is a paragraph")
        self.assertEqual(repr(node), "HTMLNode(tag='p', value='This is a paragraph', children=None, props=None)")

if __name__ == "__main__":
    unittest.main()
