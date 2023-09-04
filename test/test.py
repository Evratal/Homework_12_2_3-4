import unittest

from utils.arrs import get, my_slice


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([], 0, "test"), "test")


class TestSlice(unittest.TestCase):
    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1, ), [2, 3])
        self.assertEqual(my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(my_slice([]), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -3, -1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], -6, -1), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], 0,5), [1, 2, 3, 4])

