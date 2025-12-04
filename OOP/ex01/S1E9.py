from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Character.

        Parameters:
        first_name : The first name of the character.
        is_alive : The health state of the character.
        Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the health state of the character
        """
        pass


class Stark(Character):
    """Class representing a Stark character."""
    def __init__(self, first_name, is_alive=True):
        """
        Stark character has been created
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        This method overrides the abstract method from the base class and
        updates the is_alive attribute to False.
        """
        self.is_alive = False
