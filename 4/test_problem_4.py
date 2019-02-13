import unittest
import problem_4

class Test4(unittest.TestCase):

    def test_palindrome_checker(self):
        n = problem_4.Problem_4()
        self.assertEqual(n.is_pal(9009), True)

    def test_solver1(self):
        n = problem_4.Problem_4()
        self.assertEqual(n.solver(99, 99), 9009)

    def test_solver2(self):
        n = problem_4.Problem_4()
        n.solver(999,999)

if __name__ == '__main__':
    unittest.main()