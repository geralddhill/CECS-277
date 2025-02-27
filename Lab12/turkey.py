from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
    """ Decorator that adds turkey to the plate.

    Attributes:
        _plate: :class:`Plate` attribute to represent a plate with food on it.
    """

    def description(self) -> str:
        """ Adds a turkey to the description of the plate.

        :return: A string description of the plate and what is on it, plus a turkey.
        """
        desc = super().description()

        if self.count() > 1:
            desc += " and "

        return desc + "Turkey"

    def area(self) -> int:
        """ Removes the area of the turkey from the area left of the plate.

        :return: The remaining square inches the plate can hold minus the area of the turkey.
        """
        return super().area() - 15

    def weight(self) -> int:
        """ Removes the weight of the turkey from the plate.

        :return: The remaining number of ounces the plate can hold minus the area of the turkey.
        """
        return super().weight() - 4

    def count(self) -> int:
        """ Adds one to the number of food items on the plate.

        :return: The number of food items the plate is currently holding plus one."""
        return super().count() + 1