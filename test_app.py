import unittest
from app import add


class TestApp(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, 5), -5)

    def test_add_float(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_add_large_numbers(self):
        self.assertEqual(add(10**9, 10**9), 2 * 10**9)


if __name__ == '__main__':
    unittest.main()
