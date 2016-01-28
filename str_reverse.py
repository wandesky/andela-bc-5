import unittest


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


def swap(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]


def reversex(s):
    new_s = list(s)
    length = len(s)
    for i in range(len(new_s)//2):
        swap(new_s, i, length - i - 1)

    return "".join(new_s)


def run():
    print reverse("Andela")
    print reverse("Hello")
    print reverse("This is fun.")
    print reversex("Andela")
    print reversex("Hello")
    print reversex("This is fun.")


class TestReverseX(unittest.TestCase):

    def test_reserveses_hello(self):
        self.assertEqual(reversex("hello"), "olleh")

    def test_reverse_catherine(self):
        self.assertEqual(reversex("catherine"), "enirehtac")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()
    run()
