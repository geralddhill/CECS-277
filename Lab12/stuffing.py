from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):
    """ Decorator that adds stuffing to the plate.

    Attributes:
        _plate: :class:`Plate` attribute to represent a plate with food on it.
    """

    def description(self) -> str:
        """ Adds stuffing to the description of the plate.

        :return: A string description of the plate and what is on it, plus stuffing.
        """
        desc = super().description()

        if self.count() > 1:
            desc += " and "

        return desc + "Stuffing"

    def area(self) -> int:
        """ Removes the area of the stuffing from the area left of the plate.

        :return: The remaining square inches the plate can hold minus the area of the stuffing.
        """
        return super().area() - 18

    def weight(self) -> int:
        """ Removes the weight of the stuffing from the plate.

        :return: The remaining number of ounces the plate can hold minus the area of the stuffing.
        """
        return super().weight() - 7

    def count(self) -> int:
        """ Adds one to the number of food items on the plate.

        :return: The number of food items the plate is currently holding plus one."""
        return super().count() + 1