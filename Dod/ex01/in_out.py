def square(x: int | float)-> int | float:
    return x * x

def pow(x: int | float)-> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        base = function(x)
        for i in range(count):
            base = function(base)
        count += 1
        return base

    return inner
