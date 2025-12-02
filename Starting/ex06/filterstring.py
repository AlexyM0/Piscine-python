import sys


def printfilter(string: str, nbr: int) -> None:
    """
    Print the list of words from `string` that are longer than `nbr`.
    """
    words: list[str] = []
    current = ""

    for c in string:
        if c == " ":
            if current != "":
                words.append(current)
                current = ""
        else:
            current += c
    if current != "":
        words.append(current)

    def is_longer(s: str) -> bool:
        """
        Return True if `s` is longer than `nbr`.
        """
        return len(s) > nbr

    filtered = [word for word in words if is_longer(word)]
    print(filtered)


def main():
    """
    Read arguments from command line and call `printfilter`.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        printfilter(sys.argv[1], int(sys.argv[2]))
    except Exception as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
