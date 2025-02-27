from abc import ABC
from plate import Plate

class PlateDecorator(Plate, ABC):
    """ Abstract base class for a decorator that adds food to a plate and changes the plate's properties as food is added.

    Attributes:
        _plate: :class:`Plate` attribute to represent a plate with food on it.
    """

    def __init__(self, p: Plate) -> None:
        """Constructor for :class:`PlateDecorator`.

        :param p: :class:`Plate` attribute to represent the previous state of the plate.
        """
        self._plate = p

    def description(self) -> str:
        """:return: A string description of the plate and what is on it."""
        return self._plate.description()

    def area(self) -> int:
        """:return: The remaining square inches the plate can hold."""
        return self._plate.area()

    def weight(self) -> int:
        """:return: The remaining number of ounces the plate can hold."""
        return self._plate.weight()

    def count(self) -> int:
        """:return: The number of food items the plate is currently holding."""
        return self._plate.count()