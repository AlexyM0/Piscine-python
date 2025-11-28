def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Return the list of BMI values computed from `height` and `weight`.
    """
    assert type(height) is list, "height must be a list"
    assert type(weight) is list, "weight must be a list"
    assert len(height) == len(weight), "Bad arguments"

    result: list[int | float] = []
    for h, w in zip(height, weight):
        assert type(h) in (int, float) and type(w) in (int, float), (
            "Bad type(s)"
        )
        bmi = w / (h**2)
        result.append(bmi)
    return result


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """
    Return a list of booleans indicating if each BMI is >= `limit`.
    """
    result: list[bool] = []
    for b in bmi:
        assert type(b) in (int, float), "Bad type(s)"
        result.append(b >= limit)
    return result


def main():
    """
    Placeholder for testing `give_bmi` and `apply_limit`.
    """
    pass


if __name__ == "__main__":
    main()
