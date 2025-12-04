def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice `family` from row index `start` to
    `end` and print shapes before/after.
    """
    try:
        if type(family) is not list:
            raise AssertionError("family must be a list")
        for row in family:
            if type(row) is not list:
                raise AssertionError("family must be a list of lists")
            for c in row:
                if not type(c) in (int, float):
                    raise AssertionError("bad types")
        if len(family) > 0:
            first_len = len(family[0])
            for row in family:
                if len(row) != first_len:
                    raise AssertionError("each row must be of the same size")
        rows = len(family)
        cols = len(family[0])
        print(f"My shape is : ({rows}, {cols})")
        new_family = family[start:end]
        rows = len(new_family)
        cols = len(new_family[0])
        print(f"My new shape is : ({rows}, {cols})")
        return new_family
    except AssertionError as error:
        print("AssertionError: ", error)
        return None


def main():
    """
    Placeholder for testing `slice_me`.
    """
    pass


if __name__ == "__main__":
    main()
