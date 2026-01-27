class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        str_ = ""
        if self.props is None:
            return ""
        for key in self.props.keys():
            str_ += f' {key}="{self.props[key]}"'

        return str_

    def __repr__(self):
        print(f"{self.tag} {self.value} {self.children} {self.props_to_html()}")
