import sys


def print_sum(s: str):
    """
    Print a summary of character statistics for the given text.

    The function counts and displays:
      - total number of characters
      - number of uppercase letters (A–Z)
      - number of lowercase letters (a–z)
      - number of punctuation marks (.,!?:;)
      - number of whitespace characters (space, tab, newline)
      - number of digits (0–9)
    """
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
    """
    - If more than one argument is provided, the program stops with an
      assertion error.
    - If no argument is provided, the function prompts the user and reads
      the entire text from standard input.
    - If exactly one argument is provided, it is used as the text to analyze.

    The chosen text is then passed to `print_sum` for analysis and display.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provide")
        if len(sys.argv) < 2:
            print("What is the text to count?")
            arg = sys.stdin.read()
        else:
            arg = sys.argv[1]
        print_sum(arg)
    except Exception as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
