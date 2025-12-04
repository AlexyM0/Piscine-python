def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Return the list of BMI values computed from `height` and `weight`.
    """
    try:
        if type(height) is not list:
            raise AssertionError("height must be a list")
        if type(weight) is not list:
            raise AssertionError("weight must be a list")
        if len(height) != len(weight):
            raise AssertionError("Bad arguments")
    except AssertionError as error:
        print("AssertionError: ", error)
        return []
    result: list[int | float] = []
    try:
        for h, w in zip(height, weight):
            if not (type(h) in (int, float) and type(w) in (int, float)):
                raise AssertionError("Bad type(s)")
            bmi = w / (h**2)
            result.append(bmi)
    except AssertionError as error:
        print("AssertionError: ", error)
        return []
    return result


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """
    Return a list of booleans indicating if each BMI is >= `limit`.
    """
    try:
        if not isinstance(bmi, list):
            raise AssertionError("must be a list")
        result: list[bool] = []
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise AssertionError(
                    "Bad type(s)"
                )
            result.append(b > limit)
        return result

    except AssertionError as error:
        print("AssertionError: ", error)
        return []
