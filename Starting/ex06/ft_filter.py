
def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]

##def is_even(n):
    ##return n % 2 == 0

def main():
    #print(ft_filter(is_even, [1, 2, 3, 4]))

if __name__ == "__main__":
    main()