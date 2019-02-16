import unittest
import problem_8

class Test8(unittest.TestCase):

    def test_solve_first_4_index_in_blob(self):
        n = problem_8.Problem_8()
        self.assertEqual(n.multiply_range(0,4), 126)

    def test_solve_example(self):
        n = problem_8.Problem_8()
        self.assertEqual(n.solver(4), 5832)

    def test_solve_problem(self):
        n = problem_8.Problem_8()
        print('answer to problem 8:')
        print(n.solver(13))

if __name__ == '__main__':
    unittest.main()
