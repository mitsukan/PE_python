import unittest
import problem_17


class Test17(unittest.TestCase):

    def test_can_count_letters_in_single_numbers(self):
        n = problem_17.Prob17()
        self.assertEqual(n.count(1), 3)
        self.assertEqual(n.count(2), 3)
        self.assertEqual(n.count(3), 5)
        self.assertEqual(n.count(4), 4)
        self.assertEqual(n.count(5), 4)
        self.assertEqual(n.count(6), 3)
        self.assertEqual(n.count(7), 5)
        self.assertEqual(n.count(8), 5)
        self.assertEqual(n.count(9), 4)