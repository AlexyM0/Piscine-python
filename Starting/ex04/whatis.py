import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 1:
        sys.exit(0)

    arg = sys.argv[1]

    if arg.startswith("-") and int(arg) == 0:
        raise AssertionError("argument is not an integer")
    if not arg.lstrip("+-").isdigit():
        raise AssertionError("argument is not an integer")

    nbr = int(arg)

    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except Exception as e:
    print("AssertionError:", e)
