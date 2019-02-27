import unittest
import problem_10

class Test10(unittest.TestCase):


    def test_create_primes(self):
        n = problem_10.Prob10()
        self.assertEqual(n.create_primes(10), [2,3,5,7])

    def test_sum_of_primes(self):
        n = problem_10.Prob10()
        self.assertEqual(n.sum_of_primes(10), 17)

    def test_solution_finder(self):
        n = problem_10.Prob10()
        print('solution to problem 10:')
        print(n.sum_of_primes(2000000))


if __name__ == '__main__':
    unittest.main()
