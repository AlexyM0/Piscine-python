import sys

assert len(sys.argv) <= 2, "more than one argument is provide"

if len(sys.argv) == 1:
    sys.exit(0)

arg = sys.argv[1]
assert arg != "-0", "argument is not an integer"
assert arg.lstrip("+-").isdigit(), "argument is not an integer"

nbr = int(arg)

if nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
