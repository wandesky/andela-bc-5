import unittest

from mathx.super_sum import super_sum


class SuperSumTest(unittest.TestCase):
    """Test cases for the super_sum function."""

    def test_two_numbers(self):
        result = super_sum(20, 20)
        self.assertEqual(result, 40)

    def test_four_numbers(self):
        result = super_sum(10, 15, 18, 20)
        self.assertEqual(result, 63)

    def sum_two_lists(self):
        a = [10, 20, 30, 40]
        b = [100, 20]
        result = super_sum(a, b)
        self.assertEqual(result, 220)

    def test_a_list_and_number(self):
        a = [10, 30, 50]
        result = super_sum(a, 50)
        self.assertEqual(result, 140)

    def test_four_lists(self):
        a, b, c, d = [1, 2], [2, 3], [3], [4, 10]
        result = super_sum(a, b, c, d)
        self.assertEqual(result, 25)

    def test_large_input(self):
        big_a = [i ** 3 for i in xrange(1000)]
        self.assertEqual(super_sum(big_a), sum(big_a))

    def test_with_nested_lists(self):
        a = [2, 3, 4, (8, 5, (4, 5, 6), [4, 5], 6), 4, {3, 4, 6, (3, 4), 2}, 3, 2]
        self.assertEqual(super_sum(a), 83)
