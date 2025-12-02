def ft_filter(function, iterable):
    """
    Return a list of items from `iterable` for which `function` is True.

    If `function` is None, keep all truthy items.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def is_even(n):
    return n % 2 == 0


def main():
    """
    Example placeholder for testing `ft_filter`.
    """
    print(ft_filter(is_even, [1, 2, 3, 4]))
    pass


if __name__ == "__main__":
    main()
