import unittest
from katas import add, multiply, power, factorial, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        res = add(1, 1)
        self.assertEqual(res, 2)
        # self.fail("TODO: Write add unit test")

    def test_multiply(self):
        res = multiply(2, 2)
        self.assertEqual(res, 4)
        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        res = power(5, 3)
        self.assertEqual(res, 125)
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        res = factorial(4)
        self.assertEqual(res, 24)
        # self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        res = fibonacci(5)
        self.assertEqual(res, 3)
        # self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
