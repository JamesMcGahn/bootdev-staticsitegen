from htmlnode import HTMLNode
from leafNode import LeafNode


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("need tag")
        if self.children is None:
            raise ValueError("need children")

        else:
            child_str = ""
            for child in self.children:
                child_str += child.props_to_html()
            props = self.props_to_html()
            return f"<{self.tag}{props}>{child_str}</{self.tag}>"

    def __repr__(self):
        print(f"{self.tag} {self.props_to_html()}")
