import unittest
import problem_8

class Test8(unittest.TestCase):

    def test_solve_first_4_index_in_blob(self):
        n = problem_8.Problem_8()
        self.assertEqual(n.multiply_range(0,4), 126)

    def test_solve_example(self):
        self.assertEqual(problem_8.solver(4), 5832)


if __name__ == '__main__':
    unittest.main()
