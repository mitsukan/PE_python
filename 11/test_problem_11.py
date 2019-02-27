import unittest
from unittest.mock import MagicMock
import problem_11



class Test11(unittest.TestCase):

    def test_can_store_a_high_score(self):
        n = problem_11.Prob11()
        self.assertEqual(n.high_score, 0)
        self.assertEqual(n.high_combo, [])

    def test_product_method(self):
        n = problem_11.Prob11()
        self.assertEqual(n.product(2,3,4,5), 120)

    def test_iterate_horizontally(self):
        n = problem_11.Prob11()
        n.iterate_horizontally = MagicMock()
        n.iterate_horizontally()
        n.iterate_horizontally.assert_called

    def test_product_vertically(self):
        n = problem_11.Prob11()
        n.iterate_vertically = MagicMock()
        n.iterate_vertically()
        n.iterate_vertically.assert_called