def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice `family` from row index `start` to `end` and print shapes before/after.
    """
    assert type(family) is list, "family must be a list"
    for row in family:
        assert type(row) is list, "family must be a list of lists"
        for c in row:
            assert type(c) in (int, float), "bad type(s)"
    if len(family) > 0:
        first_len = len(family[0])
        for row in family:
            assert len(row) == first_len, "each row must be of the same size"
    rows = len(family)
    cols = len(family[0])
    print(f"My shape is : ({rows}, {cols})")
    new_family = family[start:end]
    rows = len(new_family)
    cols = len(new_family[0])
    print(f"My new shape is : ({rows}, {cols})")
    return new_family


def main():
    """
    Placeholder for testing `slice_me`.
    """
    pass


if __name__ == "__main__":
    main()
