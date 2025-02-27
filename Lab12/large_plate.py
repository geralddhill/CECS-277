from plate import Plate

class LargePlate(Plate):
    """Represents a flimsier 12-inch paper plate."""

    def description(self) -> str:
        """:return: The description of the plate."""
        return "Flimsy 12 inch paper plate with\n"

    def area(self) -> int:
        """:return: The area of the plate."""
        return 113

    def weight(self) -> int:
        """:return: The weight capacity of the plate."""
        return 24

    def count(self) -> int:
        """:return: Zero (the plate starts with nothing on it)."""
        return 0
