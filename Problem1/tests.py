from unittest import TestCase, main
from solution import smallest_missing_integer


class Tests(TestCase):

    def test_simple(self):
        self.assertEqual(3, smallest_missing_integer([1, 2]))

    def test_complicated(self):
        self.assertEqual(3, smallest_missing_integer([4, 1, 5, 4, 2]))

    def test_negative_numbers(self):
        self.assertEqual(3, smallest_missing_integer([4, 1, -2, 2, 2]))

    def test_all_negative(self):
        self.assertEqual(1, smallest_missing_integer([-1, -3]))

    def test_readme1(self):
        self.assertEqual(5, smallest_missing_integer([1, 3, 6, 4, 1, 2]))

    def test_readme2(self):
        self.assertEqual(4, smallest_missing_integer([1, 2, 3]))


if __name__ == '__main__':
    main()
