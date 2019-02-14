import unittest
import problem_6

class Test6(unittest.TestCase):

    def test_example_sum_of_squares(self):
        self.assertEqual(problem_6.sum_of_squares(10), 385)

    def test_example_square_of_sum(self):
        self.assertEqual(problem_6.square_of_sum(10), 3025)

    def test_exammple_difference(self):
        self.assertEqual(problem_6.difference(10), 2640)

if __name__ == '__main__':
    unittest.main()