from leafNode import LeafNode
from textnode import TextType, TextNode


def text_node_to_html_node(text_node: TextNode):
    tntype = text_node.text_type
    match tntype:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(
                "img", "", props={"href": text_node.url, "alt": text_node.text}
            )
