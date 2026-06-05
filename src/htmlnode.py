class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children    # this is a list
        self.props = props          # properties/attributes (dict)

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return f""

        # Create a list from the attributes
        converted_attributes: list[str] = list(
                map(
                    lambda key: f"{key}=\"{self.props[key]}\"",
                    self.props
                )
            )

        # Return attributes as a joined list
        return " ".join(converted_attributes)

    def __repr__(self):
        return (
            f"{id(self)} HTMLNode object tag = {self.tag}\n"
            f"{id(self)} HTMLNode object value = {self.value}\n"
            f"{id(self)} HTMLNode object children = {self.children}\n"
            f"{id(self)} HTMLNode object props = {self.props}\n"
        )

    # Method to compare if two nodes are equal (not comparing children)
    def __eq__(self, other: HTMLNode) -> bool:
        if (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        ):
            return True
        else:
            return False
