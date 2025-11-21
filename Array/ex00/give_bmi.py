def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
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
    result: list[bool] = []
    for b in bmi:
        assert type(b) in (int, float), "Bad type(s)"
        result.append(b >= limit)
    return result


def main():
    pass


if __name__ == "__main__":
    main()
