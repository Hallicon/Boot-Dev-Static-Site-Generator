import htmlnode


class ParentNode(htmlnode.HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag on ParentNode object")
        elif self.children is None:
            raise ValueError("No children attached to ParentNode")

        """
        A parent node should have children,
        so if we recurse a parent node we should be
        able to get all of its children through recursion
        """

        # First let's create a list of string objects
        built_html = []

        # Then the parent will have its own tag added in first
        built_html.append(f"<{self.tag}")

        # Before closing the tag we need to handle the properties
        if self.props is not None:
            properties = super().props_to_html()
            built_html.append(f" {properties}")
        built_html.append(f">")

        # Then the function should iterate through the children
        for child in self.children:
            # If child is a parent node it will recurse
            string = child.to_html()
            built_html.append(string)

        # Then the closing tag should be added in
        built_html.append(f"</{self.tag}>")

        # Finally a string joining all of them should be returned
        return "".join(built_html)
