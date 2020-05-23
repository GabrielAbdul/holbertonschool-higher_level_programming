#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """
        method to test max int values of a list with max_integer()
        """
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([5, 5, 5, 6]), 6)
        self.assertEquals(max_integer([51, 287, 32, 46]), 287)
        self.assertEquals(max_integer([1, 32, 3, 4]), 32)
        self.assertEquals(max_integer([1, 2, 3, 4, 5]), 5)

    if __name__ == '__main__':
        unittest.main()
