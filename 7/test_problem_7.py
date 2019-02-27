import unittest
import problem_7

class Test7(unittest.TestCase):

    def test_aggregate_6_prime_numbers(self):
        m = problem_7.Problem7()
        self.assertEqual(m.aggregate_primes(6), 13)

    def test_return_solution(self):
        m = problem_7.Problem7()
        print('solution to 7:', m.aggregate_primes(10001))

if __name__ == '__main__':
    unittest.main()

