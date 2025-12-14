def median(lst) -> any:
    """Return the median value of a list of numbers
    (middle value, or average of two middles)."""
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2

    if n % 2 == 1:
        return lst[mid]
    else:
        return (lst[mid - 1] + lst[mid]) / 2


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print statistics (mean, median, quartile, std, var)
    based on keyword requests in kwargs."""
    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            print(sum(args) / len(args))
        elif value == "median":
            print(median(args))
        elif value == "quartile":
            data = sorted(args)
            n = len(data)
            mid = n // 2
            if n % 2 == 0:
                lower = data[:mid]
                upper = data[mid:]
            else:
                lower = data[:mid+1]
                upper = data[mid:]
            result_quart = [float(median(lower)), float(median(upper))]
            print(result_quart)
        elif value == "std":
            m = sum(args) / len(args)
            variance = sum((x - m) ** 2 for x in args) / len(args)
            print(variance ** 0.5)
        elif value == "var":
            m = sum(args) / len(args)
            print(sum((x - m) ** 2 for x in args) / len(args))
