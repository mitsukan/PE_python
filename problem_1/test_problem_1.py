import unittest
from problem_1 import problem_1

class Test1(unittest.TestCase):

    def test_3_returns_0(self):
        self.assertEqual(problem_1(3), 0)

    def test_5_returns_3(self):
        self.assertEqual(problem_1(5), 3)

    def test_10_returns_23(self):
        self.assertEqual(problem_1(10), 23)

if __name__ == '__main__':
    unittest.main()