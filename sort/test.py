import unittest
from random import randint

from insertion import insort
from merge import msort


class InsortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.unsorted_array = [-1, 3, 1, 0, -2]
        self.sorted_array = sorted(self.unsorted_array)

    def test_empty_array(self):
        self.assertEqual(insort([]), [])

    def test_single_element_array(self):
        self.assertEqual(insort([2]), [2])

    def test_multiple_elements_array(self):
        self.assertEqual(insort(self.unsorted_array), self.sorted_array)


class MsortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.unsorted_array = [-1, 3, 1, 0, -2]
        self.sorted_array = sorted(self.unsorted_array)

    def test_empty_array(self):
        l = []
        msort(l)
        self.assertEqual(l, [])

    def test_single_element_array(self):
        c = 7
        l = [c]
        msort(l)
        self.assertEqual(l, [c])

    def test_multiple_elements_array(self):
        msort(self.unsorted_array)
        self.assertEqual(self.unsorted_array, self.sorted_array)


if __name__ == '__main__':
    unittest.main()
