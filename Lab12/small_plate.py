from plate import Plate

class SmallPlate(Plate):
    """Represents a sturdier 10-inch paper plate."""

    def description(self) -> str:
        """:return: The description of the plate."""
        return "Sturdy 10 inch paper plate with\n"

    def area(self) -> int:
        """:return: The area of the plate."""
        return 78

    def weight(self) -> int:
        """:return: The weight capacity of the plate."""
        return 32

    def count(self) -> int:
        """:return: Zero (the plate starts with nothing on it)."""
        return 0
