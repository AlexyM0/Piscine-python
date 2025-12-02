import sys


def translate_morse(string: str) -> bool:
    """
    Translate `string` to Morse code and print it.
    Return False if a char is invalid.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    string = string.upper()
    result = ""
    for c in string:
        if c in NESTED_MORSE:
            result += NESTED_MORSE[c]
        else:
            return False
    print(result)
    return True


def main() -> None:
    """
    Check arguments and translate the given string to Morse.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        if not translate_morse(sys.argv[1]):
            raise AssertionError("the arguments are bad")
    except Exception as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
