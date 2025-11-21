import os


def ft_tqdm(lst: range):
    total = len(lst)
    if total == 0:
        return

    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80

    bar_width = max(10, term_width - 41)
    inner = bar_width - 1

    i = 0
    for value in lst:
        i += 1
        progress = i / total
        filled = int(inner * progress)

        if filled <= 0:
            bar = ">" + "." * (inner - 1)
        elif filled >= inner:
            bar = "=" * (inner - 1) + ">"
        else:
            bar = "=" * (filled - 1) + ">" + "." * (inner - filled)

        percent = int(progress * 100)
        print(f"\r{percent:3d}%|[{bar}]| {i}/{total}", end="", flush=True)
        yield value

    print()


def main():
    pass


if __name__ == "__main__":
    main()
