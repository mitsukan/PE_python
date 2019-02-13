import unittest
import problem_2

class Test2(unittest.TestCase):

    def test_can_count_fibonacci(self):
        newprob = problem_2.Problem2()
        self.assertEqual(newprob.fibonacci(89), [1,2,3,5,8,13,21,34,55,89])

    def test_solver_8_returns_10(self):
        newprob = problem_2.Problem2()
        newprob.fibonacci(89)
        self.assertEqual(newprob.solver(8), 10)

    def test_solver_610_returns_798(self):
        newprob = problem_2.Problem2()
        newprob.fibonacci(10000)
        self.assertEqual(newprob.solver(610))

if __name__ == '__main__':
    unittest.main()
