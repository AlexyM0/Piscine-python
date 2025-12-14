def callLimit(limit: int):
    """Return a decorator that limits how many
    times a function can be called."""
    count = 0

    def callLimiter(function):
        """Decorate `function` to enforce
        the maximum number of allowed calls."""
        def limit_function(*args: any, **kwds: any):
            """Wrapper that counts calls and prints
            an error if the limit is exceeded."""
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
