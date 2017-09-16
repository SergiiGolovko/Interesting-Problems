from unittest import TestCase, main
from solution import smallest_missing_integer


class Tests(TestCase):

    def test_simple(self):
        self.assertEqual(3, smallest_missing_integer([1, 2]))

    def test_complicated(self):
        self.assertEqual(3, smallest_missing_integer([4, 1, 5, 4, 2]))

    def test_negative_numbers(self):
        self.assertEqual(3, smallest_missing_integer([4, 1, -2, 2, 2]))


if __name__ == '__main__':
    main()
