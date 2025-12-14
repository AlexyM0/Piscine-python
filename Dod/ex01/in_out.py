def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that applies `function`
    repeatedly to x on each call."""
    count = 0

    def inner() -> float:
        """Compute function(x) the first time, then function
        applied more times each call."""
        nonlocal count
        base = function(x)
        for i in range(count):
            base = function(base)
        count += 1
        return base

    return inner
