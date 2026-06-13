import htmlnode


class LeafNode(htmlnode.HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_string_list = super().props_to_html()
            return (
                f"<{self.tag} "
                f"{props_string_list}>"
                f"{self.value}</{self.tag}>"
            )

    def __repr__(self):
        return (
            f"{id(self)} LeafNode object tag = {self.tag}\n"
            f"{id(self)} LeafNode object value = {self.value}\n"
            f"{id(self)} LeafNode object props = {self.props}\n"
        )