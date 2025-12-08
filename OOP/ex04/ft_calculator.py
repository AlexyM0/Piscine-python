class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.
        """
        dot_product = 0.0
        for x, y in zip(V1, V2):
            dot_product += x * y
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise and print the result vector.
        """

        result = []
        for x, y in zip(V1, V2):
            somme = x + y
            result.append(somme)

        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors element-wise and print the result vector.
        """

        result = []
        for x, y in zip(V1, V2):
            diff = x - y
            result.append(diff)

        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")
