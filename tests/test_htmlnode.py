import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!", props={"class": "phrase"})
        self.assertEqual(node.to_html(), '<span class="phrase">Hello, world!</span>')


class TestParentNode(unittest.TestCase):
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        node = ParentNode("", [LeafNode("p", "Hello, world!")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("div", [])
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()
