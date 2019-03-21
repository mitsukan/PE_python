import unittest
import problem_17


class Test17(unittest.TestCase):

    def test_can_count_letters_in_unique_numbers(self):
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
        self.assertEqual(n.count(10), 3)
        self.assertEqual(n.count(11), 6)
        self.assertEqual(n.count(12), 6)
        self.assertEqual(n.count(13), 8)
        # self.assertEqual(n.count(15), 7)
        # self.assertEqual(n.count(18), 8)

    # def test_can_count_letters_in_teen_numbers(self):
    #     n = problem_17.Prob17()
    #     self.assertEqual(n.count(14), 8)
    #     self.assertEqual(n.count(16), 7)
    #     self.assertEqual(n.count(17), 9)
    #     self.assertEqual(n.count(19), 8)
    #     self.assertEqual(n.count(20), 6)
    #
    # def test_can_count_letters_in_twenty_numbers(self):
    #     n = problem_17.Prob17()