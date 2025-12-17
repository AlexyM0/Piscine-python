def median(lst) -> any:
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2

    if n % 2 == 1:
        return lst[mid]
    else:
        return (lst[mid - 1] + lst[mid]) / 2


def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        for key, value in kwargs.items():
            if len(args) == 0:
                print("ERROR")
            elif value == "mean":
                print("mean :", sum(args) / len(args))
            elif value == "median":
                print("median :", median(args))
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
                print("quartile :", result_quart)
            elif value == "std":
                m = sum(args) / len(args)
                variance = sum((x - m) ** 2 for x in args) / len(args)
                print("std :", variance ** 0.5)
            elif value == "var":
                m = sum(args) / len(args)
                print("var :", sum((x - m) ** 2 for x in args) / len(args))
    except (TypeError, ValueError, AssertionError):
        print("ERROR")
