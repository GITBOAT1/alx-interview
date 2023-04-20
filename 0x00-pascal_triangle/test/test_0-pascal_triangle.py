#!/usr/bin/python3
import unittest
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

class TestPascalTriangle(unittest.TestCase):
    def test_n_less_than_or_equal_to_zero(self):
        self.assertEqual(pascal_triangle(-1), [])
        self.assertEqual(pascal_triangle(0), [])
        
    def test_n_greater_than_zero(self):
        self.assertEqual(pascal_triangle(1), [[1]])
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])
        self.assertEqual(pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

if __name__ == '__main__':
    unittest.main()
