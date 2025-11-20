import sys


def print_sum(s: str):
    size = len(s)
    count_upper = 0
    count_lower = 0
    count_ponct = 0
    count_space = 0
    count_digit = 0

    for c in s:
        if 'A' <= c <= 'Z':
            count_upper += 1
        elif 'a' <= c <= 'z':
            count_lower += 1
        elif '0' <= c <= '9':
            count_digit += 1
        elif c == ' ' or c == '\t' or c == '\n':
            count_space += 1
        elif (
            c == '.'
            or c == ','
            or c == '!'
            or c == '?'
            or c == ':'
            or c == ';'
        ):
            count_ponct += 1

    print("The text contains", size, "characters:")
    print(count_upper, "upper letters")
    print(count_lower, "lower letters")
    print(count_ponct, "punctuation marks")
    print(count_space, "spaces")
    print(count_digit, "digits")


def main():
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) < 2:
        print("What is the text to count?")
        arg = sys.stdin.read()
    else:
        arg = sys.argv[1]
    print_sum(arg)


if __name__ == "__main__":
    main()
