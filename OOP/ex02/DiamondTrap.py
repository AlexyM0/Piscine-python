from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The King"""

    def __init__(self, first_name, is_alive=True):
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """eye setter method"""
        self.eyes = color

    def set_hairs(self, color):
        """hairs setter method"""
        self.hairs = color

    def get_eyes(self):
        """eye getter method"""
        return self.eyes

    def get_hairs(self):
        """hairs getter method"""
        return self.hairs