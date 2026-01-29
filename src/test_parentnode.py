import unittest

from parent_node import ParentNode
from leafNode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        leaf_node = LeafNode(
            tag="a",
            value="Click Me",
            props={"href": "www.test.com", "alt": "click this"},
        )
        node = ParentNode(
            tag="p",
            children=[leaf_node],
        )
        p = "p"
        self.assertEqual(node.tag, p)

    def test_props(self):
        leaf_node = LeafNode(
            tag="a",
            value="Click Me",
            props={"href": "www.test.com", "alt": "click this"},
        )
        node = ParentNode(
            tag="div",
            children=[leaf_node],
            props={"href": "www.test.com", "alt": "click this"},
        )
        props = ' href="www.test.com" alt="click this"'
        node2 = ParentNode(tag="div", children=[leaf_node], props=None)
        self.assertEqual(node.props_to_html(), props)
        self.assertEqual(node2.props_to_html(), "")

    def test_none(self):
        with self.assertRaises(ValueError):
            ParentNode(None, None, None).to_html()
        with self.assertRaises(ValueError):
            ParentNode("tag", None).to_html()
        with self.assertRaises(ValueError):
            ParentNode(None, "tag").to_html()


def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )


if __name__ == "__main__":
    unittest.main()
