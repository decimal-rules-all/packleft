class DimensionedObject(object):
    """Abstract class for all three dimension object
    """
    def __init__(self, length: int, width: int, height: int) -> None:
        # Validate the dimension
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimension should not be negative.")
        # Set the dimension
        self.length: int = length
        self.width: int = width
        self.height: int = height
        # Calculate the volume
        self.volume: int = length * width * height


class Item(DimensionedObject):
    """Class for an item to pack
    """
    def __init__(self, length: int, width: int, height: int, weight: int=0) -> None:
        super().__init__(length, width, height)

        # Validate the weight
        if weight < 0:
            raise ValueError("Weight should not be negative.")
        self.weight = weight


class Box(DimensionedObject):
    """Class for a box as a container to pack items in it
    """
    def __init__(self, length: int, width: int, height: int, max_weight: int) -> None:
        super().__init__(length, width, height)

        # Validate the max weight
        if max_weight < 0:
            raise ValueError("Max weight should not be negative.")
        self.max_weight = max_weight
