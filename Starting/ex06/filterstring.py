import sys

def printfilter(string: str, nbr: int):
    words = []
    current = ""

    for c in string:
        if c == ' ':
            if current != "":
                words.append(current)
                current = ""
        else:
            current += c
    if current != "":
        words.append(current)

    is_longer = lambda s: len(s) > nbr
    filtered = [word for word in words if is_longer(word)]
    print(filtered)


def main():
    assert len(sys.argv) == 3, "the arguments are bad"
    printfilter(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()