from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):
    """ Decorator that adds potatoes to the plate.

    Attributes:
        _plate: :class:`Plate` attribute to represent a plate with food on it.
    """

    def description(self) -> str:
        """ Adds potatoes to the description of the plate.

        :return: A string description of the plate and what is on it, plus potatoes.
        """
        desc = super().description()

        if self.count() > 1:
            desc += " and "

        return desc + "Potatoes"

    def area(self) -> int:
        """ Removes the area of the potatoes from the area left of the plate.

        :return: The remaining square inches the plate can hold minus the area of the potatoes.
        """
        return super().area() - 18

    def weight(self) -> int:
        """ Removes the weight of the potatoes from the plate.

        :return: The remaining number of ounces the plate can hold minus the area of the potatoes.
        """
        return super().weight() - 6

    def count(self) -> int:
        """ Adds one to the number of food items on the plate.

        :return: The number of food items the plate is currently holding plus one."""
        return super().count() + 1