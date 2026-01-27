import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="p", value="test", children=None, props=None)
        p = "p"
        self.assertEqual(node.tag, p)

    def test_props(self):
        node = HTMLNode(
            tag="p",
            value="test",
            children=None,
            props={"href": "hamster", "link": "cheetah"},
        )
        props = ' href="hamster" link="cheetah"'
        node2 = HTMLNode()
        self.assertEqual(node.props_to_html(), props)
        self.assertEqual(node2.props_to_html(), "")

    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == "__main__":
    unittest.main()
