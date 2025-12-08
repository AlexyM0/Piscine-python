class calculator:
    """
    calculator class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar
    """
    def __init__(self, vector):
        """
        Initializes the calculator with the provided vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
            The resulting vector after addition.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """
            The resulting vector after multiplication.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        """
            The resulting vector after subtraction.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        """
            The resulting vector after division.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
