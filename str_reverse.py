def reverse(s):
    """
    Reverse a string using string slicing.

    >>> reverse("Andela")
    'alednA'
    >>> reverse("Hello")
    'olleH'
    >>> reverse("this is fun")
    'nuf si siht'
    >>> reverse("racecar")
    'racecar'
    """
    return s[::-1]


def main():
    print reverse("Andela")
    print reverse("Hello")
    print reverse("This is fun.")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
