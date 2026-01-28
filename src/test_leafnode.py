import unittest

from leafNode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag(self):
        node = LeafNode(tag="p", value="test")
        p = "p"
        self.assertEqual(node.tag, p)

    def test_props(self):
        node = LeafNode(
            tag="a",
            value="Click Me",
            props={"href": "www.test.com", "alt": "click this"},
        )
        props = ' href="www.test.com" alt="click this"'
        node2 = LeafNode(None, None, None)
        self.assertEqual(node.props_to_html(), props)
        self.assertEqual(node2.props_to_html(), "")

    def test_none(self):
        node = LeafNode(None, None, None)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = LeafNode(
            tag="a",
            value="Click Me",
            props={"href": "www.test.com", "alt": "click this"},
        )
        self.assertEqual(
            node.to_html(), '<a href="www.test.com" alt="click this">Click Me</a>'
        )
        node2 = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node2.to_html()
        node3 = LeafNode(None, "this is value")
        self.assertEqual(node3.to_html(), node3.value)


if __name__ == "__main__":
    unittest.main()
