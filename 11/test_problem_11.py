import unittest
import problem_11

class Test11(unittest.TestCase):

    def test_sum_of_a_horizontal_left(self):
        n = problem_11.Prob11()
        self.assertEqual(n.product(2,3,4,5), 120)